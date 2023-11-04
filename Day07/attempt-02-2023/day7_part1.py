from neo4j import GraphDatabase


NEO4J_API = "bolt://0.0.0.0:7687"
AUTH = ("test", "test")
DB = "neo4j"

with GraphDatabase.driver(NEO4J_API, auth=AUTH, encrypted=False) as driver:
    driver.verify_connectivity()
    records, _, _ = driver.execute_query(
        "MATCH (n) RETURN n;", database_=DB
    )
    for record in records:
        print(record)
