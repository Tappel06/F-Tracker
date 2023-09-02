"""This file contains all the code for the user profile"""

#=====Imports=====#
'''This section contains all the imports for the file'''
import Presentation_layer.shared_display
from Business_Layer.database_connect import Database_Connection

#=====Classes=====#
'''This section contains all the classes'''
class User_profile():

    #====Constructor====#

    def __init__(self, user_record):
        # Stores user details
        self.user_details = user_record
        # Creates database object
        self.db = Database_Connection()
        # Runs the main menu options
        self.main_menu_options()


    #====Main menu methods====#
    '''Contains all the methods associated with the main menu'''

    def main_menu_options(self):
        """Takes the input of the menu options, then implements methods according to the input"""

        # Prints the logo
        self.logo("m")
        # Prints the options
        self.print_main_menu_options()
        
        # Loops option
        while True:
            # gets option input
            option = input("Option: ")

            # If option "1" selected, go to "expenses_menu_options"
            if option == "1":
                self.expenses_menu_options()
                # Prints the logo
                self.logo("m")
                # Prints the options
                self.print_main_menu_options()

            # Else if option "2" selected, go to "income_menu_options"
            elif option == "2":
                self.income_menu_options()
                # Prints the logo
                self.logo("m")
                # Prints the options
                self.print_main_menu_options()

            # Else if option "3" selected, go to "budget_menu_options"
            elif option == "3":
                pass

            # Else if option "4" selected, got to "fianacial_goals_menu_options"
            elif option == "4":
                pass

            # Else if option "5" selected, break the loop
            elif option == "5":
                break

            # Else if option "6" selected, exit
            elif option == "6":
                exit()

            # Else, print that a given option has not been chosen
            else:
                # Prints the logo
                self.logo("m")
                print("\n***** You did not enter a given option! *****")
                self.print_main_menu_options()


    def print_main_menu_options(self):
        """Prints the main menus' options"""
        print('''
1. Expenses
2. Income
3. Budget
4. Financial goals
5. Logout
6. Exit
''')


    #=====Expenses Menu Methods=====#
    '''Coantains all the methods associated with the expenses menu'''

    def expenses_menu_options(self):
        """Takes the input of the expense menu options, then implements methods according to the input"""
        # Prints the logo
        self.logo("e")
        # Print expens menu options
        self.print_expense_menu_options()

        # Loops option
        while True:
            # Gets option input
            option = input("\nOption: ")

            # If option equals "1", run "add_expense"
            if option == "1":
                self.add_expense()
                # Prints the logo
                self.logo("e")
                # Print expens menu options
                self.print_expense_menu_options()

            # Else if option equals "2", run "view_expense"
            elif option == "2":
                self.view_expenses()
                # Prints the logo
                self.logo("e")
                # Print expens menu options
                self.print_expense_menu_options()

            # Else if option equals "3", run "view_expense_by_category"
            elif option == "3":
                self.view_expense_by_category()
                # Prints the logo
                self.logo("e")
                # Print expens menu options
                self.print_expense_menu_options()

            # Else if option equals "4", run "add_remove_expense_category"
            elif option == "4":
                self.add_remove_expense_category()
                # Prints the logo
                self.logo("e")
                # Print expens menu options
                self.print_expense_menu_options()

            # Else if option equals "5", break loop to return to previous menu
            elif option == "5":
                break

            # Else, print that incorrect option inserted
            else:
                # Prints the logo
                self.logo("e")
                print("\n***** You did not enter a given option!")
                # Print expens menu options
                self.print_expense_menu_options()


    def print_expense_menu_options(self):
        """Prints the expense menus' options"""
        print('''
1. Add expense
2. View expenses
3. View expenses by category
4. Add or remove an expense category
5. Previous menu''')


    def add_expense(self):
        """Adds a new expense record"""
        # Gets Expense Categories
        expense_categories = self.db.get_all_expense_categories(self.user_details[0][0])
        # Prints the logo
        self.logo("e")
        
        # Loop to check if a date value exist, otherwise end method
        while True:

            # Get user input for date
            date = self.date_string_creator()
            
            if date == None:
                # Exit method
                return
            else:
                # Print logo
                self.logo("e")
                # Exits loop
                break

        # Loop Choose category
        while True:
            # Choose an Expense Category, or Type "E" to cancel:
            print("\nChoose an expense category, or type \"E\" to cancel:\n")

            # varaible containing index no.
            index_no = 1
            # Prints out expense catefory
            for category in expense_categories:
                print(f"{index_no}. {category[3]}")
                index_no += 1

            category_input = input("\nOption: ")

            # Checks if option is equal to "E", ends method if it does
            if category_input.upper() == "E":
                # Exits method
                return
            
            try:
                # Checks if option can be casted to an integer
                if int(category_input):
                    # If number is within index range
                    if len(expense_categories) > 0 and int(category_input) > 0 and int(category_input) < len(expense_categories) + 1:
                        # Adds new value category_String
                        category_string = expense_categories[int(category_input)-1][3]
                        # Break loop
                        break
                    else:
                        # Prints the logo
                        self.logo("e")
                        print("\n***** You did not enter a given option! *****\n")

            except Exception:
                # Prints the logo
                self.logo("e")
                print("\n***** You did not enter a given option! *****\n")

        # Print logo
        self.logo("e")
        # Loop Amount input
        while True:
            try:
                amount = float(input("\nInsert the expense amount: "))
                break
            except Exception:
                # Print logo
                self.logo("e")
                print("\n***** You did not enter an amount! *****")

        # Print logo
        self.logo("e")
        while True:
            # Print confirmation input of adding the new expense record
            confirm = input(f"""\nYou are about to add the following expense record:\n
Date: {date}
Category: {category_string}
Amount: {amount}

Are you sure you want to add this record? (Y/N): """)
            
            # Adds record if confirm equals "Y"
            if confirm.upper() == "Y":
                self.db.add_expense_transaction_record(self.user_details[0][0], date, category_string, amount)
                break

            # Else if confirm equal "N", then break
            elif confirm.upper() == "N":
                break
            # Else print option was not selected
            else:
                # Prints logo
                self.logo("e")
                print("\n***** You did not select (Y/N)! *****\n")


    def view_expenses(self):
        """Displays all the expense records, and have the option to delete a record"""
        # Prints logo
        self.logo("e")
        # Prints Expenses
        self.print_expenses()

        # Print options:
        print("""\n1. Delete expense by ID
2. Return to previous menu""")
        # Options to delete expense, or return to previous menu
        while True:
            # Option input
            option = input("\nOption: ")

            # If option equals "1", run delete_expense
            if option == "1":
                self.delete_expense()
                # Prints logo
                self.logo("e")
                # Prints Expenses
                self.print_expenses()
                # Print options:
                print("""\n1. Delete expense by ID
2. Return to previous menu""")

            # Else if option equals "2", break to go back to previous menu
            elif option == "2":
                break
            
            # Else print given option not selected
            else:
                print("\n***** You did not enter a given option! *****")


    def delete_expense(self):
        """Deletes an expense record by id"""
        # Get expense transactions
        expense_transactions = self.db.get_all_expenses_by_user_id(self.user_details[0][0])

        while True:
            # Bool to indicate if user selected correct option
            correct_option = False
            # Gets input
            id = input("\nEnter \"E\" to cancel\nTransaction ID: ")

            # Checks if "E" has been entered
            if id.upper() == "E":
                # Breaks loop to go to previous menu
                break

            for expense in expense_transactions:
                # If id is equal to the expense option
                if id == str(expense[0]):
                    # Set correct_option to True
                    correct_option = True
                    # Breaks for loop
                    break

            # If correct option equals true
            if correct_option == True:
                # Delete Record
                self.db.delete_expense_transaction_by_id(id)
                # Break loop
                break    
            

    def print_expenses(self):
        "Prints a list of expenses"
        # Gets expense list
        expense_list = self.db.get_all_expenses_by_user_id(self.user_details[0][0])
        # Variable that contains the total amount of all the expenses
        total_amount = 0.00
        
        print("\nAll Expenses:\n")
        print("\n--------------------------------------------------------------------------------")
        
        for expense in expense_list:
            # adds up the total amount of expenses
            total_amount += expense[5]
            # Prints Expenses
            print(f'''Transaction ID: {expense[0]},   Date: {expense[2]},   Category: {expense[4]},   Amount: {expense[5]}
--------------------------------------------------------------------------------''')
            
        # prints the total expenses
        print(f'''================================================================================
The total of all your expenses are : {total_amount}
================================================================================''')
            
        
    def view_expense_by_category(self):
        """Displays all the expense records by category"""
        # Prints logo
        self.logo("e")
        
        # Loops list
        while True:
            # Prints options
            print('''
1. Enter category
2. Return to previous menu''')
            
            # Gets option input
            option = input("\nOption: ")
            
            # If option 1 is selected
            if option == "1":
                # Prints logo
                self.logo("e")
                # gets input for category keyword
                category = input("\nEnter an expense category: ")
                
                # Prints logo
                self.logo("e")
                # prints the category list
                self.print_expenses_by_category(category)
                

            # If option 2 is selected
            elif option == "2":
                # breaks loop to go back to previous menu
                break
            else:
                # Prints logo
                self.logo("e")
                # Print that option has not been selected
                print("\n***** You have not selected an option! *****")


    def print_expenses_by_category(self, category):
        """Prints a list by category"""
        # Gets list
        category_list = self.db.get_all_expenses_by_user_id_and_category(self.user_details[0][0], category)

        # adds up the total amount of expenses
        total_amount = 0.00

        print(f"\nYour Expenses for this category search:\n")
        print("\n--------------------------------------------------------------------------------")

        for expense in category_list:
            # adds up the total amount of expenses
            total_amount += expense[5]
            # Prints Expenses
            print(f'''Transaction ID: {expense[0]},   Date: {expense[2]},   Category: {expense[4]},   Amount: {expense[5]}
--------------------------------------------------------------------------------''')
            
        # prints the total expenses
        print(f'''================================================================================
The total of all this expenses are : {total_amount}
================================================================================''')

    def add_remove_expense_category(self):
        """Displays a list of current categories, and preview options to add or remove new ones"""
        # Prints the logo
        self.logo("e")
        # Displays all the current expense categories
        self.print_expense_categories()
        # Prints category options
        self.print_add_remove_expense_category_options()

        # Loops options
        while True:
            # option input
            option = input("\nOption: ")

            # if option equals "1", run "add_expense_category"
            if option == "1":
                self.add_expense_category()
                # Prints the logo
                self.logo("e")
                # Displays all the current expense categories
                self.print_expense_categories()
                # Prints category options
                self.print_add_remove_expense_category_options()

            # if option equals "2", run "remove_expense_category"
            elif option == "2":
                self.remove_expense_category()
                # Prints the logo
                self.logo("e")
                # Displays all the current expense categories
                self.print_expense_categories()
                # Prints category options
                self.print_add_remove_expense_category_options()

            # if option equals "3", break loop to go to previous menu
            elif option == "3":
                break

            # else print that an option is not selected
            else:
                print("\n***** You did not enter a given option! *****")


    def print_add_remove_expense_category_options(self):
        """Prints the options add or remove category"""
        print('''
1. Add category
2. Remove Category
3. Previous menu''')
        

    def add_expense_category(self):
        """Adds a new expense category"""

        # loops questions
        while True: 
            # Prints type "E" to cancel current procedure
            print("\nType \"E\" to cancel")
            category_name = input("What is the name of your new expense: ")
            # Checks if "E" is typed
            if category_name.upper() == "E":
                break
            elif category_name != "":
                self.db.create_new_expense_category(self.user_details[0][0], category_name)
                # Prints the logo
                self.logo("e")
                # Displays all the current expense categories
                self.print_expense_categories()
                print(f"\n***** {category_name} added to expense categories. *****\n")
            else:
                print("***** You did not type anything! *****")


    def remove_expense_category(self):
        """Removes an expense Category"""

        # Gets a list of all the expense categories under this user's id
        categories = self.db.get_all_expense_categories(self.user_details[0][0])
        # Prints the logo
        self.logo("e")
        # Print open space
        print("")
        # Print expense categories
        self.print_expense_categories()

        # loops
        while True:

            # Takes int value as input
            option = input("\nEnter \"E\" to cancel\nCategory ID: ")

            # Checks if "E" has been entered
            if option.upper() == "E":
                break

            try: 
                # Checks if option can be casted
                if int(option):
                    # Boolean value if no ID's matched
                    id_match = False

                    # Runs a loop to see if any id"s match
                    for category in categories:

                        if int(option) == category[0]:
                            # Sets id_match to True
                            id_match = True
                            self.db.delete_expense_category(int(option))

                            # Prints the logo
                            self.logo("e")
                            # Print Category removed
                            print("\n***** Category has been removed successfully *****")
                            # Gets a list of all the expense categories under this user's id
                            categories = self.db.get_all_expense_categories(self.user_details[0][0])
                            # Print expense categories
                            self.print_expense_categories()
                            # Break loop
                            break

                    # if id_match equals False, print option not chosen
                    if id_match == False:
                        # Prints the logo
                        self.logo("e")
                        print("\n***** You did not insert a valid ID! *****\n")
                        # Print expense categories
                        self.print_expense_categories()

            except Exception:
                # Prints the logo
                self.logo("e")
                print("\n***** You did not insert a valid ID! *****\n")
                # Print expense categories
                self.print_expense_categories()
                pass


    def print_expense_categories(self):
        """Prints out all the expense categories under user's id"""

        # Gets a list of all the expense categories under this user's id
        categories = self.db.get_all_expense_categories(self.user_details[0][0])

        print("Expense categories: \n")

        # Prints each category
        for category in categories:
            print(f"ID: {category[0]}, Name: {category[3]}")


    #=====Income Menu Methods=====#
    '''Coantains all the methods associated with the income menu'''

    def income_menu_options(self):
        """Takes the input of the income menu options, then implements methods according to the input"""
        # Prints the logo
        self.logo("e")
        # Print expens menu options
        self.print_income_menu_options()

        # Loops option
        while True:
            # Gets option input
            option = input("\nOption: ")

            # If option equals "1", run "add_income"
            if option == "1":
                self.add_income()
                # Prints the logo
                self.logo("e")
                # Print expens menu options
                self.print_income_menu_options()

            # Else if option equals "2", run "view_income"
            elif option == "2":
                self.view_income()
                # Prints the logo
                self.logo("e")
                # Print expens menu options
                self.print_income_menu_options()

            # Else if option equals "3", run "view_income_by_category"
            elif option == "3":
                self.view_income_by_category()
                # Prints the logo
                self.logo("e")
                # Print expens menu options
                self.print_income_menu_options()

            # Else if option equals "4", run "add_remove_income_category"
            elif option == "4":
                self.add_remove_income_category()
                # Prints the logo
                self.logo("e")
                # Print expens menu options
                self.print_income_menu_options()

            # Else if option equals "5", break loop to return to previous menu
            elif option == "5":
                break

            # Else, print that incorrect option inserted
            else:
                # Prints the logo
                self.logo("e")
                print("\n***** You did not enter a given option!")
                # Print expens menu options
                self.print_income_menu_options()


    def print_income_menu_options(self):
        """Prints the income menus' options"""
        print('''
1. Add income
2. View income
3. View income by category
4. Add or remove an income category
5. Previous menu''')


    def add_income(self):
        """Adds a new income record"""
        # Gets income Categories
        income_categories = self.db.get_all_income_categories(self.user_details[0][0])
        # Prints the logo
        self.logo("e")
        
        # Loop to check if a date value exist, otherwise end method
        while True:

            # Get user input for date
            date = self.date_string_creator()
            
            if date == None:
                # Exit method
                return
            else:
                # Print logo
                self.logo("e")
                # Exits loop
                break

        # Loop Choose category
        while True:
            # Choose an income Category, or Type "E" to cancel:
            print("\nChoose an income category, or type \"E\" to cancel:\n")

            # varaible containing index no.
            index_no = 1
            # Prints out income catefory
            for category in income_categories:
                print(f"{index_no}. {category[3]}")
                index_no += 1

            category_input = input("\nOption: ")

            # Checks if option is equal to "E", ends method if it does
            if category_input.upper() == "E":
                # Exits method
                return
            
            try:
                # Checks if option can be casted to an integer
                if int(category_input):
                    # If number is within index range
                    if len(income_categories) > 0 and int(category_input) > 0 and int(category_input) < len(income_categories) + 1:
                        # Adds new value category_String
                        category_string = income_categories[int(category_input)-1][3]
                        # Break loop
                        break
                    else:
                        # Prints the logo
                        self.logo("e")
                        print("\n***** You did not enter a given option! *****\n")

            except Exception:
                # Prints the logo
                self.logo("e")
                print("\n***** You did not enter a given option! *****\n")

        # Print logo
        self.logo("e")
        # Loop Amount input
        while True:
            try:
                amount = float(input("\nInsert the income amount: "))
                break
            except Exception:
                # Print logo
                self.logo("e")
                print("\n***** You did not enter an amount! *****")

        # Print logo
        self.logo("e")
        while True:
            # Print confirmation input of adding the new income record
            confirm = input(f"""\nYou are about to add the following income record:\n
Date: {date}
Category: {category_string}
Amount: {amount}

Are you sure you want to add this record? (Y/N): """)
            
            # Adds record if confirm equals "Y"
            if confirm.upper() == "Y":
                self.db.add_income_transaction_record(self.user_details[0][0], date, category_string, amount)
                break

            # Else if confirm equal "N", then break
            elif confirm.upper() == "N":
                break
            # Else print option was not selected
            else:
                # Prints logo
                self.logo("e")
                print("\n***** You did not select (Y/N)! *****\n")


    def view_income(self):
        """Displays all the income records, and have the option to delete a record"""
        # Prints logo
        self.logo("e")
        # Prints income
        self.print_income()

        # Print options:
        print("""\n1. Delete income by ID
2. Return to previous menu""")
        # Options to delete income, or return to previous menu
        while True:
            # Option input
            option = input("\nOption: ")

            # If option equals "1", run delete_income
            if option == "1":
                self.delete_income()
                # Prints logo
                self.logo("e")
                # Prints income
                self.print_income()
                # Print options:
                print("""\n1. Delete income by ID
2. Return to previous menu""")

            # Else if option equals "2", break to go back to previous menu
            elif option == "2":
                break
            
            # Else print given option not selected
            else:
                print("\n***** You did not enter a given option! *****")


    def delete_income(self):
        """Deletes an income record by id"""
        # Get income transactions
        income_transactions = self.db.get_all_income_by_user_id(self.user_details[0][0])

        while True:
            # Bool to indicate if user selected correct option
            correct_option = False
            # Gets input
            id = input("\nEnter \"E\" to cancel\nTransaction ID: ")

            # Checks if "E" has been entered
            if id.upper() == "E":
                # Breaks loop to go to previous menu
                break

            for income in income_transactions:
                # If id is equal to the income option
                if id == str(income[0]):
                    # Set correct_option to True
                    correct_option = True
                    # Breaks for loop
                    break

            # If correct option equals true
            if correct_option == True:
                # Delete Record
                self.db.delete_income_transaction_by_id(id)
                # Break loop
                break    
            

    def print_income(self):
        "Prints a list of income"
        # Gets income list
        income_list = self.db.get_all_income_by_user_id(self.user_details[0][0])
        # Variable that contains the total amount of all the income
        total_amount = 0.00
        
        print("\nAll income:\n")
        print("\n--------------------------------------------------------------------------------")
        
        for income in income_list:
            # adds up the total amount of income
            total_amount += income[5]
            # Prints income
            print(f'''Transaction ID: {income[0]},   Date: {income[2]},   Category: {income[4]},   Amount: {income[5]}
--------------------------------------------------------------------------------''')
            
        # prints the total income
        print(f'''================================================================================
The total of all your income are : {total_amount}
================================================================================''')
            
        
    def view_income_by_category(self):
        """Displays all the income records by category"""
        # Prints logo
        self.logo("e")
        
        # Loops list
        while True:
            # Prints options
            print('''
1. Enter category
2. Return to previous menu''')
            
            # Gets option input
            option = input("\nOption: ")
            
            # If option 1 is selected
            if option == "1":
                # Prints logo
                self.logo("e")
                # gets input for category keyword
                category = input("\nEnter an income category: ")
                
                # Prints logo
                self.logo("e")
                # prints the category list
                self.print_income_by_category(category)
                

            # If option 2 is selected
            elif option == "2":
                # breaks loop to go back to previous menu
                break
            else:
                # Prints logo
                self.logo("e")
                # Print that option has not been selected
                print("\n***** You have not selected an option! *****")


    def print_income_by_category(self, category):
        """Prints a list by category"""
        # Gets list
        category_list = self.db.get_all_income_by_user_id_and_category(self.user_details[0][0], category)

        # adds up the total amount of income
        total_amount = 0.00

        print(f"\nYour income for this category search:\n")
        print("\n--------------------------------------------------------------------------------")

        for income in category_list:
            # adds up the total amount of income
            total_amount += income[5]
            # Prints income
            print(f'''Transaction ID: {income[0]},   Date: {income[2]},   Category: {income[4]},   Amount: {income[5]}
--------------------------------------------------------------------------------''')
            
        # prints the total income
        print(f'''================================================================================
The total of all this income are : {total_amount}
================================================================================''')

    def add_remove_income_category(self):
        """Displays a list of current categories, and preview options to add or remove new ones"""
        # Prints the logo
        self.logo("e")
        # Displays all the current income categories
        self.print_income_categories()
        # Prints category options
        self.print_add_remove_income_category_options()

        # Loops options
        while True:
            # option input
            option = input("\nOption: ")

            # if option equals "1", run "add_income_category"
            if option == "1":
                self.add_income_category()
                # Prints the logo
                self.logo("e")
                # Displays all the current income categories
                self.print_income_categories()
                # Prints category options
                self.print_add_remove_income_category_options()

            # if option equals "2", run "remove_income_category"
            elif option == "2":
                self.remove_income_category()
                # Prints the logo
                self.logo("e")
                # Displays all the current income categories
                self.print_income_categories()
                # Prints category options
                self.print_add_remove_income_category_options()

            # if option equals "3", break loop to go to previous menu
            elif option == "3":
                break

            # else print that an option is not selected
            else:
                print("\n***** You did not enter a given option! *****")


    def print_add_remove_income_category_options(self):
        """Prints the options add or remove category"""
        print('''
1. Add category
2. Remove Category
3. Previous menu''')
        

    def add_income_category(self):
        """Adds a new income category"""

        # loops questions
        while True: 
            # Prints type "E" to cancel current procedure
            print("\nType \"E\" to cancel")
            category_name = input("What is the name of your new income: ")
            # Checks if "E" is typed
            if category_name.upper() == "E":
                break
            elif category_name != "":
                self.db.create_new_income_category(self.user_details[0][0], category_name)
                # Prints the logo
                self.logo("e")
                # Displays all the current income categories
                self.print_income_categories()
                print(f"\n***** {category_name} added to income categories. *****\n")
            else:
                print("***** You did not type anything! *****")


    def remove_income_category(self):
        """Removes an income Category"""

        # Gets a list of all the income categories under this user's id
        categories = self.db.get_all_income_categories(self.user_details[0][0])
        # Prints the logo
        self.logo("e")
        # Print open space
        print("")
        # Print income categories
        self.print_income_categories()

        # loops
        while True:

            # Takes int value as input
            option = input("\nEnter \"E\" to cancel\nCategory ID: ")

            # Checks if "E" has been entered
            if option.upper() == "E":
                break

            try: 
                # Checks if option can be casted
                if int(option):
                    # Boolean value if no ID's matched
                    id_match = False

                    # Runs a loop to see if any id"s match
                    for category in categories:

                        if int(option) == category[0]:
                            # Sets id_match to True
                            id_match = True
                            self.db.delete_income_category(int(option))

                            # Prints the logo
                            self.logo("e")
                            # Print Category removed
                            print("\n***** Category has been removed successfully *****")
                            # Gets a list of all the income categories under this user's id
                            categories = self.db.get_all_income_categories(self.user_details[0][0])
                            # Print income categories
                            self.print_income_categories()
                            # Break loop
                            break

                    # if id_match equals False, print option not chosen
                    if id_match == False:
                        # Prints the logo
                        self.logo("e")
                        print("\n***** You did not insert a valid ID! *****\n")
                        # Print income categories
                        self.print_income_categories()

            except Exception:
                # Prints the logo
                self.logo("e")
                print("\n***** You did not insert a valid ID! *****\n")
                # Print income categories
                self.print_income_categories()
                pass


    def print_income_categories(self):
        """Prints out all the income categories under user's id"""

        # Gets a list of all the income categories under this user's id
        categories = self.db.get_all_income_categories(self.user_details[0][0])

        print("Income categories: \n")

        # Prints each category
        for category in categories:
            print(f"ID: {category[0]}, Name: {category[3]}")


    #=====Shared Methods=====#
    '''Contains all the methods shared among the other methods in this class'''

    def logo(self, menu_type):
        """Clears console and prints the logo, user details, and the current menu type
        
            :param string menu_type: The type of menu header
        """
        # Uses the header from "shared_display file" 
        Presentation_layer.shared_display.header()
        # Prints out user details
        print(f'''User: {self.user_details[0][2]} {self.user_details[0][3]}
Logged in as: {self.user_details[0][1]}
User ID: {self.user_details[0][0]}
================================================================================''')
        
        # Menu header options
        # If menu equals "m" print "Main Menu"
        if menu_type == "m":
            print('''||  Main Menu  ||
=================''')
        
        # IF menu equals "e" print "Expense Menu"
        elif menu_type == "e":
            print('''||  Expense Menu  ||
====================''')
            
        # IF menu equals "i" print "Income Menu"
        elif menu_type == "i":
            print('''||  Income Menu  ||
===================''')
            

    def date_string_creator(self):
        """Turns a user's input into a date in string format
        
            :returns: returns the date in a string format

            :rtype: string
        """
        # Dictionary of the amounts of days in each month
        months = {1 : 31, 2 : 29, 3 : 31, 4 : 30, 5 : 31, 6 : 30,
                  7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
        
        # Escape variable
        escape = False

        # Prints enter "0" to escape
        print("\nEnter \"0\" to escpae")

        # Takes year input
        while True:
            try:
                year = int(input("\nInsert the year (yyyy): "))

                # Checks if "0" has been entere
                if year == 0:
                    # Sets escape to True
                    escape = True
                    break

                # Checks that the length of year is four
                if year < 1900 or year > 10000:
                    print("\n***** You did not enter a year (yyyy)! *****\n")
                else:
                    break

            except Exception:
                print("\n***** You did not enter a year (yyyy)! *****\n")

        # Checks if escape equals True, then cancels method
        if escape == True:
            return

        # Takes month input
        while True:
            try:
                month = int(input("Insert the month number: "))

                # Checks if "0" has been entered
                if month == 0:
                    # Sets escape to True
                    escape = True
                    break

                # Checks that month is 1 - 12
                if month < 1 or month > 12:
                    print("\n***** You did not enter a month! *****\n")

                else:
                    break

            except Exception:
                print("\n***** You did not enter a month! *****\n")

        # Checks if escape equals True, then cancels method
        if escape == True:
            return
        
        # Takes day input
        while True:
            try:
                day = int(input("Insert the day of the month: "))

                # Checks if "0" has been entered
                if day == 0:
                    # Sets escape to True
                    escape = True
                    break

                # Checks that the correct day is inserted
                if day < 1 or day > months[month]:
                    print("\n***** You did not enter a day of the month! *****\n")
                else:
                    break

            except Exception:
                print("\n***** You did not enter a day of the month! *****\n")

        # Checks if escape equals True, then cancels method
        if escape == True:
            return
        
        # Checks if months is less tha 10, then converts it to string with 0 infront
        month_string = ""
        if month < 10:
            month_string = f"0{month}"
        else:
            month_string = str(month)

        # Checks if day is less than 10, then converts it to string with 0 infront
        day_string = ""
        if day < 10:
            day_string = f"0{day}"
        else:
            day_string = str(day)

        # Converts the date into a readable string, and the returns it
        date = f"{str(year)}-{month_string}-{day_string}"

        # Returns date
        return date

            

