import sqlite3

# Подключение к базе данных (если базы данных нет, она будет создана)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Создание таблицы Products с полем для изображений
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    login TEXT,
    password TEXT,
    stock TEXT,
    basket TEXT
    

)
''')

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
