import mysql.connector
import random

conn = mysql.connector.connect(
    host="localhost",
    user="pinaki",
    password="root",  # 🔁 replace
    database="pickle"
)

cursor = conn.cursor()

# Fetch order ids
cursor.execute("SELECT Orderid FROM Orders")
order_ids = [row[0] for row in cursor.fetchall()]

# For each order, calculate total amount and insert payment
for order_id in order_ids:
    # Get all items in the order
    cursor.execute("""
        SELECT I.price, OI.quantity
        FROM OrderItems OI
        JOIN Item I ON OI.item_id = I.Itemid
        WHERE OI.order_id = %s
    """, (order_id,))
    
    items = cursor.fetchall()
    total_amount = sum(price * qty for price, qty in items)

    mode = random.choice(["UPI", "Cash", "Card", "Netbanking"])
    status = random.choice(["Paid", "Pending", "Failed"])

    cursor.execute("""
        INSERT INTO Payment (order_id, mode, amount, status)
        VALUES (%s, %s, %s, %s)
    """, (order_id, mode, total_amount, status))

conn.commit()
print("✅ Payment table populated.")
cursor.close()
conn.close()

