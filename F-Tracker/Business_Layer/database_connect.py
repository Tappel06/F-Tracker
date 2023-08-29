'''This file contains the class for connecting to the programs\' database, or checks wether the
databse exists'''

#=====Imports=====#
import sqlite3
import os

class Database_Connection():

    def __init__(self):
        """This is the constructor, and it connects to the database"""

        # Checks if directory exists.
        self.path_exists()

        # Connects to the database
        self.db = sqlite3.connect("Database/users_db")
        # creates cursor object
        self.cursor = self.db.cursor()
        # Prints that the connection with database is established, and cursor created
        print("Database connection established, and cursor created.")
        # Checks and create tables if needed
        self.tables_exist()
        

    def path_exists(self):
        """Checks wether a path exists, and creates a new one if it does not exist"""

        # Prints that it is checking for directory path existance
        print("Checking if \"Database\" directory exists...")

        # Prints that the path does not exist, then creates it, then prints it is created.
        if os.path.exists("Database") == False:
            print("The directory \"Database\" does not exist, creating directory...")
            os.system("mkdir Database")
            print("Database directory \"Database\" created successfully.")

        # Prints that the directory exists
        else: 
            print("Directory \"Database\" exists.")


    def tables_exist(self):
        """Checks wether the \"users_table\" or \"transactions_table\" tables exist, then creates them 
        if they do not exist."""

        # Checks if user_table exist, then creates it if it does not exist
        try:
            self.cursor.execute("SELECT * FROM users_table;")
        # Prints that the user table does not exist, and then creates it
        except Exception:
            print("The table \"users_table\" does not exist")
            self.create_user_table()

        # Checks if transactions_table exists, then creates it if it does not exist
        try:
            self.cursor.execute("SELECT * FROM transactions_table;")
        # Print that 
        except Exception:
            print("The table \"transactions_table\" does not exist")
            self.create_transactions_table()


    def create_user_table(self):
        """Creates a user table inside \"user_db\", then prints out the process"""

        # Prints creating user table
        print("Creating \"users_table\" table.")

        # Creates user Table
        try:
            self.cursor.execute('''
                                CREATE TABLE users_table(
                                User_id INT(4),
                                Username VARCHAR(20),
                                First_name VARCHAR(20),
                                Last_name VARCHAR(20),
                                Password VARCHAR(50),
                                PRIMARY KEY(User_id))
                                ''')
            self.db.commit()
            # Prints that table created successfully
            print("The table \"users_table\" was created successfully")
        # Prints that the table could not be created
        except Exception:
            self.db.rollback()
            print("The table \"users_table\" was not created successfully")

    
    def create_transactions_table(self):
        """Creates a transactions table inside \"user_db\", then prints out the process"""

        # Creates transactions table
        try:
            self.cursor.execute('''CREATE TABLE transactions_table(
                                Transaction_id INT(6),
                                User_id INT(4),
                                Username VARCHAR(20),
                                PRIMARY KEY(Transaction_id)
                                );''')
            self.db.commit()
            # Prints that table created successfully
            print("The table \"transactions_table\" was created successfully")
        # Prints that the table could not be created
        except Exception:
            self.db.rollback()
            print("The table \"transactions_table\" was not created successfully")
