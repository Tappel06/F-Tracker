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

            # Checks if budget_table exists
            try:
                cursor.execute("SELECT * FROM budget_table;")
            # Print that 
            except Exception:
                print("The table \"budget_table\" does not exist")
                self.create_budget_table()

            # Checks if "financial_goal_category_table" exists, the creates it if it does not exist
            try:
                cursor.execute("SELECT * FROM financial_goals_table;")
            # Print that 
            except Exception:
                print("The table \"financial_goals_category_table\" does not exist")
                self.create_financial_goals_table()


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


    def create_budget_table(self):
        """Creates a budget table inside \"user_db\", then prints out the process"""

        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            # Creates transactions table
            try:
                cursor.execute('''CREATE TABLE budget_table(
                                Budget_id INT(6),
                                User_id INT(4),
                                Category VARCHAR(20),
                                Total DECIMAL(20,2),
                                PRIMARY KEY(Budget_id));
                                ''')
                db.commit()
                # Prints that table created successfully
                print("The table \"budget_table\" was created successfully")
            # Prints that the table could not be created
            except Exception:
                db.rollback()
                print("The table \"budget_table\" was not created successfully")


    def create_financial_goals_table(self):
        """Creates a financial goals table inside \"user_db\", then prints out the process"""

        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            # Creates transactions table
            try:
                cursor.execute('''CREATE TABLE financial_goals_table(
                                Goal_id INT(6),
                                User_id INT(4),
                                Category VARCHAR(20),
                                Total DECIMAL(20,2),
                                PRIMARY KEY(Goal_id));
                                ''')
                db.commit()
                # Prints that table created successfully
                print("The table \"financial_goals_table\" was created successfully")
            # Prints that the table could not be created
            except Exception:
                db.rollback()
                print("The table \"financial_goals_table\" was not created successfully")


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
                               WHERE User_id = ? AND Income_or_expense = "Expense"
                               ORDER BY yyyy_mm_dd;''', (user_id,))
                # Gets expense list
                expense_list = cursor.fetchall()
                # Returns expense_list
                return expense_list
            
            except Exception:
                print("Could not retrieve expense records by user id")


    def get_all_expenses_by_user_id_and_category(self, user_id, category):
        """Gets all expenses by user_id and category, returns a list
        
            :param int user_id: the user's ID
            :param string category: the category by which list must be fetched

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
                               WHERE User_id = ? 
                               AND Income_or_expense = "Expense"
                               AND Category LIKE ?
                               ORDER BY yyyy_mm_dd;''', (user_id, f"%{category}%",))
                # Gets expense list
                expense_list = cursor.fetchall()
                # Returns expense_list
                return expense_list
            
            except Exception:
                print("Could not retrieve expense records by user id and category")


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


    #=====Transaction Table Section (Income)=====#
    '''Contains all the methods conserning the Income of transactions_table'''   

    def get_all_income_by_user_id(self, user_id):
        """Gets all income by user_id, returns a list
        
            :param int user_id: the user's ID

            :returns: list of income by user

            :rtype: list
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''SELECT * FROM transactions_table
                               WHERE User_id = ? AND Income_or_expense = "Income"
                               ORDER BY yyyy_mm_dd;''', (user_id,))
                # Gets income list
                income_list = cursor.fetchall()
                # Returns income_list
                return income_list
            
            except Exception:
                print("Could not retrieve income records by user id")


    def get_all_income_by_user_id_and_category(self, user_id, category):
        """Gets all income by user_id and category, returns a list
        
            :param int user_id: the user's ID
            :param string category: the category by which list must be fetched

            :returns: list of income by user

            :rtype: list
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''SELECT * FROM transactions_table
                               WHERE User_id = ? 
                               AND Income_or_expense = "Income"
                               AND Category LIKE ?
                               ORDER BY yyyy_mm_dd;''', (user_id, f"%{category}%",))
                # Gets income list
                income_list = cursor.fetchall()
                # Returns income_list
                return income_list
            
            except Exception:
                print("Could not retrieve income records by user id and category")


    def delete_income_transaction_by_id(self, transaction_id):
        """Deletes income record by transaction id
        
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
                print("Could not delete income transaction by id")



    def add_income_transaction_record(self, user_id, date, category, amount):
        """Creates and adds a new transaction record in transactions_table
        
            :param int user_id: receives the user's id
            :param string date: receives the date of the transaction
            :param string category: receives the income category
            :param float amoun: receives the amount of the income
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                cursor.execute('''INSERT INTO transactions_table
                                VALUES (?, ?, ?, "Income", ?, ?);''',
                                (self.auto_assign_transaction_id(), user_id, date, category, amount))
                db.commit()
            
            except Exception:
                db.rollback
                print("Income transaction record could not be created in transactions_table")


    def get_expense_sum_of_category_and_id(self, user_id, category):
        """Gets the sum of amount of expense records where the user_id and category match 
            in transactions_table
        
            :param int user_id: takes user's id
            :param string category: takes category

            :returns: sum of all the expenses by category and id

            :rtype: float
        """
        # opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes cursor
                cursor.execute('''SELECT SUM(Total) FROM transactions_table
                                WHERE User_id = ?
                                AND Category = ?
                                And Income_or_expense = "Expense"''',
                                (user_id, category,))
                # Gets the sum
                sum = cursor.fetchone()
                return sum
            except Exception:
                print("Could not return a sum of expenses by category from transactions_table")


    #=====Category table Section=====#
    '''Contains all the methods conserning the "income_expense_category_table"'''

    def create_new_income_category(self, user_id, category_title):
        """Creates a new income category record in the \"income_expense_category_table\"
        
            :param int user_id: The user's id to who the category is related to
            :param string category_title: The new name of the income category
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''INSERT INTO income_expense_category_table
                                    VALUES (?, ?, "Income", ?);
                                    ''', (self.auto_assign_category_id(), user_id, category_title))
                db.commit()
                print("new income category added")
            except Exception:
                db.rollback()
                print("new income category could not be added")


    def create_new_expense_category(self, user_id, category_title):
        """Creates a new income category record in the \"income_expense_category_table\"
        
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


    def delete_income_category(self, category_id):
        """Deletes a income_category from the \"income_expense_category_table\"
        
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
                print("Income category removed")
            except Exception:
                db.rollback()
                print("Income category could not be removed")


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
                print("Income category removed")
            except Exception:
                db.rollback()
                print("Income category could not be removed")


    def delete_expense_category_by_category(self, category):
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
                                    WHERE Category_Title = ?
                                    AND Income_or_expense = "Expense";
                                    ''', (category,))
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
        """returns all the records where categories are expense

        :param int user_id: contains the user id with what the expense are related to

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
                income_category_list = cursor.fetchall()
                return income_category_list
            except Exception:
                print("Could not retrieve income_category_list")


    def get_a_expense_categories(self, user_id, category):
        """returns all the records where specific category and id

        :param int user_id: contains the user id with what the expense are related to
        :param string category: uses category of expense

        :returns: list of expense records related to the user id and category

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
                                    Income_or_expense = "Expense"
                                    AND Category_Title = ?;''',
                                    (user_id, category,))
                # Stores the categorie records in alist
                expense_category_list = cursor.fetchall()
                return expense_category_list
            except Exception:
                print("Could not retrieve expense_category_list")


    def expense_category_exists(self, user_id, category):
        """Checks wether a specific expense caegory exists
        
            :param int user_id: uses the user's id
            :param string categor: uses the category to check if it exists

            :returns: True if category exists, False if not

            :rtype: bool
        """
        # gets list
        list = self.get_a_expense_categories(user_id, category)

        # checks if list is more than 0, return True if so.
        if len(list) > 0:
            return True
        else:
            return False


    def get_all_income_categories(self, user_id):
        """returns all the records where categories are income

        :param int user_id: contains the user id with what the income are related to

        :returns: list of income records related to the user id

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
                                    Income_or_Expense = "Income";''',
                                    (user_id,))
                # Stores the categorie records in alist
                income_category_list = cursor.fetchall()
                return income_category_list
            except Exception:
                print("Could not retrieve income_category_list")


    #=====Budget Table Section=====#
    '''This section contains all the methods related to the budget_table'''

    def budget_category_exists(self, category, user_id):
        """Checks wether a budget category exists, return true if it does exist
        
            :param string category: the category that needs to be searched
            :param int user_id: gets the user id

            :returns: True if category exists, return False if not

            :rtype: bool
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates query
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''SELECT * FROM budget_table
                                WHERE Category = ? 
                                AND User_id = ?;''',(category, user_id))
                # Gets list
                category_list = cursor.fetchall()
                # Returns True if category_list's length more than 0, else false
                if len(category_list) > 0:
                    return True
                else:
                    return False
                
            except Exception:
                print("Could not determine if category exists in budget_table")

    
    def add_budget_record(self, user_id, category, budget_amount):
        """Adds a budget category to the budget_table
        
            :param int user_id: Takes the user id
            :param string category: takes the category of the expense
            :param float budget_amount: takes the total amount of the budget in the expense
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''INSERT INTO budget_table
                                VALUES (?, ?, ?, ?);''', 
                                (self.auto_assign_budget_id(), user_id, category, budget_amount,))
                db.commit()
            
            except Exception:
                db.rollback()
                print("Could not add new budget record")


    def update_budget_record(self, user_id, category, budget_amount):
        """Adds a budget category to the budget_table
        
            :param int user_id: Takes the user id
            :param string category: takes the category of the expense
            :param float budget_amount: takes the total amount of the budget in the expense
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''UPDATE budget_table
                                SET Total = ?
                                WHERE User_id = ?
                                AND Category = ?;''', 
                                (budget_amount, user_id, category,))
                db.commit()
            
            except Exception:
                db.rollback()
                print("Could not update budget record")
                
    
    def get_all_budget_by_id(self, user_id):
        """Gets all the budget records by user
        
            :param int user_id: uses the user's id

            :returns: list of budget records of the user

            :rtype: list
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''SELECT * FROM budget_table
                                WHERE User_id = ?''', (user_id,))
                # Gets list
                budget_list = cursor.fetchall()
                # Returns list
                return budget_list
            
            except Exception:
                print("Could not return a list from budget_table")


    def get_all_budget_categories_by_user_id(self, user_id):
        """Gets all the budget categories by id
        
            :param int user_id: uses user's id as key

            :returns: a list of all records with the user's id

            :rtype: list
        """
        # Opens Database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''SELECT * FROM budget_table
                               WHERE User_id = ?''', (user_id,))
                # Gets budget records
                budget_records = cursor.fetchall()
                return budget_records
            except Exception:
                print("Could not return a list of all budget categories by user id from budget_table")


    def delete_budget_record_by_category_and_user_id(self, user_id, category):
        """Removes a record from the budget_table with the user id and category details
        
            :param int user_id: uses user's id
            :param string category: uses category of the budget
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor =db.cursor()

            try:
                # Executes query
                cursor.execute('''DELETE FROM budget_table
                               WHERE User_id = ?
                               AND Category = ?;''', (user_id, category,))
                # Commits
                db.commit()

            except Exception:
                db.rollback()
                print("Could not delete record from budget_table")


    def auto_assign_budget_id(self):
        """Automaticaly assigns an id if it does not exist in the \"budget_table\"
        
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
                    cursor.execute(f"""SELECT * FROM budget_table
                                        WHERE Budget_id = ?;""", (id,))
                    # Gets list of categories
                    budget_list = cursor.fetchall()
                    # Checks if budget equals 0, then breaks loop if does exist
                    if len(budget_list) == 0:
                        # returns id
                        return id
                    else:
                        id += 1
                except Exception:
                    print("Could not generate a budget id")
                    break


    def get_all_budget_by_user_id_and_category(self, user_id, category):
        """Gets all budget records by user_id and category, returns a list
        
            :param int user_id: the user's ID
            :param string category: the category by which list must be fetched

            :returns: list of budgets by user and category

            :rtype: list
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''SELECT * FROM budget_table
                               WHERE User_id = ? 
                               AND Category LIKE ?;''', (user_id, f"%{category}%",))
                # Gets budget list
                budget_list = cursor.fetchall()
                # Returns expense_list
                return budget_list
            
            except Exception:
                print("Could not retrieve budget records by user id and category")


    #=====Financial Goals Table Section=====#
    '''This section contains all the methods related to the budget_table'''

    def financial_goal_category_exists(self, category, user_id):
        """Checks wether a financial goal category exists, return true if it does exist
        
            :param string category: the category that needs to be searched
            :param int user_id: gets the user id

            :returns: True if category exists, return False if not

            :rtype: bool
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates query
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''SELECT * FROM financial_goals_table
                                WHERE Category = ? 
                                AND User_id = ?;''',(category, user_id))
                # Gets list
                category_list = cursor.fetchall()
                # Returns True if category_list's length more than 0, else false
                if len(category_list) > 0:
                    return True
                else:
                    return False
                
            except Exception:
                print("Could not determine if category exists in financial_goals_table")

    
    def add_financial_goals_record_and_maybe_expense_record(self, user_id, category, goal_amount):
        """Adds a budget category to the budget_table, and maybe to expense category table if it does
            not exist.
        
            :param int user_id: Takes the user id
            :param string category: takes the category of the expense
            :param float goal_amount: takes the total amount of the financial goal
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''INSERT INTO financial_goals_table
                                VALUES (?, ?, ?, ?);''', 
                                (self.auto_assign_goal_id(), user_id, category, goal_amount,))
                db.commit()

                # If category does not exist in expenses, create it
                if self.expense_category_exists(user_id, category) == False:
                    self.create_new_expense_category(user_id, category)
            
            except Exception:
                db.rollback()
                print("Could not add new financial goal record")

            
    def update_financial_goal_record(self, user_id, category, goal_amount):
        """Adds a budget category to the budget_table
        
            :param int user_id: Takes the user id
            :param string category: takes the category of the goal
            :param float budget_amount: takes the total amount of the goal
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''UPDATE financial_goals_table
                                SET Total = ?
                                WHERE User_id = ?
                                AND Category = ?;''', 
                                (goal_amount, user_id, category,))
                db.commit()
            
            except Exception:
                db.rollback()
                print("Could not update financial goal record")
                
    
    def get_all_financial_goals_by_id(self, user_id):
        """Gets all the financial goal records by user
        
            :param int user_id: uses the user's id

            :returns: list of financial goal records of the user

            :rtype: list
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''SELECT * FROM financial_goals_table
                                WHERE User_id = ?''', (user_id,))
                # Gets list
                goal_list = cursor.fetchall()
                # Returns list
                return goal_list
            
            except Exception:
                print("Could not return a list from budget_table")


    def delete_financial_goal_record_by_category_and_user_id(self, user_id, category):
        """Removes a record from the budget_table and income_expense_category_table 
            with the user id and category details
        
            :param int user_id: uses user's id
            :param string category: uses category of the budget
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor =db.cursor()

            try:
                # Executes query for budget table
                cursor.execute('''DELETE FROM financial_goals_table
                               WHERE User_id = ?
                               AND Category = ?;''', (user_id, category,))
                # Commits
                db.commit()
                self.delete_expense_category_by_category(category)

            except Exception:
                db.rollback()
                print("Could not delete record from budget_table and income_expense_category_table")



    def auto_assign_goal_id(self):
        """Automaticaly assigns an id if it does not exist in the \"financial_goals_table\"
        
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
                    cursor.execute(f"""SELECT * FROM financial_goals_table
                                        WHERE Goal_id = ?;""", (id,))
                    # Gets list of categories
                    goal_list = cursor.fetchall()
                    # Checks if goal id equals 0, then breaks loop if does exist
                    if len(goal_list) == 0:
                        # returns id
                        return id
                    else:
                        id += 1
                except Exception:
                    print("Could not generate a goal id")
                    break


    def search_all_financial_goals_by_user_id_and_category(self, user_id, category):
        """Gets all financial_goal records by user_id and category, returns a list
        
            :param int user_id: the user's ID
            :param string category: the category by which list must be fetched

            :returns: list of financial_goals by user id and category

            :rtype: list
        """
        # Opens database
        with sqlite3.connect("Database/users_db") as db:
            # Creates cursor
            cursor = db.cursor()

            try:
                # Executes query
                cursor.execute('''SELECT * FROM financial_goals_table
                               WHERE User_id = ? 
                               AND Category LIKE ?;''', (user_id, f"%{category}%",))
                # Gets fiancial goal list
                goal_list = cursor.fetchall()
                # Returns goal_list
                return goal_list
            
            except Exception:
                print("Could not retrieve financial goal records by user id and category")