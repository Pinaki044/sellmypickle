import mysql.connector
from faker import Faker
import random
from datetime import timedelta, datetime

fake = Faker()

conn = mysql.connector.connect(
    host="localhost",
    user="pinaki",
    password="root",  # 🔁 Replace this
    database="pickle"
)

cursor = conn.cursor()

# Get all SHG ids and Type ids
cursor.execute("SELECT SHGid FROM SHG")
shg_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT Tid FROM Type")
type_ids = [row[0] for row in cursor.fetchall()]

# Some sample item names for more realism
sample_items = {
    "Pickles": ["Mango Pickle", "Lemon Pickle", "Chilli Pickle"],
    "Papads": ["Urad Dal Papad", "Rice Papad", "Spicy Masala Papad"],
    "Candles": ["Lavender Scented", "Soy Wax", "Decorative Candle"],
    "Handmade Soaps": ["Neem Soap", "Charcoal Soap", "Aloe Vera Soap"],
    "Spices": ["Garam Masala", "Turmeric Powder", "Cumin Seeds"],
    "Handicrafts": ["Clay Pot", "Bamboo Basket", "Wall Hanging"],
    "Herbal Products": ["Herbal Oil", "Organic Face Pack", "Amla Juice"],
    "Snacks": ["Banana Chips", "Chakli", "Thekua"],
    "Eco-friendly Decor": ["Terracotta Vase", "Coconut Shell Bowl", "Palm Leaf Plate"],
    "Others": ["Jute Bag", "Bead Jewellery", "Organic Dish Wash"]
}

for _ in range(10000):
    type_id = random.choice(type_ids)
    shg_id = random.choice(shg_ids)

    # Get name from type
    cursor.execute("SELECT name FROM Type WHERE Tid = %s", (type_id,))
    type_name = cursor.fetchone()[0]
    item_name = random.choice(sample_items.get(type_name, ["Handmade Item"]))

    price = round(random.uniform(50, 500), 2)
    description = fake.sentence(nb_words=10)
    dom = fake.date_between(start_date='-6M', end_date='today')
    doe = dom + timedelta(days=random.randint(30, 180))

    cursor.execute("""
        INSERT INTO Item (name, price, description, DoM, DoE, Tid, SHGid)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (item_name, price, description, dom, doe, type_id, shg_id))

conn.commit()
print("✅ Item table populated.")
cursor.close()
conn.close()

