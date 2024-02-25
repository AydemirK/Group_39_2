import sqlite3


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as err:
        print(f"Error {err}")
    return conn


def create_table(conn, create_table_sql):
    try:
        cur = conn.cursor()
        cur.execute(create_table_sql)
    except sqlite3.Error as err:
        print(f"Error {err}")


def insert_data(conn, product):
    sql = '''INSERT INTO products (product_title, price, quantity) VALUES (?,?,?)'''
    try:
        cur = conn.cursor()
        cur.execute(sql, product)
        conn.commit()
    except sqlite3.Error as err:
        print(f"Error {err}")


def update_quant(conn, product):
    sql = ''' UPDATE products SET quantity = ? WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as err:
        print(f"Error {err}")


def update_price(conn, product):
    sql = ''' UPDATE products SET price = ? WHERE id = ? '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as err:
        print(f"Error {err}")


def del_comm(conn, id):
    sql = ''' DELETE FROM products WHERE id=? '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as err:
        print(f"Error {err}")


def all_products(conn):
    sql = ''' SELECT * FROM products '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        list_products = cursor.fetchall()
        for product in list_products:
            print(product)
    except sqlite3.Error as err:
        print(f"Error {err}")


def all_products_less(conn, low):
    sql = ''' SELECT * FROM products WHERE price <= ? AND quantity >= ? '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, low)
        list_products = cursor.fetchall()
        for product in list_products:
            print(product)
    except sqlite3.Error as err:
        print(f"Error {err}")


def title_search(conn, name):
    sql = ''' SELECT * FROM products WHERE product_title  LIKE '%'||?||'%' '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (name,))
        list_products = cursor.fetchall()
        for product in list_products:
            print(product)
    except sqlite3.Error as err:
        print(f"Error {err}")


products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL, 
    price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''

connection = create_connection('HW.db')
if connection:
    print("Connection established")
    # create_table(connection, products_table)
    # insert_data(connection, ('Carrots', 50.00, 150))
    # insert_data(connection, ('Onions', 22.00, 202))
    # insert_data(connection, ('Pepper', 303.00, 19))
    # insert_data(connection, ('Tomato', 186.00, 63))
    # insert_data(connection, ('Cucumber', 235.00, 84))
    # insert_data(connection, ('Cabbage', 75.00, 93))
    # insert_data(connection, ('Eggplant', 226.00, 35))
    # insert_data(connection, ('Garlic', 280.00, 40))
    # insert_data(connection, ('meats', 620.00, 1))
    # insert_data(connection, ('Sausage', 493.00, 111))
    # insert_data(connection, ('Dutch cheese', 763.00, 100))
    # insert_data(connection, ('Baby soap', 43.00, 55))
    # insert_data(connection, ('Sour cream', 72.00, 460))
    # insert_data(connection, ('Liquid soap', 80.00, 100))
    # insert_data(connection, ('Potatoes', 54.00, 100))
    # insert_data(connection, ('Potatoes', 54.00, 100))
    # update_quant(connection, (61, 15))
    # update_price(connection, (32.00, 15))
    # del_comm(connection, 16)
    # all_products(connection)
    all_products_less(connection, (100, 5))
    # title_search(connection, 'soap')

    connection.close()
