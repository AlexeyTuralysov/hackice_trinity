import sqlite3

# Создаем соединение с базой данных (если базы данных не существует, она будет создана)
conn = sqlite3.connect('database.db')

# Создаем курсор для выполнения SQL-запросов
cursor = conn.cursor()

# Удаляем существующую таблицу, если она уже существует
cursor.execute('DROP TABLE IF EXISTS products')

# Создаем таблицу products
cursor.execute('''
    CREATE TABLE products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        image_src TEXT
    )
''')

# Заполняем таблицу данными
products_data = [
    ('орео', 19.99, '\static\image\OREO-Chocolate-Sandwich-Cookies-13-29-oz_f4b2b9ae-a9d4-4c9e-8978-d5dbf8d866d1.2e7c923458a90653316559e94272a857.webp'),
    ('молоко', 80.99, '\static\image\milk.jpg')
    # Добавьте другие продукты по необходимости
]

cursor.executemany('INSERT INTO products (name, price, image_src) VALUES (?, ?, ?)', products_data)

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()
