from neo4j import GraphDatabase


NEO4J_API = "bolt://0.0.0.0:7687"
AUTH = ("test", "test")
DB = "neo4j"


def read_input(input_file):
    """Read the input file and return it in digestible chunks"""
    try:
        with open(input_file, "r") as inp:
            input_str = inp.read().strip()
            input_list = input_str.split("\n")
            return input_list
    except (FileNotFoundError, PermissionError) as err:
        raise SystemExit(
            f"Failed to read specified input file {input_file} with exception:\n{err}"
        )


def rule_to_data(rule):
    """Given a rule (line in the puzzle input), return relevant data."""
    # Short rule:
    # 'light red bags contain 1 bright white bag, 2 muted yellow bags.'

    # Long rule:
    # muted coral bags contain 5 faded violet bags, 2 drab red bags, 3 muted olive bags, 4 mirrored tomato bags.

    # Terminal rule:
    # dotted gray bags contain no other bags.

    r = (
        rule.replace("bags ", "")
        .replace("bags, ", ", ")
        .replace(" bags.", "")
        .replace(" bag.", "")
        .replace("bag", "")
    )
    spl = r.split(" contain ")
    outer_color = spl[0]
    if "no other bags." in rule:
        return (outer_color, None)
    inners = []
    sub_rules = spl[1].split(" , ")
    for s in sub_rules:
        num = int(s[0])
        color = s[1:].strip()
        inners.append((num, color))

    return (outer_color, inners)


def node_exists(color):
    """Check whether a node like "faded blue" exists in the database."""
    query = "MATCH (b:Bag {color: '%s'}) RETURN count(b)" % color
    with GraphDatabase.driver(NEO4J_API, auth=AUTH, encrypted=False) as driver:
        records, _, _ = driver.execute_query(query, database_=DB)
    count = records[0].values()[0]
    return count > 0


def get_data_state(data):
    """Decide which state the data are in, return as a string e.g. ("1a2c").

    Given example data like:
        data = ('vibrant plum', [(5, 'faded blue'), (6, 'dotted black')])
    We need to know whether:
        1a. The outer bag exists.
        1b. The outer bag does not exist
        2a. The inner bags all exist.
        2b. The inner bags all don't exist.
        2c. Some inner bags exist; others don't.
        2d. There are no inner bags defined. This is a terminal bag.
    """
    outer_exists = node_exists(data[0])
    outer_state = "1a" if outer_exists else "1b"
    inners = data[1]
    if not inners:
        inner_state = "2d"
        return outer_state + inner_state
    inners_exist = [node_exists(i[1]) for i in inners]
    if all(inners_exist):
        inner_state = "2a"
    elif any(inners_exist):
        inner_state = "2b"
    else:
        inner_state = "2c"

    return outer_state + inner_state


