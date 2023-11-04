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


def rule_data_to_cypher(rd):
    """Given rule data, generate a Cypher query to create nodes + rel's."""
    # ('vibrant plum', [(5, 'faded blue'), (6, 'dotted black')])
    # ('faded blue', None)
    outer_color = rd[0]
    inners = rd[1]
    if node_exists(outer_color):
        if not inners:
            print('Nothing to create')
        exist_list = [node_exists(x[1]) for x in inners]
        if all(exist_list):
            print('Nothing to create')
        non_exist_index = [i for i, x in enumerate(exist_list) if x == 0]
        query = "MATCH (outer:Bag {color: '%s'})\n" % outer_color
        query += "CREATE "
        for n in non_exist_index:
            count, color = inners[n]
            query += "(outer)-[:contains {count: %d}]->(:Bag {color: '%s'}),\n" % (count, color)
        query = query.rstrip('\n').rstrip(",")
    else:
        query = "CREATE (outer:Bag {color: '%s'})" % outer_color
        if inners:
            query += ",\n"
            for index, i in enumerate(inners):
                c, n = i
                query += "(b%s:Bag {color: '%s'})<-[:contains {count: %d}]-(outer)" % (
                    index,
                    n,
                    c,
                )
                if index < len(inners) - 1:
                    query += ",\n"
    return query


def main():
    rules = read_input("test_input.txt")
    rules_data = [rule_to_data(rule) for rule in rules]
    queries = [rule_data_to_cypher(x) for x in rules_data[:3]]
    for query in queries:
        print(query)

    # with GraphDatabase.driver(NEO4J_API, auth=AUTH, encrypted=False) as driver:
    #     driver.verify_connectivity()
    #     driver.execute_query(query, database_=DB)
    #     records, _, _ = driver.execute_query("MATCH (b:Bag) RETURN b")
    #     for record in records:
    #         print(record)


if __name__ == "__main__":
    main()
