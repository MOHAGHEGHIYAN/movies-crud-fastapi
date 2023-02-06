from mysql import connector
import os
from dotenv import load_dotenv

load_dotenv()


def initialize_db_tables():
    tables_sql = open(
        os.path.join(os.path.dirname(__file__), "sqls/create_db_tables.sql"), "r"
    ).read()
    db = connector.connect(
        host=os.getenv("MYSQL_DB_HOST"),
        port=os.getenv("MYSQL_DB_PORT"),
        user=os.getenv("MYSQL_DB_USER"),
        password=os.getenv("MYSQL_DB_PASS"),
        database=os.getenv("MYSQL_DB_NAME"),
    )
    db_cursor = db.cursor()
    db_cursor.execute(tables_sql)
    print("db and its tables created successfully")


if __name__ == "__main__":
    initialize_db_tables()
