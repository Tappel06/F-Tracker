'''This file contains the class for connecting to the programs\' database, or checks wether the
databse exists'''

#=====Imports=====#
import sqlite3
import os

class Database_Connection():

    def __init__(self):
        """This is the constructor"""

        # Checks if directory exists.
        self.path_exists()
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


    #====Create Tables section====#
    '''This section contains all the methods that create tables'''
    
    def tables_exist(self):
        """Checks wether the \"users_table\" or \"transactions_table\" tables exist, then creates them 
        if they do not exist."""
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            # Checks if user_table exist, then creates it if it does not exist
            try:
                cursor.execute("SELECT * FROM users_table;")
            # Prints that the user table does not exist, and then creates it
            except Exception:
                print("The table \"users_table\" does not exist")
                self.create_user_table()

            # Checks if transactions_table exists, then creates it if it does not exist
            try:
                cursor.execute("SELECT * FROM transactions_table;")
            # Print that 
            except Exception:
                print("The table \"transactions_table\" does not exist")
                self.create_transactions_table()

            # Checks if "income_expense_category_table" exists, the creates it if it does not exist
            try:
                cursor.execute("SELECT * FROM income_expense_category_table;")
            # Print that 
            except Exception:
                print("The table \"income_expense_category_table\" does not exist")
                self.create_income_expense_category_table()


    def create_user_table(self):
        """Creates a user table inside \"user_db\", then prints out the process"""

        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            # Prints creating user table
            print("Creating \"users_table\" table.")

            # Creates user Table
            try:
                cursor.execute('''
                                CREATE TABLE users_table(
                                User_id INT(4),
                                Username VARCHAR(20),
                                First_name VARCHAR(20),
                                Last_name VARCHAR(20),
                                Password VARCHAR(50),
                                PRIMARY KEY(User_id))
                                ''')
                db.commit()
                # Prints that table created successfully
                print("The table \"users_table\" was created successfully")
            # Prints that the table could not be created
            except Exception:
                db.rollback()
                print("The table \"users_table\" was not created successfully")

    
    def create_transactions_table(self):
        """Creates a transactions table inside \"user_db\", then prints out the process"""

        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            # Creates transactions table
            try:
                cursor.execute('''CREATE TABLE transactions_table(
                                Transaction_id INT(6),
                                User_id INT(4),
                                yyyy_mm_dd DATE,
                                Income_or_expense VARCHAR(7),
                                Category VARCHAR(20),
                                Total DECIMAL(20,2),
                                PRIMARY KEY(Transaction_id));
                                ''')
                db.commit()
                # Prints that table created successfully
                print("The table \"transactions_table\" was created successfully")
            # Prints that the table could not be created
            except Exception:
                db.rollback()
                print("The table \"transactions_table\" was not created successfully")


    def create_income_expense_category_table(self):
        """Creates a category table for income and expenses inside \"user_db\", then prints the process"""

        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            # Creates income_expense_category_table
            try:
                # Executes query
                cursor.execute('''CREATE TABLE income_expense_category_table(
                                Category_id INT(6),
                                User_id INT(6),
                                Income_or_expense VARCHAR(7),
                                Category_Title VARCHAR(20),
                                PRIMARY KEY(Category_id));
                                ''')
                db.commit()
                # Prints that table created successfully
                print("The table \"income_expense_category_table\" was created successfully")
            except Exception:
                db.rollback()
                print("The table \"income_expense_category_table\" was not created successfully")


    #=====Users table section=====#
    '''Contains all the methods related to the "users_table'''

    def user_authenticater(self, username, password):
        """Checks wether a user details match
        
            :param string username: username
            :param string password: password

            :returns: True if user details correct, False if incorrect
            :rtype: boolean
        """

        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Execute query
                cursor.execute('''SELECT * FROM users_table
                                WHERE Username = ? AND Password = ?;
                                ''', (username, password,))
                # Gets a list of users with same details
                userlist = cursor.fetchall()
                
                # Checks if the userlist is equal to one
                if len(userlist) == 1:
                    # Returns True
                    return True
                else:
                    return False
            
            except Exception:
                print("QUERY ERROR")


    def assign_new_user_id(self):
        """Automaticaly assign a new id to a new user, returns a number
        
            :rtype int
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            # starts id variable on "1"
            id = 1
            
            # continious loop till id found
            while True:
                try:
                    # Executes query
                    cursor.execute("""SELECT * FROM users_table
                                    WHERE User_id = ?""", (id,))
                    # Get record list
                    user_list = cursor.fetchall()

                    # Checks if user_list length is 0
                    if len(user_list) == 0:
                        break
                    else:
                        id += 1

                except Exception:
                    print("Error at \"assign_new_user_id\" in database_connect")

            # returns id
            return id
    

    def add_user_record(self, username, first_name, last_name, password):
        """Creates a new user record, returns True if successfully added
        
            :param string username: Username
            :param string first_name: Users first name
            :param string last_name: Users last name
            :param string password: users password
        
            :returns: True or False if user registered successfully
        
            :rtype: boolean
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            # Assigns an id for the user
            assigned_id = self.assign_new_user_id()

            try: 
                # Execute query
                cursor.execute('''INSERT INTO users_table
                                    VALUES (?, ?, ?, ?, ?)''', 
                                    (assigned_id, username, first_name,
                                    last_name, password))
                db.commit()
                print("User added to the database")
                return True
            except Exception:
                db.rollback()
                print("User not successfully added to the database")
                return False
        

    def get_user_record(self, username, password):
        """Gets the user's record, and return it
        
            :param string username: The users' usersname
            :param string password: The users' password
            
            :returns: list of the user's record details
            
            :rtypre: list
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            try: 
                # Executes query
                cursor.execute('''SELECT * FROM users_table
                                WHERE Username = ? AND Password = ?''',
                                (username, password,))
                # Stores record into a list
                user_list = cursor.fetchall()
                return user_list
            except Exception:
                print("Error at \"get_user_record\"")


    def get_all_users(self):
        """Returns a list of all the users in the users_table
        
            :returns: a list of all the users in the users_table

            :rtype: list
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''SELECT * FROM users_table;''')
                # Stores the users into a list
                user_list = cursor.fetchall()
                # Returns the user list
                return user_list
            except Exception:
                print("User list could not be fetched. error at \"get_all_users\"")


    def username_exists(self, username):
        """Checks wether a specific username exists
        
            :param string username: The username of the user

            :returns: True if the username exists

            :rtype: bool
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            # default boolean value
            username_exist = False

            try:
                # Executes query
                cursor.execute('''SELECT * FROM users_table
                                WHERE Username = ?''', (username,))
                # Stores user/s into a list
                user_list = cursor.fetchall()
                # Checks if user_list is equal to zero
                if len(user_list) > 0:
                    username_exist = True

            except Exception:
                print("Error at \"username_exist\" in \"database_connect\"")

            # Returns boolean value
            return username_exist
    

    #=====Transaction Table Section (Expenses)=====#
    '''Contains all the methods conserning the Expenses of transactions_table'''

    def get_all_expenses_by_user_id(self, user_id):
        """Gets all expenses by user_id, returns a list
        
            :param int user_id: the user's ID

            :returns: list of expenses by user

            :rtype: list
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''SELECT * FROM transactions_table
                               WHERE User_id = ? AND Income_or_expense = "Expense";''', (user_id,))
                # Gets expense list
                expense_list = cursor.fetchall()
                # Returns expense_list
                return expense_list
            
            except Exception:
                print("Could not retrieve expense records by user id")


    def delete_expense_transaction_by_id(self, transaction_id):
        """Deletes expense record by transaction id
        
            :param int transaction_id: gets the transaction id of record to be deleted
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''DELETE FROM transactions_table
                               WHERE Transaction_id = ?;''', (transaction_id,))
                db.commit()
            except Exception:
                db.rollback()
                print("Could not delete expense transaction by id")


    def add_expense_transaction_record(self, user_id, date, category, amount):
        """Creates and adds a new transaction record in transactions_table
        
            :param int user_id: receives the user's id
            :param string date: receives the date of the transaction
            :param string category: receives the expense category
            :param float amoun: receives the amount of the expense
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                cursor.execute('''INSERT INTO transactions_table
                                VALUES (?, ?, ?, "Expense", ?, ?);''',
                                (self.auto_assign_transaction_id(), user_id, date, category, amount))
                db.commit()
            
            except Exception:
                db.rollback
                print("Expense transaction record could not be created in transactions_table")


    def auto_assign_transaction_id(self):
        """Automaticaly assigns an id if it does not exist in the \"transactions_table\"
        
            :returns: available id number

            :rtype: int
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            # ID integer value starts at 1
            id = 1

            # While loop till id does not exist in table
            while True:
                try:
                    # Executes query
                    cursor.execute("""SELECT * FROM transactions_table
                                    WHERE Transaction_id = ?;""", (id,))
                    # Gets list of categories
                    transaction_list = cursor.fetchall()
                    # Checks if category equals 0, then breaks loop if does exist
                    if len(transaction_list) == 0:
                        # returns id
                        return id
                    
                    else:
                        id += 1

                except Exception:
                    print("Could not generate a transaction id")
                    break

    #=====Category table Section=====#
    '''Contains all the methods conserning the "income_expense_category_table"'''

    def create_new_expense_category(self, user_id, category_title):
        """Creates a new expense category record in the \"income_expense_category_table\"
        
            :param int user_id: The user's id to who the category is related to
            :param string category_title: The new name of the expense category
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''INSERT INTO income_expense_category_table
                                    VALUES (?, ?, "Expense", ?);
                                    ''', (self.auto_assign_category_id(), user_id, category_title))
                db.commit()
                print("new expense category added")
            except Exception:
                db.rollback()
                print("new expense category could not be added")


    def delete_expense_category(self, category_id):
        """Deletes a expense_category from the \"income_expense_category_table\"
        
            :param int category_id: The id of the category to be deleted
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''DELETE FROM income_expense_category_table
                                    WHERE Category_id = ?;
                                    ''', (category_id,))
                db.commit()
                print("Expense category removed")
            except Exception:
                db.rollback()
                print("Expense category could not be removed")


    def auto_assign_category_id(self):
        """Automaticaly assigns an id if it does not exist in the \"income_expense_category_table\"
        
            :returns: available id number

            :rtype: int
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            # ID integer value starts at 1
            id = 1

            # While loop till id does not exist in table
            while True:
                try:
                    # Executes query
                    cursor.execute(f"""SELECT * FROM income_expense_category_table
                                        WHERE Category_id = ?;""", (id,))
                    # Gets list of categories
                    category_list = cursor.fetchall()
                    # Checks if category equals 0, then breaks loop if does exist
                    if len(category_list) == 0:
                        # returns id
                        return id
                    else:
                        id += 1
                except Exception:
                    print("Could not generate a category id")
                    break

        
    def get_all_expense_categories(self, user_id):
        """returns all the records where categories are expenses

        :param int user_id: contains the user id with what the expenses are related to

        :returns: list of expense records related to the user id

        :rtype: list
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''SELECT * FROM income_expense_category_table
                                    WHERE User_id = ? AND 
                                    Income_or_Expense = "Expense";''',
                                    (user_id,))
                # Stores the categorie records in alist
                expense_category_list = cursor.fetchall()
                return expense_category_list
            except Exception:
                print("Could not retrieve expense_category_list")