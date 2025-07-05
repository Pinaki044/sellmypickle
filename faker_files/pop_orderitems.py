import mysql.connector
import random

conn = mysql.connector.connect(
    host="localhost",
    user="pinaki",
    password="root",  # 🔁 replace
    database="pickle"
)

cursor = conn.cursor()

# Fetch all order ids
cursor.execute("SELECT Orderid FROM Orders")
order_ids = [row[0] for row in cursor.fetchall()]

# Fetch all item ids
cursor.execute("SELECT Itemid FROM Item")
item_ids = [row[0] for row in cursor.fetchall()]

# Each order will contain 1–5 random items
for order_id in order_ids:
    num_items = random.randint(1, 5)
    selected_items = random.sample(item_ids, num_items)

    for item_id in selected_items:
        quantity = random.randint(1, 3)
        cursor.execute("""
            INSERT INTO OrderItems (order_id, item_id, quantity)
            VALUES (%s, %s, %s)
        """, (order_id, item_id, quantity))

conn.commit()
print("✅ OrderItems table populated.")
cursor.close()
conn.close()

