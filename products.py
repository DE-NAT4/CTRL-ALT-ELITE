from db import get_connection



def view_products():
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:

                cur.execute("""
                    SELECT id, name, price
                    FROM products
                    ORDER BY id ASC;
                """)

                products = cur.fetchall()

                print("\n--- PRODUCTS ---")
                if len(products) == 0:
                    print("No products found")
                else:
                    for p in products:
                        print(f"{p[0]} | {p[1]} | £{p[2]}")

    except Exception as e:
        print("Error viewing products:", e)



def add_product(name, price):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:

                cur.execute("""
                    INSERT INTO products (name, price)
                    VALUES (%s, %s)
                    RETURNING id;
                """, (name, price))

                new_id = cur.fetchone()[0]
                conn.commit()

                print(f"Product added successfully (ID: {new_id})")

    except Exception as e:
        print("Error adding product:", e)



def update_product(product_id, name, price):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:

                cur.execute("""
                    UPDATE products
                    SET name = %s,
                        price = %s
                    WHERE id = %s;
                """, (name, price, product_id))

                conn.commit()

                print("Product updated successfully!")

    except Exception as e:
        print("Error updating product:", e)



def delete_product(product_id):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:

                cur.execute("""
                    DELETE FROM products
                    WHERE id = %s;
                """, (product_id,))

                conn.commit()

                print("Product deleted successfully!")

    except Exception as e:
        print("Error deleting product:", e)
