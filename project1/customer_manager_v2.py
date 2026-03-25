import sqlite3
# database connection
# def is a user defined function


def connect_db():
    """
    creates and returns a connection to the SQLite database
    """
    return sqlite3.connect("customers.db")

# function to view the customers


def view_customers():
    """
    fetches and displays all customers in a formatted table
    """
    conn = connect_db()
    cursor = conn.cursor()

    # SQL query to get all records
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()

    # display header
    print("\n --- Customers list --- ")
    print("ID | Name                      | Age   | Country")
    print("_" * 40)

    # loop through the rows and print nicely formatted output
    for row in rows:
        print(f"{row[0]} | {row[1]: <10} | {row[2]} | {row[3]}")
    conn.close()

# for adding customer


def add_customer():
    """
    Takes user input and inserts a new customer into the database
    """
    try:
        # get user input
        name = input("Enter name: ")
        age = int(input("Enter age: "))  # this will be converted to int
        country = input("Enter country; ")

        conn = connect_db()
        cursor = conn.cursor()

        # insert data into the table
        cursor.execute(""
                       "INSERT INTO customers (name, age, country) VALUES (?, ?, ?), (name, age, country)"
                       )
        conn.commit()
        conn.close()
        print("customer added successfully!")
    except ValueError:
        # it handles errors case where age is not a valid number
        print("Age must be a number.")

# for deleting customer


def delete_customer():
    """
    Deletes a customer based on ID"""
    try:
        # Get id from user
        customer_id = int(input("Enter customer id to delete: "))
        conn = connect_db()
        cursor = conn.cursor()

        # delete query
        cursor.execute(
            "DELETE FROM customers WHERE id = ?", (customer_id,)
        )
        conn.commit()
        conn.close()
        print("Customer deleted successfully!")

    except ValueError:
        print("Please enter a valid customer id.")

# search customer


def search_customer():
    """
    Searches customer by name using partial tracking
    """
    name = input("Enter name to search: ")
    conn = connect_db()
    cursor = conn.cursor()
    # LIKE allows partial matching using %
    cursor.execute(
        "SELECT * FROM customers WHERE name LIKE ?", ('%' + name + '%',)
    )
    rows = cursor.fetchall()
    print("\n --- Search result --- ")
    if rows:
        print("ID | Name                      | Age   | Country")
        print("_" * 40)
        for row in rows:
            print(f"{row[0]} | {row[1]:<10} | {row[2]} | {row[3]}")
    else:
        print("No customer found.")

    conn.close()
# update customer


def update_customer():
    """
    Updates an existing customer's details."""
    try:
        # Get id and new values
        customer_id = input("Enter customer id to update: ")
        new_name = input("Enter new name: ")
        new_age = int(input("Enter new age: "))
        new_country = input("Enter new country: ")

        conn = connect_db()
        cursor = conn.cursor()
        # update query
        cursor.execute(
            "UPDATE customers SET name=?, age=?, country=?", (
                new_name, new_age, new_country)
        )
        conn.commit()
        conn.close()
    except ValueError:
        print("Invalid input, age and id must be numbers")

# menu system main loop


def menu():
    """
    Displays menu and handles user interaction.
    Runs continuously until user exits."""

    while True:
        print("\n --- Customer Management System --- ")
        print("1. View Customers")
        print("2. Add Customer")
        print("3. Delete Customer")
        print("4. Search Customer")
        print("5. Update Customer")
        print("6. Exit")

        # take user input
        choice = input("select option: ")
        # match user choice with function

        if choice == "1":
            view_customers()
        elif choice == "2":
            add_customer()
        elif choice == "3":
            delete_customer()
        elif choice == "4":
            search_customer()
        elif choice == "5":
            update_customer()

        elif choice == "6":
            print("exiting...........")
            break
        else:
            print("Invalid choice.")


# program entry point, this starts the program4
menu()
