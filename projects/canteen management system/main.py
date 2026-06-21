import mysql.connector
import matplotlib.pyplot as plt

# ---------------- DATABASE CONNECTION ----------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="66511",
    database="canteen_db",
    port=3307
)

cur = conn.cursor()

# ---------------- TABLES ----------------
cur.execute("""
CREATE TABLE IF NOT EXISTS menu(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price FLOAT,
    stock INT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS customers(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS orders(
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    item_name VARCHAR(100),
    quantity INT,
    total FLOAT
)
""")

conn.commit()

# ---------------- MENU ----------------
def add_item():
    name = input("Item Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))

    cur.execute(
        "INSERT INTO menu(name, price, stock) VALUES(%s,%s,%s)",
        (name, price, stock)
    )
    conn.commit()
    print("✅ Item Added")


def view_menu():
    cur.execute("SELECT * FROM menu")
    for row in cur.fetchall():
        print(row)


# ---------------- CUSTOMER ----------------
def add_customer():
    name = input("Customer Name: ")

    cur.execute(
        "INSERT INTO customers(name) VALUES(%s)",
        (name,)
    )
    conn.commit()
    print("✅ Customer Added")


def view_customers():
    cur.execute("SELECT * FROM customers")
    for row in cur.fetchall():
        print(row)


# ---------------- ORDER ----------------
def place_order():
    view_customers()
    cid = int(input("Enter Customer ID: "))

    view_menu()
    item_id = int(input("Enter Item ID: "))
    qty = int(input("Enter Quantity: "))

    cur.execute(
        "SELECT name, price, stock FROM menu WHERE id=%s",
        (item_id,)
    )
    item = cur.fetchone()

    if item:
        name, price, stock = item

        if stock >= qty:
            total = price * qty

            cur.execute(
                "INSERT INTO orders(customer_id,item_name,quantity,total) VALUES(%s,%s,%s,%s)",
                (cid, name, qty, total)
            )

            cur.execute(
                "UPDATE menu SET stock = stock - %s WHERE id=%s",
                (qty, item_id)
            )

            conn.commit()
            print(f"✅ Order Placed! Total = ₹{total}")

        else:
            print("❌ Not enough stock")
    else:
        print("❌ Item not found")


def view_orders():
    cur.execute("""
    SELECT o.id, c.name, o.item_name, o.quantity, o.total
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
    """)
    for row in cur.fetchall():
        print(row)


# ---------------- REPORTS ----------------
def total_sales():
    cur.execute("SELECT SUM(total) FROM orders")
    result = cur.fetchone()
    print("💰 Total Sales:", result[0] if result[0] else 0)


def low_stock():
    cur.execute("SELECT * FROM menu WHERE stock < 5")
    print("⚠️ Low Stock Items:")
    for row in cur.fetchall():
        print(row)


# ---------------- 📈 SALES CHART ----------------
def sales_chart():
    cur.execute("SELECT id, total FROM orders")
    data = cur.fetchall()

    if not data:
        print("❌ No sales data")
        return

    order_ids = []
    totals = []

    for row in data:
        order_ids.append(row[0])
        totals.append(row[1])

    plt.plot(order_ids, totals, marker='o')
    plt.title("Sales Trend")
    plt.xlabel("Order ID")
    plt.ylabel("Total Amount")
    plt.grid()

    plt.show()


# ---------------- MAIN MENU ----------------
while True:
    print("\n===== CANTEEN SYSTEM =====")
    print("1. Add Menu Item")
    print("2. View Menu")
    print("3. Add Customer")
    print("4. View Customers")
    print("5. Place Order")
    print("6. View Orders")
    print("7. Total Sales")
    print("8. Low Stock Alert")
    print("9. Sales Chart")
    print("10. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_item()

    elif choice == "2":
        view_menu()

    elif choice == "3":
        add_customer()

    elif choice == "4":
        view_customers()

    elif choice == "5":
        place_order()

    elif choice == "6":
        view_orders()

    elif choice == "7":
        total_sales()

    elif choice == "8":
        low_stock()

    elif choice == "9":
        sales_chart()

    elif choice == "10":
        print("👋 Exiting...")
        break

    else:
        print("❌ Invalid Choice")