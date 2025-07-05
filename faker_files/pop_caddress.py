import mysql.connector
from faker import Faker

fake = Faker()

conn = mysql.connector.connect(
    host="localhost",
    user="pinaki",
    password="root",  # 🔁 Replace with your actual password
    database="pickle"
)

cursor = conn.cursor()

for _ in range(10000):
    landmark = fake.street_name()
    city = fake.city()
    state = fake.state()
    pincode = fake.postcode()

    cursor.execute("""
        INSERT INTO CAddress (landmark, city, state, pincode)
        VALUES (%s, %s, %s, %s)
    """, (landmark, city, state, pincode))

conn.commit()
print("✅ CAddress table populated.")
cursor.close()
conn.close()

