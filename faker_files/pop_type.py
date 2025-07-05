import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="pinaki",
    password="root",  # 🔁 Replace this
    database="pickle"
)

cursor = conn.cursor()

types = [
    ("Pickles", "Traditional homemade pickles in various flavors."),
    ("Papads", "Crispy Indian snack made from lentils."),
    ("Candles", "Hand-poured scented and unscented candles."),
    ("Handmade Soaps", "Natural, skin-friendly soaps made by SHGs."),
    ("Spices", "Authentic, homemade Indian spices."),
    ("Handicrafts", "Decor items made by local artisans."),
    ("Herbal Products", "Natural wellness and beauty products."),
    ("Snacks", "Tasty local and traditional snacks."),
    ("Eco-friendly Decor", "Sustainable handmade decor items."),
    ("Others", "Other creative handmade products.")
]

for name, description in types:
    cursor.execute("""
        INSERT INTO Type (name, description)
        VALUES (%s, %s)
    """, (name, description))

conn.commit()
print("✅ Type table populated.")
cursor.close()
conn.close()

