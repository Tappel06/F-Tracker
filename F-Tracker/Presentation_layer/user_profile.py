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
                pass

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
                self.db.close_database()
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
                pass

            # Else if option equals "2", run "view_expense"
            elif option == "2":
                pass

            # Else if option equals "3", run "view_expense_by_category"
            elif option == "3":
                pass

            # Else if option equals "4", run "add_remove_expense_category"
            elif option == "4":
                self.add_remove_expense_category()

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
                pass

            # if option equals "3", break loop to go to previous menu
            elif option == "3":
                break

            # else print that an option is not selected
            else:
                print("\n***** You did not enter a given option! *****")


    def add_expense_category(self):
        """Adds a new expense category"""

        # Prints type "E" to cancel current procedure
        print("\nType \"E\" to cancel")

        # loops questions
        while True: 
            category_name = input("What is the name of your new expense: ")
            # Checks if "E" is typed
            if category_name.upper() == "E":
                break
            elif category_name != "":
                self.db.create_new_expense_category(self.user_details[0][0], category_name)
            else:
                print("*****You did not type anything*****")


    def print_add_remove_expense_category_options(self):
        """Prints the options add or remove category"""
        print('''
1. Add category
2. Remove Category
3. Previous menu''')


    def print_expense_categories(self):
        """Prints out all the expense categories under user's id"""
        # Gets a list of all the expense categories under this user's id
        categories = self.db.get_all_expense_categories(self.user_details[0][0])

        print("Expense categories: \n")

        # Prints each category
        for category in categories:
            print(category[3])


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
=================''')

