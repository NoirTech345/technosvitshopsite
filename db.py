import sqlite3


connection = sqlite3.connect('database.sqlite')
cursor = sqlite3.Cursor(connection)

cursor.execute('DROP TABLE IF EXISTS products')

request = ('CREATE TABLE IF NOT EXISTS products'
           '(id INTEGRER PRIMARY KEY AUTOINCREMENT,'
           'name VARCHAR(255),'
           'price INTEGR,'
           'category VARCHAR(255),'
           'characteristics VARCHAR(255)'
           'image_name VARCHAR(255))')
cursor.execute(request)

insert_request = ("INSERT INTO products"
                 "(name, price, category, characteristics, image_name) VALUES (?, ?, ?, ?, ?)")

cursor.execute(insert_request, ("Процесор Intel Core i9", 15000, "CPU", ""))

