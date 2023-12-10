import sqlite3


class UserDatabase:
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        ''')
        self.conn.commit()

    def add_user(self, name, age):
        self.cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
        self.conn.commit()

    def retrieve_users(self):
        self.cursor.execute("SELECT * FROM users")
        rows = self.cursor.fetchall()
        return rows

    def update_user_age(self, name, new_age):
        self.cursor.execute("UPDATE users SET age = ? WHERE name = ?", (new_age, name))
        self.conn.commit()

    def delete_user(self, id: int):
        self.cursor.execute("DELETE FROM users WHERE id = ?", (id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()


def main():
    database = UserDatabase('rawsql.db')

    while True:
        print("\nChoose an operation:")
        print("1. Add user")
        print("2. Retrieve users")
        print("3. Update user age")
        print("4. Delete user")
        print("5. Exit")

        choice = input("Enter the number corresponding to the operation: ")

        if choice == '1':
            name = input("Enter user name: ")
            age = int(input("Enter user age: "))
            database.add_user(name, age)
            print("User added successfully!")

        elif choice == '2':
            users = database.retrieve_users()
            print("\nUsers in the database:")
            for user in users:
                print(user)

        elif choice == '3':
            name = input("Enter user name to update age: ")
            new_age = int(input("Enter new age: "))
            database.update_user_age(name, new_age)
            print("User age updated successfully!")

        elif choice == '4':
            id = input("Enter id to delete: ")
            database.delete_user(int(id))
            print("User deleted successfully!")

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

    database.close_connection()
    print("Program terminated.")


if __name__ == "__main__":
    main()
