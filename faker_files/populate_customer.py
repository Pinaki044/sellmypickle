from faker import Faker
import mysql.connector

fake = Faker()

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="pinaki",
    password="root",
    database="sellmypickle_db"
)

cursor = conn.cursor()

# Insert fake Customer Address and Customer
for _ in range(0,10000):  # You can later change this to 10000
    # CAddress
    landmark = fake.street_name()
    city = fake.city()
    state = fake.state()
    pincode = fake.postcode()

    cursor.execute("""
        INSERT INTO CAddress (landmark, city, state, pincode)
        VALUES (%s, %s, %s, %s)
    """, (landmark, city, state, pincode))

    address_id = cursor.lastrowid  # get inserted address ID

    # Customer
    name = fake.name()
    email = fake.email()
    phone = fake.phone_number()[:20]  # Limit phone to 20 characters max
    feedback = fake.sentence()

    cursor.execute("""
        INSERT INTO Customer (name, email, phone, feedback, address_id)
        VALUES (%s, %s, %s, %s, %s)
    """, (name, email, phone, feedback, address_id))

    if _ % 10 == 0:
        print(f"{_} records inserted...")

# Commit and close
conn.commit()
cursor.close()
conn.close()

print("✅ Done: Data inserted.")

