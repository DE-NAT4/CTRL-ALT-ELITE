import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

host_name = os.getenv("POSTGRES_HOST")
database_name = os.getenv("POSTGRES_DB")
user_name = os.getenv("POSTGRES_USER")
user_password = os.getenv("POSTGRES_PASSWORD")

def get_connection():
    return psycopg2.connect(
        host=host_name,
        dbname=database_name,
        user=user_name,
        password=user_password
    )
def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    # PRODUCTS
    cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product_id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        price DECIMAL
    );
    """)

    # COURIERS
    cur.execute("""
    CREATE TABLE IF NOT EXISTS couriers (
        courier_id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(20)
    );
    """)

    # ORDERS
    cur.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id SERIAL PRIMARY KEY,
        customer_name VARCHAR(100),
        customer_address VARCHAR(100),
        customer_phone VARCHAR(20),
        courier_id INT,
        status INT,
        items TEXT
    );
    """)

    conn.commit()
    cur.close()
    conn.close()

    print("Tables created!")

if __name__ == "__main__":
    create_tables()