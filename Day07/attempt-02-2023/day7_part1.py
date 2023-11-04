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
    # 'light red bags contain 1 bright white bag, 2 muted yellow bags.'
    # 'light red contain 1 bright white, 2 muted yellow bags.'
    r = rule.replace('bags ', '').replace('bags, ', ', ').replace(' bags.', '').replace(' bag.', '').replace('bag', '')
    spl = r.split(' contain ')
    outer_color = spl[0]
    if 'no other bags.' in rule:
        return (outer_color, None)
    inners = []
    sub_rules = spl[1].split(' , ')
    for s in sub_rules:
        num = int(s[0])
        color = s[1:].strip()
        inners.append((num, color))

    return (outer_color, inners)


def main():
    # with GraphDatabase.driver(NEO4J_API, auth=AUTH, encrypted=False) as driver:
    #     driver.verify_connectivity()
    #     records, _, _ = driver.execute_query("MATCH (n) RETURN n;", database_=DB)
    #     for record in records:
    #         print(record)
    rules = read_input("test_input.txt")
    rules_data = [rule_to_data(rule) for rule in rules]
    for rd in rules_data:
        print(rd)


if __name__ == "__main__":
    main()
