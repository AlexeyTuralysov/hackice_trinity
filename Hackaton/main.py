# app.py

from flask import Flask, render_template, redirect, url_for, request
from flask import render_template, flash,redirect, url_for, make_response, request, session

import sqlite3
from datetime import datetime


app = Flask(__name__)

app.secret_key = 'secret' 


@app.route('/')
def index():
        return render_template('index.html')



""" работа с корзиной  """




@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form['search_term']
        results = search_in_database(search_term)
        return render_template('search_results.html', results=results)

    return render_template('search.html')


def add_to_basket(username, product_name):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Получаем текущую корзину пользователя
    cursor.execute("SELECT basket FROM Users WHERE login=?", (username,))
    current_basket = cursor.fetchone()

    if current_basket:
        current_basket = current_basket[0] + ',' + product_name
        # Обновляем корзину пользователя
        cursor.execute("UPDATE Users SET basket=? WHERE login=?", (current_basket, username))
    else:
        # Если пользователя нет в базе, добавляем его с товаром в корзине
        cursor.execute("INSERT INTO Users (login, basket) VALUES (?, ?)", (username, product_name))

    conn.commit()
    conn.close()



@app.route('/add_to_basket', methods=['POST'])
def add_to_basket_route():
    username = session['username'] 

    
    product_name = request.form['product_name']




    add_to_basket(username, product_name)

    return redirect(url_for('search'))
    


def search_in_database(search_term):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + search_term + '%',))
    results = cursor.fetchall()

    conn.close()

    return results


    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE Users SET basket=? WHERE login=?", (updated_basket, user_login))

    conn.commit()
    conn.close()

""" """

""" вывод в корзину"""


@app.route('/basket')
def view_basket():
    # Получите текущего пользователя (замените это на ваш способ получения пользователя)
    username = session['username'] 

    # Получите содержимое корзины пользователя из базы данных
    basket_content = get_basket_content(username)

    # Получите детали продуктов из корзины
    products_in_basket = []
    for item in basket_content:
        product_details = get_product_details(item)
        if product_details:
            products_in_basket.append(product_details)

    return render_template('basket.html', products_in_basket=products_in_basket)


def get_basket_content(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute("SELECT basket FROM Users WHERE login=?", (username,))
    basket_content = cursor.fetchone()

    conn.close()

    return basket_content[0].split(',') if basket_content else []

def get_product_details(product_name):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name, price, image_src FROM products WHERE name=?", (product_name,))
    product_details = cursor.fetchone()

    conn.close()

    return product_details if product_details else None


""""""



@app.route('/upset')
def upse():
    session.pop('username', None)
    return redirect(url_for('index'))



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Подключение к базе данных
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        # Проверка наличия пользователя в базе данных
        cursor.execute("SELECT * FROM Users WHERE login = ? AND password = ?", (username, password))
        user = cursor.fetchone()

        # Закрытие соединения с базой данных
        cursor.close()
        conn.close()

        if user:
            session['username'] = username # Сохранение имени пользователя в сессии
            
            
        
            
               
            
            return render_template('index.html')
        
        else:
            return render_template('login.html')

    return render_template('login.html')




@app.route('/stock', methods=['GET', 'POST'])
def stock():
    
    return render_template('stock.html')






if __name__ == '__main__':
    app.run()
