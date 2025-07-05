from faker import Faker
import random
import mysql.connector

fake = Faker()

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="pinaki",
    password="root",  # 🔁 your MySQL password
    database="sellmypickle_db"
)

cursor = conn.cursor()

# Optional: get existing Item IDs (assuming you already have items)
cursor.execute("SELECT Itemid FROM Item")
item_ids = [row[0] for row in cursor.fetchall()]
if not item_ids:
    print("❌ No items found. Please populate Items table first.")
    exit()

# Insert 100 SHG entries
for _ in range(100):
    name = fake.company()
    address = fake.address().replace("\n", ", ")
    phone = fake.phone_number()[:20]
    email = fake.email()
    pincode = fake.postcode()

    item_id = random.choice(item_ids)

    cursor.execute("""
        INSERT INTO SHG (name, address, phone, email, Pincode, Itemid)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (name, address, phone, email, pincode, item_id))

    if _ % 10 == 0:
        print(f"{_} SHG records inserted...")

conn.commit()
cursor.close()
conn.close()
print("✅ Done: SHG data inserted.")

