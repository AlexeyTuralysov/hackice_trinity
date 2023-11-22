import sqlite3

# Подключение к базе данных (если базы данных нет, она будет создана)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Создание таблицы Products с полем для изображений
query = """INSERT INTO Users (login, password, stock, basket) VALUES ('admin', 'admin', '', '');"""



count = cursor.execute(query)
# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
