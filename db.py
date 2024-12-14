import sqlite3


connection = sqlite3.connect('database.sqlite')
cursor = sqlite3.Cursor(connection)

cursor.execute('DROP TABLE IF EXISTS products')
cursor.execute('DROP TABLE IF EEXISTS shopping_cart')

request = ('CREATE TABLE IF EXISTS products'
           '(id INTEGRER PRIMARY KEY AUTOINCREMENT,'
           'name VARCHAR(255),'
           'price INTEGR,'
           'depth INTEGER'
           'image_name VARCHAR(255))'
cursor.excute(request)

