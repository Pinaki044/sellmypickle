import mysql.connector
from faker import Faker
import random

fake = Faker()

conn = mysql.connector.connect(
    host="localhost",
    user="pinaki",
    password="root",  # 🔁 Replace with your real MySQL password
    database="pickle"
)

cursor = conn.cursor()

# Get existing address IDs
cursor.execute("SELECT CAddid FROM CAddress")
address_ids = [row[0] for row in cursor.fetchall()]

for _ in range(10000):
    name = fake.name()
    email = fake.email()
    phone = fake.phone_number()[:15]
    feedback = fake.text(max_nb_chars=100)
    address_id = random.choice(address_ids)

    cursor.execute("""
        INSERT INTO Customer (name, email, phone, feedback, address_id)
        VALUES (%s, %s, %s, %s, %s)
    """, (name, email, phone, feedback, address_id))

conn.commit()
print("✅ Customer table populated.")
cursor.close()
conn.close()

