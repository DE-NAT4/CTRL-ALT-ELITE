from db import get_connection



def view_orders():
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:

                cur.execute("""
                    SELECT
                        o.order_id,
                        o.customer_name,
                        o.customer_address,
                        o.customer_phone,
                        c.name AS courier_name,
                        o.status
                    FROM orders o
                    LEFT JOIN couriers c
                        ON o.courier_id = c.courier_id
                    ORDER BY o.order_id ASC;
                """)

                orders = cur.fetchall()

                print("\n--- ORDERS ---")
                for o in orders:
                    print(f"""
Order ID: {o[0]}
Customer: {o[1]}
Address: {o[2]}
Phone: {o[3]}
Courier: {o[4]}
Status: {o[5]}
-------------------------
""")

    except Exception as e:
        print("Error viewing orders:", e)



def add_order(customer_name, customer_address, customer_phone, courier_id, status):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:

                cur.execute("""
                    INSERT INTO orders (
                        customer_name,
                        customer_address,
                        customer_phone,
                        courier_id,
                        status
                    )
                    VALUES (%s, %s, %s, %s, %s)
                    RETURNING order_id;
                """, (
                    customer_name,
                    customer_address,
                    customer_phone,
                    courier_id,
                    status
                ))

                new_id = cur.fetchone()[0]
                conn.commit()

                print(f"Order added successfully (ID: {new_id})")

    except Exception as e:
        print("Error adding order:", e)



def update_order_status(order_id, new_status):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:

                cur.execute("""
                    UPDATE orders
                    SET status = %s
                    WHERE order_id = %s;
                """, (new_status, order_id))

                conn.commit()

                print("Order status updated successfully!")

    except Exception as e:
        print("Error updating order status:", e)



def delete_order(order_id):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:

                cur.execute("""
                    DELETE FROM orders
                    WHERE order_id = %s;
                """, (order_id,))

                conn.commit()

                print("Order deleted successfully!")

    except Exception as e:
        print("Error deleting order:", e)



def view_orders_by_status(status):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:

                cur.execute("""
                    SELECT order_id, customer_name, status
                    FROM orders
                    WHERE status = %s;
                """, (status,))

                rows = cur.fetchall()

                print(f"\n--- ORDERS WITH STATUS: {status} ---")
                for r in rows:
                    print(f"{r[0]} | {r[1]} | {r[2]}")

    except Exception as e:
        print("Error filtering orders by status:", e)



def view_orders_by_courier(courier_id):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:

                cur.execute("""
                    SELECT o.order_id, o.customer_name, o.status, c.name
                    FROM orders o
                    LEFT JOIN couriers c
                        ON o.courier_id = c.courier_id
                    WHERE o.courier_id = %s;
                """, (courier_id,))

                rows = cur.fetchall()

                print(f"\n--- ORDERS FOR COURIER {courier_id} ---")
                for r in rows:
                    print(f"{r[0]} | {r[1]} | {r[2]} | {r[3]}")

    except Exception as e:
        print("Error filtering orders by courier:", e)