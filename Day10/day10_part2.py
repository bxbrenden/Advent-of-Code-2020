from typing import List

from neo4j import GraphDatabase


def read_input(input_file):
    """Read the input file and return it in digestible chunks"""
    try:
        with open(input_file, "r") as inp:
            input_str = inp.read().strip()
            input_list = sorted([int(n) for n in input_str.split("\n")])
            if input_list[0] != 0:
                input_list.insert(0, 0)
            final_val = input_list[-1]
            input_list.append(final_val + 3)
            print('\n'.join([str(x) for x in sorted(input_list)]))
            return sorted(input_list)
    except (FileNotFoundError, PermissionError) as err:
        raise SystemExit(
            f"Failed to read input file {input_file} with exception:\n{err}"
        )


def find_joltage_diffs(puz: List[int], three_diffs: int = 0, one_diffs: int = 1) -> int:
    try:
        new_diff = puz[1] - puz[0]
        print(f"Diff: {puz[1]} - {puz[0]} = {new_diff}")
        if new_diff == 1:
            print(f"one diffs += 1, now at {one_diffs + 1}")
            one_diffs += 1
        elif new_diff == 3:
            print(f"three diffs += 1, now at {three_diffs + 1}")
            three_diffs += 1
        if len(puz) <= 2:
            print(f"Adding one more to three_diffs value {three_diffs}")
            three_diffs += 1
            print(f"Final one diffs: {one_diffs}")
            print(f"Final three diffs: {three_diffs}")
            return one_diffs * three_diffs
        else:
            return find_joltage_diffs(puz[1:], three_diffs, one_diffs)
    except IndexError:
        raise SystemExit("This is unexpected...")


def create_base_nodes(node_list):
    # Define correct URI and AUTH arguments (no AUTH by default)
    # node_list_str = "[" + ', '.join([str(x) for x in node_list]) + "]"
    URI = "bolt://localhost:7687"
    AUTH = ("", "")
    with GraphDatabase.driver(URI, auth=AUTH) as client:
        # Check the connection
        client.verify_connectivity()
        records, summary, keys = client.execute_query(
            "UNWIND $node_list AS n MERGE (:Adapter {name: n})",
            node_list=node_list,
            database_="memgraph",
        )

        # Get the result
        for record in records:
            print(record["name"])


def create_all_relationships(node_list):
    first = node_list[0]
    second = node_list[1]
    URI = "bolt://localhost:7687"
    AUTH = ("", "")
    with GraphDatabase.driver(URI, auth=AUTH) as client:
        # Check the connection
        client.verify_connectivity()
        query = "MATCH (a:Adapter {name: $first}), (b:Adapter {name: $second}) "
        query += "MERGE (a)-[:converts]->(b)"
        records, summary, keys = client.execute_query(
            query,
            first=first,
            second=second,
            database_="memgraph",
        )

        # Get the result
        for record in records:
            print(record["name"])

    if len(node_list) > 2:
        return create_all_relationships(node_list[1:])
    else:
        return True


def validate_inner_relationships():
    URI = "bolt://localhost:7687"
    AUTH = ("", "")
    with GraphDatabase.driver(URI, auth=AUTH) as client:
        # Check the connection
        client.verify_connectivity()
        query = "MATCH (alpha:Adapter {name: 1})-[ab:converts]->(beta:Adapter)-[r:converts*]->(gamma:Adapter)-[s:converts*]->(psi:Adapter)-[yz:converts]->(omega:Adapter) "
        query += "MATCH (o:Adapter)-[og:converts]->(gamma) "
        query += "WHERE gamma.name - o.name > 3 "
        query += "RETURN count(og)"
        records, summary, keys = client.execute_query(
            query,
            database_="memgraph",
        )

        # Get the result
        for record in records:
            return int(record["count(og)"])


def validate_edge_relationships(puz):
    results = []
    start = min(puz)
    end = max(puz)
    URI = "bolt://localhost:7687"
    AUTH = ("", "")
    with GraphDatabase.driver(URI, auth=AUTH) as client:
        # Check the connection
        query = "MATCH (psi:Adapter)-[yz:converts]->(omega:Adapter {name: $end})\n"
        query += "WHERE omega.name - psi.name > 3\n"
        query += "RETURN count(yz) as result"
        records, summary, keys = client.execute_query(
            query,
            end=end,
            database_="memgraph",
        )
        print(query)

        # Get the result
        for record in records:
            results.append(int(record["result"]))

    with GraphDatabase.driver(URI, auth=AUTH) as client:
        query = "MATCH (alpha:Adapter {name: $start})-[ab:converts]->(beta:Adapter)\n"
        query += "WHERE beta.name - alpha.name > 3\n"
        query += "RETURN count(ab) AS result"
        records, summary, keys = client.execute_query(
            query,
            start=start,
            database_="memgraph",
        )
        for record in records:
            results.append(int(record["result"]))

    return results


def build_dag(puz):
    """Build a directed, acyclic graph out of nodes."""
    first = puz[0]
    query = "MATCH (a:Adapter {name: $first})\n"
    query += "MATCH (o:Adapter) WHERE o.name > a.name AND o.name - a.name <= 3\n"
    query += "MERGE (a)-[:converts]->(o)"
    URI = "bolt://localhost:7687"
    AUTH = ("", "")
    with GraphDatabase.driver(URI, auth=AUTH) as client:
        records, summary, keys = client.execute_query(
            query,
            first=first,
            database_="memgraph",
        )

        # Get the result
        for record in records:
            print(record["name"])
    if len(puz) > 2:
        return build_dag(puz[1:])
    else:
        return True


def main():
    puz = read_input("puzzle_input.txt")
    create_base_nodes(puz)
    build_dag(puz)
    # create_all_relationships(puz)
    # assert validate_inner_relationships() == 0
    # assert validate_edge_relationships(puz) == [0, 0]
    # print("\n".join([str(p) for p in puz]))
    # answer = find_joltage_diffs(puz)
    # print(f'ANSWER: {answer}')


if __name__ == "__main__":
    main()
