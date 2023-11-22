import sqlite3

# Подключение к базе данных (если базы данных нет, она будет создана)
conn = sqlite3.connect('products.db')
cursor = conn.cursor()

# Создание таблицы Products с полем для изображений
cursor.execute('''
CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    expiry_date_from DATE,
    expiry_date_to DATE,
    image BLOB
)
''')

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
