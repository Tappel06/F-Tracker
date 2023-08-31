"""This file contains all the code for the user profile"""

#=====Imports=====#
'''This section contains all the imports for the file'''
import Presentation_layer.shared_display

#=====Classes=====#
'''This section contains all the classes'''
class User_profile():

    def __init__(self, user_record):
        # Stores user details
        self.user_details = user_record
        # Runs the main menu options
        self.main_menu_options()


    def main_menu_options(self):
        """Takes the input of the menu options, then implements functions according to the input"""

        # Prints the logo
        self.logo("m")
        # Prints the options
        self.print_main_menu_options()
        
        # Loops option
        while True:
            # gets option input
            option = input("Option: ")

            # If option "1" selected, go to "add_expense"
            if option == "1":
                pass

            # Else if option "2" selected, go to "view_expenses"
            elif option == "2":
                pass

            # Else if option "3" selected, go to "view_expenses_by_category"
            elif option == "3":
                pass

            # Else if option "4" selected, got to "add_income"
            elif option == "4":
                pass

            # Else if option "5" selected, go to "view_income"
            elif option == "5":
                pass

            # Else if option "6" selected, go to "view_income_by_category"
            elif option == "6":
                pass
            # Else if option "7" selected, go to "set_budeget_by_category"
            elif option == "7":
                pass

            # Else if option "8" selected, go to "view_budget_by_category"
            elif option == "8":
                pass

            # Else if option "9" selected, go to "set_financial_goals"
            elif option == "9":
                pass

            # Else if option "10" selected, go to "view_progress_fiancials"
            elif option == "10":
                pass

            # Else if option "11" selected, break the loop
            elif option == "11":
                break

            # Else if option "12" selected, exit
            elif option == "12":
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
1. Add expense
2. View expenses
3. View expenses by category
4. Add income
5. View income
6. View income by category
7. Set budget for a category
8. View budget for a category
9. Set financial goals
10. View progress towards financials
11. Logout
12. Exit
''')


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
        # If menu equals "m" print "main menu"
        if menu_type == "m":
            print('''||  Main Menu  ||
=================''')

