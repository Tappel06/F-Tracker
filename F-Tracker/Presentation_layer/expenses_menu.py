'''This file contains all the code for the expenses menu'''

#=====Imports=====#
'''This section contains all the imports'''
from Presentation_layer.user_profile import User_profile

class Expenses_menu(User_profile):
    """Sub class of User_profile"""

    def __init__(self, user_record):
        """Constructor"""
        super().__init__(user_record)


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
        print(f'''\n Transaction Id:{" " * 4}Date:{" " * 10}Category:{" " * 26}Amount:
--------------------------------------------------------------------------------''')
        
        for expense in expense_list:
            # adds up the total amount of expenses
            total_amount += expense[5]
            # Prints Expenses
            print(f''' {expense[0]}{" " * (19 - len(str(expense[0])))}{expense[2]}{" " * 5}{expense[4]}{" " * (35 - len(expense[4]))}{expense[5]}
--------------------------------------------------------------------------------''')
            
        # prints the total expenses
        print(f'''================================================================================
{" " * 55}Expense Total: {round(total_amount, 2)}
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
        print(f'''\n Transaction Id:{" " * 4}Date:{" " * 10}Category:{" " * 26}Amount:
--------------------------------------------------------------------------------''')

        for expense in category_list:
            # adds up the total amount of expenses
            total_amount += expense[5]
            # Prints Expenses
            print(f''' {expense[0]}{" " * (19 - len(str(expense[0])))}{expense[2]}{" " * 5}{expense[4]}{" " * (35 - len(expense[4]))}{expense[5]}
--------------------------------------------------------------------------------''')
            
        # prints the total expenses
        print(f'''================================================================================
{" " * 55}Expense Total: {round(total_amount, 2)}
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