def build_cypher_query(data, state):
    """Given rule data and a state from `get_data_state`, construct an idempotent Cypher query."""
    # Initialize some empty lists for MATCH, CREATE, and MERGE statements
    matches = []
    creates = []
    merges = []

    outer_color = data[0]
    match state:
        case "1a2a":  # Outer bag and all inner bags exist; this should be a no-op.
            return
        case "1a2b":  # Outer bag exists, but all inner bags don't exist; match outer, create all inners + rel's.
            outer_node_var = outer_color.replace(" ", "_")
            matches.append(
                "MATCH (%s:Bag {color: '%s'})" % (outer_node_var, outer_color)
            )
            inners = data[1]
            for i in inners:
                count, color = i
                node_var = color.replace(" ", "_")
                creates.append("CREATE (%s:Bag {color: '%s'})" % (node_var, color))
                creates.append(
                    "CREATE (%s)-[:contains {count: %d}]->(%s)"
                    % (outer_node_var, count, node_var)
                )
        case "1a2c":  # Outer bag exists, mixture of non-existent and existent inners.
            outer_node_var = outer_color.replace(" ", "_")
            matches.append(
                "MATCH (%s:Bag {color: '%s'})" % (outer_node_var, outer_color)
            )
            inners = data[1]
            for i in inners:
                count, color = i
                node_var = color.replace(" ", "_")
                if node_exists(color):
                    matches.append("MATCH (%s:Bag {color: '%s'})" % (node_var, color))
                    merges.append(
                        "MERGE (%s)-[:contains {count: %d}]->(%s)"
                        % (outer_node_var, count, node_var)
                    )
                else:
                    creates.append("CREATE (%s:Bag {color: '%s'})" % (node_var, color))
                    creates.append(
                        "CREATE (%s)-[:contains {count: %d}]->(%s)"
                        % (outer_node_var, count, node_var)
                    )
        case "1a2d":  # Outer bag exists, no inner bags defined; this should be a no-op.
            return
        case "1b2a":  # Outer bag does not exist, but all inner bags exist; create outer bag + rel's.
            outer_node_var = outer_color.replace(" ", "_")
            creates.append(
                "CREATE (%s:Bag {color: '%s'})" % (outer_node_var, outer_color)
            )
            inners = data[1]
            for i in inners:
                count, color = i
                node_var = color.replace(" ", "_")
                matches.append("MATCH (%s:Bag {color: '%s'})" % (node_var, color))
                creates.append(
                    "CREATE (%s)-[:contains {count: %d}]->(%s)"
                    % (outer_node_var, count, node_var)
                )
        case "1b2b":  # Outer bag does not exist and neither do any inners. Create all the things.
            outer_node_var = outer_color.replace(" ", "_")
            creates.append(
                "CREATE (%s:Bag {color: '%s'})" % (outer_node_var, outer_color)
            )
            inners = data[1]
            for i in inners:
                count, color = i
                node_var = color.replace(" ", "_")
                creates.append("CREATE (%s:Bag {color: '%s'})" % (node_var, color))
                creates.append(
                    "CREATE (%s)-[:contains {count: %d}]->(%s)"
                    % (outer_node_var, count, node_var)
                )
        case "1b2c":  # Outer bag does not exist, and some inners exist. Create outer + rel's and some inners, match others.
            outer_node_var = outer_color.replace(" ", "_")
            creates.append(
                "CREATE (%s:Bag {color: '%s'})" % (outer_node_var, outer_color)
            )
            inners = data[1]
            for i in inners:
                count, color = i
                node_var = color.replace(" ", "_")
                if node_exists(color):
                    matches.append("MATCH (%s:Bag {color: '%s'})" % (node_var, color))
                    merges.append(
                        "MERGE (%s)-[:contains {count: %d}]->(%s)"
                        % (outer_node_var, count, node_var)
                    )
                else:
                    creates.append("CREATE (%s:Bag {color: '%s'})" % (node_var, color))
                    creates.append(
                        "CREATE (%s)-[:contains {count: %d}]->(%s)"
                        % (outer_node_var, count, node_var)
                    )
        case "1b2d":  # Outer bag does not exist, and inners are not defined. Just create outer.
            outer_node_var = outer_color.replace(" ", "_")
            creates.append(
                "CREATE (%s:Bag {color: '%s'})" % (outer_node_var, outer_color)
            )
        case _:  # Catch-all case that shouldn't be possible.
            raise SystemExit(
                f"{state}: Bag is in the netherrealm between existence and oblivion."
            )

    return "\n".join(matches + creates + merges)


def main():
    rules = read_input("test_input.txt")
    rules_data = [rule_to_data(rule) for rule in rules]
    states = [get_data_state(rd) for rd in rules_data]
    data_states = [x for x in zip(rules_data, states)]
    queries = []
    for data, state in data_states:
        print(f"Data: {data}, State: {state}")
        query = build_cypher_query(data, state)
        print(f"Query:\n{query}\n")
        queries.append(query)

    with GraphDatabase.driver(NEO4J_API, auth=AUTH, encrypted=False) as driver:
        driver.verify_connectivity()
        for query in queries:
            driver.execute_query(query, database_=DB)
            # records, _, _ = driver.execute_query("MATCH (b:Bag) RETURN b")
            # for record in records:
            #     print(record)


if __name__ == "__main__":
    main()
