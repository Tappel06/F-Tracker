'''This file contains all the code for the main menu'''

#=====Imports=====#
'''This section contains all the imports'''
from Presentation_layer.user_profile import User_profile
from Presentation_layer.expenses_menu import Expenses_menu
from Presentation_layer.income_menu import Income_menu
from Presentation_layer.budget_menu import Budget_menu
from Presentation_layer.financial_goals_menu import Financial_goals_menu

class Main_menu(User_profile):
    """Sub class of User_profile"""

    def __init__(self, user_record):
        """Constructor"""
        super().__init__(user_record)
        self.expense_menu = Expenses_menu(user_record)
        self.income_menu = Income_menu(user_record)
        self.budget_menu = Budget_menu(user_record)
        self.financial_goals_menu = Financial_goals_menu(user_record)
        

    #====Main menu methods====#
    '''Contains all the methods associated with the main menu'''

    def main_menu_options(self):
        """Takes the input of the menu options, then implements methods according to the input"""

        # Prints the logo
        self.logo("m")
        # Print income and expenses
        self.print_income_expense_totals()
        # Prints the options
        self.print_main_menu_options()
        
        # Loops option
        while True:
            # gets option input
            option = input("Option: ")

            # If option "1" selected, go to "expenses_menu_options"
            if option == "1":
                self.expense_menu.expenses_menu_options()
                # Prints the logo
                self.logo("m")
                # Print income and expenses
                self.print_income_expense_totals()
                # Prints the options
                self.print_main_menu_options()

            # Else if option "2" selected, go to "income_menu_options"
            elif option == "2":
                self.income_menu.income_menu_options()
                # Prints the logo
                self.logo("m")
                # Print income and expenses
                self.print_income_expense_totals()
                # Prints the options
                self.print_main_menu_options()

            # Else if option "3" selected, go to "budget_menu_options"
            elif option == "3":
                self.budget_menu.budget_menu_options()
                # Prints the logo
                self.logo("m")
                # Print income and expenses
                self.print_income_expense_totals()
                # Prints the options
                self.print_main_menu_options()

            # Else if option "4" selected, got to "fianacial_goals_menu_options"
            elif option == "4":
                self.financial_goals_menu.financial_goal_menu_options()
                # Prints the logo
                self.logo("m")
                # Print income and expenses
                self.print_income_expense_totals()
                # Prints the options
                self.print_main_menu_options()
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
                # Print income and expenses
                self.print_income_expense_totals()
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
        
    def print_income_expense_totals(self):
        """Prints the totals of income and expenses"""
        # Total expenses
        expenses_list = self.db.get_all_expenses_by_user_id(self.user_details[0][0])
        income_list = self.db.get_all_income_by_user_id(self.user_details[0][0])

        total_expenses = 0.00
        total_income = 0.00

        # add up all expenses
        for expense in expenses_list:
            total_expenses += expense[5]

        # add up all income
        for income in income_list:
            total_income += income[5]

        print(f'''
-----------------------------------------
| Total Income: {round(total_income, 2)}{" " * (24 - len(str(total_income)))}|
| Total Expenses: {round(total_expenses, 2)}{" " * (31 - len(str(total_expenses)))}|
|---------------------------------------|
| Balance: {round(total_income - total_expenses, 2)}{" " * (38 - len(str(total_income - total_expenses)))}|
=========================================
''')
        
