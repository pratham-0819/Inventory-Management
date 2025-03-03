import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    port='3306',       
    user="root",    
    password="root123",
    database="inventory"     
)

cursor = conn.cursor()

def add_product(name, category, price, stock):
    cursor.execute("INSERT INTO products (name, category, price, stock) VALUES (%s, %s, %s, %s)",
                   (name, category, price, stock))
    conn.commit()

def update_stock(product_id, new_stock):
    cursor.execute("UPDATE products SET stock = %s WHERE product_id = %s", (new_stock, product_id))
    conn.commit()

def record_sale(product_id, quantity):
    cursor.execute("SELECT stock FROM products WHERE product_id = %s", (product_id,))
    stock = cursor.fetchone()[0]

    if stock >= quantity:
        cursor.execute("INSERT INTO transactions (product_id, transaction_type, quantity) VALUES (%s, 'sale', %s)",
                       (product_id, quantity))
        update_stock(product_id, stock - quantity)
    else:
        print("Not enough stock available.")

def view_inventory():
    cursor.execute("SELECT * FROM products")
    for row in cursor.fetchall():
        print(row)

def view_sales():
    cursor.execute("SELECT * FROM transactions WHERE transaction_type='sale'")
    for row in cursor.fetchall():
        print(row)

