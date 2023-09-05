'''This file contains all the code for the budget menu'''

#=====Imports=====#
'''This section contains all the imports'''
from Presentation_layer.user_profile import User_profile

class Budget_menu(User_profile):
    """Sub class of User_profile"""

    def __init__(self, user_record):
        """Constructor"""
        super().__init__(user_record)

    
    #=====Budget Menu Methods=====#
    '''Conatains all the methods related to the budget menu'''

    def budget_menu_options(self):
        """Displays the options for budget"""

        # Prints logo
        self.logo("b")
        # Prints the current budget
        self.print_current_budget()
        # Prints budget menu options
        self.print_budget_menu_options()

        while True:
            option = input("\nOption: ")

            # If option equals "1", run "add_update_budget_category"
            if option == "1":
                self.add_update_budget_category()
                # Prints logo
                self.logo("b")
                # Prints the current budget
                self.print_current_budget()
                # Prints budget menu options
                self.print_budget_menu_options()

            # If option equals "2", run "remove_budget_category"
            elif option == "2":
                self.remove_budget_category()
                # Prints logo
                self.logo("b")
                # Prints the current budget
                self.print_current_budget()
                # Prints budget menu options
                self.print_budget_menu_options()

            # If option equals "3", run "view_budget_by_category"
            elif option == "3":
                self.view_budget_by_category()
                # Prints logo
                self.logo("b")
                # Prints the current budget
                self.print_current_budget()
                # Prints budget menu options
                self.print_budget_menu_options()

            # If option equals "4", break loop to return to previous menu
            elif option == "4":
                # Break loop
                break
            # Else print that given option was not entered
            else:
                # Prints logo
                self.logo("b")
                # Prints budget menu options
                self.print_budget_menu_options()
                print("\n***** a given option was not entered! *****")


    def print_budget_menu_options(self):
        """Prints the options for the budget menu"""
        print('''
1. Add/ Update budget category
2. Remove budget category
3. View budget by category
4. Return to previous menu''')


    def print_current_budget(self):
        """Prints the current budget"""

        # Gets budget list
        budget_list = self.db.get_all_budget_by_id(self.user_details[0][0])

        print("\nYour current budget and their expenses:\n")
        print(f''' Category{" " * 26}Current Expense:{" " * 15}Expense Budget
--------------------------------------------------------------------------------''')
        
        # Total expense of expenses
        expense_total = 0.00
        # Total budget of all budgets
        budget_total = 0.00

        
        for budget in budget_list:
            # gets the sum of an category expense
            sum = self.db.get_expense_sum_of_category_and_id(self.user_details[0][0], budget[2])

            # Add up the total sum expense
            if sum[0] != None:
                expense_total += sum[0]
            
            # Add up budget total
            budget_total += budget[3]

            # Prints budget
            print(f''' {budget[2]}{" " * (34 - len(budget[2]))}{sum[0]}{" " * (31 - len(str(sum[0])))}{budget[3]}''')
    
        # prints total of expenses and budget
        print(f'''--------------------------------------------------------------------------------
{" " * 19}Total expenses: {round(expense_total, 2)}{" " * 9}Budget total: {round(budget_total, 2)}   
================================================================================''')


    def add_update_budget_category(self):
        """Checks wether a category has been added, if a category is added, then update it
        else, just add new category"""

        # Prints logo
        self.logo("b")

        # Loads all expense categories
        expense_categories = self.db.get_all_expense_categories(self.user_details[0][0])

        print("\nChoose a category you want to add or update (Enter \"E\" to escape): \n")

        while True:
            # assign category option number
            cat_num = 1
            # Print the categories available
            for cat in expense_categories:
                print(f"{cat_num}. {cat[3]}")
                cat_num += 1

            # Gets option input
            option = input("\nOption: ")
            # Checks if "E" has been entered, breaks loop to exit
            if option.upper() == "E":
                break
            
            try:
                # Checks if option can be casted to int, if not print incorrect option chosen
                if int(option):
                    # Check that the options are not less than one, or more than expense_category length
                    if int(option) > 0 and int(option) <= len(expense_categories):
                        # for loop
                        for op in range(len(expense_categories)):
                            # Checks if op matches with option - 1
                            if op == (int(option)-1):
                                # Checks if the budget category exists, if it exists, then update, else add
                                if self.db.budget_category_exists(expense_categories[op][3], self.user_details[0][0]):

                                    # Prints logo
                                    self.logo("b")
                                    
                                    while True:
                                        try:
                                            # Takes budget amount input
                                            new_budget_amount = float(input(f"\nInsert the new budget amount for {expense_categories[op][3]}: "))
                                            break
                                        except Exception:
                                            # Prints logo
                                            self.logo("b")
                                            print("\n***** You did not enter an amount! *****")
                                    
                                    # Updates new budget amount
                                    self.db.update_budget_record(self.user_details[0][0], expense_categories[op][3], new_budget_amount)
                                    break
                                else:
                                    # Prints logo
                                    self.logo("b")

                                    while True:
                                        try:
                                            # Takes budget amount input
                                            budget_amount = float(input(f"\nInsert a budget amount for {expense_categories[op][3]}: "))
                                            break
                                        except Exception:
                                            # Prints logo
                                            self.logo("b")
                                            print("\n***** You did not enter an amount! *****")

                                    # Adds new budget record
                                    self.db.add_budget_record(self.user_details[0][0], expense_categories[op][3], budget_amount)
                                    break
                        # Prints logo
                        self.logo("b")       
                        break
                            
            except Exception: 
                # Print logo
                self.logo("b")
                print("\n***** You did not insert a given option! *****\n")
        

    def remove_budget_category(self):
        """Removes a budget category"""

        # Prints logo
        self.logo("b")

        # Loads all expense categories
        budget_categories = self.db.get_all_budget_categories_by_user_id(self.user_details[0][0])

        print("\nChoose a category you want to remove (Enter \"E\" to escape): \n")

        while True:
            # assign category option number
            cat_num = 1
            # Print the categories available
            for cat in budget_categories:
                print(f"{cat_num}. {cat[2]}")
                cat_num += 1

            # Gets option input
            option = input("\nOption: ")
            # Checks if "E" has been entered, breaks loop to exit
            if option.upper() == "E":
                break

            try:
                # Checks if option can be casted to int, if not print incorrect option chosen
                if int(option):
                    # Check that the options are not less than one, or more than expense_category length
                    if int(option) > 0 and int(option) <= len(budget_categories):
                        # for loop
                        for op in range(len(budget_categories)):
                            # Checks if op matches with option - 1
                            if op == (int(option)-1):
                                # Deletes record
                                self.db.delete_budget_record_by_category_and_user_id(self.user_details[0][0], cat[2])
                                break
                        break
            
            except Exception: 
                # Print logo
                self.logo("b")
                print("\n***** You did not insert a given option! *****\n")

    def view_budget_by_category(self):
        """Views budget by category"""
        
        # Print logo
        self.logo("b")
        
        while True:
            # Search category
            search = input("\nEnter the budget category you want to view (Enter \"E\" to cancel): ")

            # Checks wether "E" has been entered, breaks loop if so
            if search.upper() == "E":
                break
            
            # Print logo
            self.logo("b")
            # Print searched
            self.print_searched_budget(search)


    def print_searched_budget(self, category_search):
        """Prints the current budget
        
            :param string category_search: uses the input to search for category
        """

        # Gets budget list
        budget_list = self.db.get_all_budget_by_user_id_and_category(self.user_details[0][0], category_search)

        print("\nYour current budget and their expenses:\n")
        print(f''' Category{" " * 26}Current Expense:{" " * 15}Expense Budget
--------------------------------------------------------------------------------''')
        
        # Total expense of expenses
        expense_total = 0.00
        # Total budget of all budgets
        budget_total = 0.00

        
        for budget in budget_list:
            # gets the sum of an category expense
            sum = self.db.get_expense_sum_of_category_and_id(self.user_details[0][0], budget[2])

            # Add up the total sum expense
            if sum[0] != None:
                expense_total += sum[0]
            
            # Add up budget total
            budget_total += budget[3]

            # Prints budget
            print(f''' {budget[2]}{" " * (34 - len(budget[2]))}{sum[0]}{" " * (31 - len(str(sum[0])))}{budget[3]}''')
    
        # prints total of expenses and budget
        print(f'''--------------------------------------------------------------------------------
{" " * 19}Total expenses: {round(expense_total, 2)}{" " * 9}Budget total: {round(budget_total, 2)}   
================================================================================''')