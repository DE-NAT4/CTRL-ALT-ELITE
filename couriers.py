from db import get_connection



def view_couriers():
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:

                cur.execute("""
                    SELECT courier_id, name, phone
                    FROM couriers
                    ORDER BY courier_id ASC;
                """)

                couriers = cur.fetchall()

                print("\n--- COURIERS ---")
                for c in couriers:
                    print(f"{c[0]} | {c[1]} | {c[2]}")

    except Exception as e:
        print("Error viewing couriers:", e)



def add_courier(name, phone):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:

                cur.execute("""
                    INSERT INTO couriers (name, phone)
                    VALUES (%s, %s)
                    RETURNING courier_id;
                """, (name, phone))

                new_id = cur.fetchone()[0]
                conn.commit()

                print(f"Courier added successfully (ID: {new_id})")

    except Exception as e:
        print("Error adding courier:", e)



def update_courier(courier_id, name, phone):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:

                cur.execute("""
                    UPDATE couriers
                    SET name = %s,
                        phone = %s
                    WHERE courier_id = %s;
                """, (name, phone, courier_id))

                conn.commit()

                print("Courier updated successfully!")

    except Exception as e:
        print("Error updating courier:", e)



def delete_courier(courier_id):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:

                cur.execute("""
                    DELETE FROM couriers
                    WHERE courier_id = %s;
                """, (courier_id,))

                conn.commit()

                print("Courier deleted successfully!")

    except Exception as e:
        print("Error deleting courier:", e)