import sqlite3
from sqlite3 import Cursor, Error


def connect_db(db):
    conn = None
    try:
        conn = sqlite3.connect(db)
    except Error as e:
        print(e)

    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)


def create_product(conn, product):
    try:
        sql = """INSERT INTO products(product_tittle, price, quantity)
        VALUES (?, ?, ?)
        """
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)


def add_product():
    create_product(connect, ('motherboard', 40, 7))
    create_product(connect, ('cpu', 70, 10))
    create_product(connect, ('monitor', 120, 15))
    create_product(connect, ('memory', 25.5, 40))
    create_product(connect, ('hdd', 15, 37))
    create_product(connect, ('ssd disk', 30, 40))
    create_product(connect, ('power unit', 35, 15))
    create_product(connect, ('mouse', 5, 30))
    create_product(connect, ('keyboard', 12, 23))
    create_product(connect, ('frame', 15, 20))
    create_product(connect, ('DVD-ROM', 5, 15))
    create_product(connect, ('mouse pad', 15, 40))
    create_product(connect, ('cpu cooler', 25, 30))
    create_product(connect, ('battery for motherboard', 1, 30))
    create_product(connect, ('thermal paste', 10, 50))


def change_quantity(conn, student):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, student)
        conn.commit()
    except Error as e:
        print(e)


def change_price(conn, student):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, student)
        conn.commit()
    except Error as e:
        print(e)


def delete_product(conn, id):
    try:
        sql = """DELETE FROM products WHERE id = ? """
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except Error as e:
        print(e)


def print_product(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for i in rows:
            print(i)
    except Error as e:
        print(e)


def select_product(conn, student):
    try:
        sql = """SELECT * FROM products WHERE price <= ? and quantity > ?"""
        cursor = conn.cursor()
        cursor.execute(sql, student)
        rows = cursor.fetchall()
        for i in rows:
            print(i)
    except Error as e:
        print(e)


def search_in_db(conn, word):
    try:
        sql = """ SELECT * FROM products WHERE product_tittle LIKE ? """
        cursor = conn.cursor()
        cursor.execute(sql, (word,))
        rows = cursor.fetchall()
        for i in rows:
            print(i)
    except Error as e:
        print(e)


connect = connect_db('''hw.db''')
create_product_table = """CREATE TABLE products(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    product_tittle VARCHAR(200) NOT NULL,
    price DOUBLE (10,2) NOT NULL DEFAULT 0.0,
    quantity INTEGER(5) NOT NULL DEFAULT 0
)"""
if connect is not None:
    print('Connected successfully!')
# create_table(connect, create_product_table)
# add_product()
# change_quantity(connect, (40, 5))
# change_price(connect, (80, 2))
# delete_product(connect, 15)
# print_product(connect)
# select_product(connect, (50, 10))
# search_in_db(connect, "cpu%")