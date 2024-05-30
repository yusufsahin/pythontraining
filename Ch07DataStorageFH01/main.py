import psycopg2
from psycopg2 import sql

def create_connection():
    return  psycopg2.connect(
        dbname='myDb',
        user='postgres',
        password='my@PassWd2024',
        host='localhost',
        port='5432'
    )

def create_table(conn):
    with conn.cursor() as cur:
        cur.execute('''
        CREATE TABLE IF NOT EXISTS employees(
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        salary NUMERIC
        )
        ''')
        conn.commit()
def insert_employee(conn,name,salary):
    with conn.cursor() as cur:
        cur.execute('''
        INSERT INTO employees(name,salary) VALUES (%s,%s) 
        ''',(name,salary))
        conn.commit()

def fetch_employees(conn):
    with conn.cursor() as cur:
        cur.execute('SELECT * FROM employees')
        rows = cur.fetchall()
        for row in rows:
            print(row)
def main():
    conn=create_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            db_version=cur.fetchone()
            print(f"Database version: {db_version[0]}")

        create_table(conn)
        insert_employee(conn,'John Doe',50000)
        insert_employee(conn,'Jane Doe',60000)

        fetch_employees(conn)

    finally:
        conn.close()

if __name__ == '__main__':
    main()