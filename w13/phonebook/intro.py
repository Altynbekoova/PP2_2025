import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="admin",
    password="123456ws"
)

def create_table():
    command = """CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(255),
                    last_name VARCHAR(255),
                    phones VARCHAR(20) UNIQUE NOT NULL
                )"""
    with conn.cursor() as cur:
        cur.execute(command)
        conn.commit()

def insert_user_console():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    phone = input("Phone: ")
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO phonebook (first_name, last_name, phones) VALUES (%s, %s, %s);",
            (first_name, last_name, phone)
        )
        conn.commit()

def insert_from_csv(filename):
    with conn.cursor() as cur:
        with open(filename, "r") as file:
            csvreader = csv.reader(file)
            next(csvreader)  # skip header
            for row in csvreader:
                if len(row) == 3:
                    first_name, last_name, phone = row
                    cur.execute(
                        "INSERT INTO phonebook (first_name, last_name, phones) VALUES (%s, %s, %s) ON CONFLICT (phones) DO NOTHING;",
                        (first_name, last_name, phone)
                    )
        conn.commit()

def update_phone(first_name, new_phone):
    with conn.cursor() as cur:
        cur.execute(
            "UPDATE phonebook SET phones = %s WHERE first_name = %s;",
            (new_phone, first_name)
        )
        conn.commit()

def delete_by_phone(phone):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM phonebook WHERE phones = %s;", (phone,))
        conn.commit()

def search_by_name(name):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s;", (f"%{name}%",))
        results = cur.fetchall()
        for row in results:
            print(row)

def show_all():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM phonebook;")
        results = cur.fetchall()
        for row in results:
            print(row)

def menu():
    while True:
        print("\n PHONEBOOK MENU")
        print("1. Add user from console")
        print("2. Upload users from CSV")
        print("3. Update phone number")
        print("4. Delete by phone")
        print("5. Search by name")
        print("6. Show all records")
        print("0. Exit")

        choice = input("Choose action: ")

        if choice == "1":
            insert_user_console()
        elif choice == "2":
            filename = 'phone.csv'
            insert_from_csv(filename)
            print("insert csv file")
        elif choice == "3":
            name = input("Enter first name: ")
            phone = input("Enter new phone number: ")
            update_phone(name, phone)
            print("done!")
        elif choice == "4":
            phone = input("Enter phone number to delete: ")
            delete_by_phone(phone)
            print("delete this number")
        elif choice == "5":
            name = input("Enter name to search: ")
            search_by_name(name)
        elif choice == "6":
            show_all()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid choice!")

# --- RUN ---
create_table()
menu()
conn.close()