import sqlite3


def connect_db():
    return sqlite3.connect("customers.db")


def view_customers():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()

    print("\n--- Customers List ---")
    for row in rows:
        print(row)

    conn.close()


def add_customer():
    name = input("Enter name: ")
    while True:
        try:
            age = int(input("Enter age: "))
            if age < 0 or age > 150:
                raise ValueError("Age out of realistic range")
            break
        except ValueError as e:
            print("Invalid age. Please enter a whole number between 1-150 range")

    country = input("Enter country: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO customers (name, age, country) VALUES (?, ?, ?)", (name,
                                                                        age, country)
    )

    conn.commit()
    conn.close()

    print("Customer added successfully!")


def delete_customer():
    customer_id = input("Enter customer ID to delete: ")
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM customers WHERE id =  ?", (customer_id,)
    )

    conn.commit()
    conn.close()
    print("Customer deleted successfully! ")


def menu():
    while True:
        print("\n=== Customer Management System ===")
        print("1. View customers")
        print("2. Add customer")
        print("3. Delete customer")
        print("4. Exit")

        choice = input("Select option: ")

        if choice == "1":
            view_customers()
        elif choice == "2":
            add_customer()
        elif choice == "3":
            delete_customer()
        elif choice == "4":
            print("Exiting..........")
            break
        else:
            print("Invalid choice!!")


menu()
