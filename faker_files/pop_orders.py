import mysql.connector
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

conn = mysql.connector.connect(
    host="localhost",
    user="pinaki",
    password="root",  # 🔁 replace with your password
    database="pickle"
)

cursor = conn.cursor()

# Fetch customer IDs
cursor.execute("SELECT Cid FROM Customer")
customer_ids = [row[0] for row in cursor.fetchall()]

for _ in range(10000):
    customer_id = random.choice(customer_ids)
    order_date = fake.date_between(start_date='-2M', end_date='today')
    order_time = fake.time()

    cursor.execute("""
        INSERT INTO Orders (customer_id, order_date, order_time)
        VALUES (%s, %s, %s)
    """, (customer_id, order_date, order_time))

conn.commit()
print("✅ Orders table populated.")
cursor.close()
conn.close()

