import sqlite3

connection = sqlite3.connect('database.sqlite')
cursor = sqlite3.Cursor(connection)

cursor.execute('DROP TABLE IF EXISTS products')

request = ('CREATE TABLE IF NOT EXISTS products'
           '(id INTEGER PRIMARY KEY AUTOINCREMENT,'
           'name VARCHAR(255),'
           'price INTEGER,'
           'category VARCHAR(255),'
           'characteristics VARCHAR(255),'
           'image_name VARCHAR(255))')
cursor.execute(request)

insert_request = ("INSERT INTO products"
                 "(name, price, category, characteristics, image_name) VALUES (?, ?, ?, ?, ?)")

# Вставка товаров в базу данных
products = [
    ("Процесор Intel Core i9", 15000, "CPU", "", ""),
    ("Відеокарта ASUS GeForce RTX 3060", 25000, "GPU", "", ""),
    ("Материнська плата MSI B450 TOMAHAWK MAX", 6000, "Motherboard", "", ""),
    ("Оперативна пам'ять Corsair Vengeance LPX 16GB", 3500, "RAM", "", ""),
    ("Блок живлення be quiet! Pure Power 11 600W", 4500, "PSU", "", ""),
    ("Жорсткий диск Seagate Barracuda 2TB", 4000, "HDD", "", ""),
    ("SSD Samsung EVO 1TB", 12000, "SSD", "", ""),
    ("Кулер для процесора Noctua NH-D15", 8000, "CPU Cooler", "", ""),
    ("Телевізор Samsung UE43T5300AUXUA", 11000, "TV", "", ""),
    ("Блок Живлення KCAS 600W", 3500, "PSU", "", ""),
    ("Процесор AMD Ryzen 5 1600", 7000, "CPU", "", ""),
    ("Пральна машина автоматична Beko WUE6626XBCW", 15000, "Appliance", "", ""),
    ("Материнська плата Asus TUF Gaming B450-Plus II", 7000, "Motherboard", "", ""),
    ("Відеокарта NVIDIA Geforce RTX 5090", 45000, "GPU", "", ""),
    ("Процесор Ryzen 7 5800X3D", 22000, "CPU", "", ""),
    ("Оперативна пам'ять Kingston Fury DDR4 32GB", 6500, "RAM", "", ""),
    ("Відеокарта Palit GeForce RTX 4070 JetStream", 35000, "GPU", "", "")
]

# Вставка всех данных
cursor.executemany(insert_request, products)

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()


