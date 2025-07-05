import mysql.connector
from faker import Faker

fake = Faker()

conn = mysql.connector.connect(
    host="localhost",
    user="pinaki",
    password="root",  # 🔁 Replace with your real password
    database="pickle"
)

cursor = conn.cursor()

for _ in range(10000):
    name = fake.company() + " SHG"
    phone = fake.phone_number()[:15]
    email = fake.email()
    address = fake.address().replace('\n', ', ')
    pincode = fake.postcode()

    cursor.execute("""
        INSERT INTO SHG (name, phone, email, address, pincode)
        VALUES (%s, %s, %s, %s, %s)
    """, (name, phone, email, address, pincode))

conn.commit()
print("✅ SHG table populated.")
cursor.close()
conn.close()

