import sqlite3

# Функция для создания таблицы
def create_table():
    conn = sqlite3.connect('inventory.db')  # Подключение к базе данных (или создание, если её нет)
    cursor = conn.cursor()

    # Создание таблицы с полями: id, название, картинка и количество
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            image TEXT,
            quantity INTEGER
        )
    ''')

    conn.commit()
    conn.close()

# Функция для добавления товара в базу данных
def add_product(name, image, quantity):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    # Добавление товара с указанными параметрами
    cursor.execute('''
        INSERT INTO inventory (name, image, quantity)
        VALUES (?, ?, ?)
    ''', (name, image, quantity))

    conn.commit()
    conn.close()

# Пример использования
if __name__ == "__main__":
    create_table()  # Создание таблицы

    # Добавление товаров
    add_product('Товар 1', 'image1.jpg', 10)
    add_product('Товар 2', 'image2.jpg', 5)
    add_product('Товар 3', 'image3.jpg', 20)
