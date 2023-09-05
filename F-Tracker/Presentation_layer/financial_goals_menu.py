'''This file contains all the code for the budget menu'''

#=====Imports=====#
'''This section contains all the imports'''
from Presentation_layer.user_profile import User_profile

class Financial_goals_menu(User_profile):
    """Sub class of User_profile"""

    def __init__(self, user_record):
        """Constructor"""
        super().__init__(user_record)


    #=====Financial Goal Methods=====#
    '''Conatains all the methods related to the budget menu'''

    def financial_goal_menu_options(self):
        """Displays the options for budget"""

        # Prints logo
        self.logo("f")
       # Prints the current budget
        self.print_current_financial_goals()
        # Prints budget menu options
        self.print_financial_goal_menu_options()

        while True:
            option = input("\nOption: ")

            # If option equals "1", run "add_update_budget_category"
            if option == "1":
                self.add_financial_goal_category()
                # Prints logo
                self.logo("f")
                # Prints the current budget
                self.print_current_financial_goals()
                # Prints budget menu options
                self.print_financial_goal_menu_options()

            # If option equals "2", run "remove_budget_category"
            elif option == "2":
                self.remove_financial_goal_category()
                # Prints logo
                self.logo("b")
                # Prints the current budget
                self.print_current_financial_goals()
                # Prints budget menu options
                self.print_financial_goal_menu_options()

            # If option equals "3", run "view_financial_goal_by_category"
            elif option == "3":
                self.view_financial_goal_by_category()
                # Prints logo
                self.logo("b")
                # Prints the current budget
                self.print_current_financial_goals()
                # Prints budget menu options
                self.print_financial_goal_menu_options()

            # If option equals "4", break loop to return to previous menu
            elif option == "4":
                # Break loop
                break
            # Else print that given option was not entered
            else:
                # Prints logo
                self.logo("b")
                # Prints budget menu options
                self.print_financial_goal_menu_options()
                print("\n***** a given option was not entered! *****")


    def print_financial_goal_menu_options(self):
        """Prints the options for the budget menu"""
        print('''
1. Add/ Update financial goal category
2. Remove financial goal category
3. View financial goal by category
4. Return to previous menu''')


    def print_current_financial_goals(self):
        """Prints the current budget"""

        # Gets financial goal list
        financial_goal_list = self.db.get_all_financial_goals_by_id(self.user_details[0][0])

        print("\nYour current financial goals:")
        print(f''' Goal:{" " * 34}Goal reached:{ " " *15}Goal amount:
--------------------------------------------------------------------------------''')
        
        # Total expense saved
        expense_total = 0.00
        # Financial goal total
        budget_total = 0.00

        
        for budget in financial_goal_list:
            # gets the sum of an category expense
            sum = self.db.get_expense_sum_of_category_and_id(self.user_details[0][0], budget[2])

            # Add up the total sum expense
            if sum[0] != None:
                expense_total += sum[0]
            
            # Add up financial goal total
            budget_total += budget[3]

            # Prints financial goals
            print(f''' {budget[2]}{" " * (39 - len(budget[2]))}{sum[0]}{" " * (28 - len(str(sum[0])))}{budget[3]}''')
    
        # prints total of expenses and financial goal
        print(f'''--------------------------------------------------------------------------------
{" " * 24}Total expenses: {round(expense_total, 2)}{" " * (14 - len(str(expense_total)))}Budget total: {round(budget_total, 2)}   
================================================================================''')


    def add_financial_goal_category(self):
        """Adds or update new financial goal category"""

        # Gets a  list of current financial goal categories
        list = self.db.get_all_financial_goals_by_id(self.user_details[0][0])

        # Prints logo
        self.logo("f")

        while True:
            # Prints instructions
            print("\nSelect a financial goal to update, or add a new one:\n")

            # Index number to be assigned
            index = 1
            # Prints options for update
            for a in list:
                print(f"{index}. {a[2]}")
                index += 1
            # Prints add category option
            print(f"\n{len(list)+1}. Add Category")
            # Prints return to previous menu option
            print(f"{len(list)+2}. Return to previous menu")
            
            # Gets option input
            option = input("\nOption: ")

            try:
                # checks if option can be casted to in
                if int(option):
                    # if options are in range of the list length
                    if int(option) > 0 and int(option) <= len(list):
                        # loop check if the one of the categories have been selected
                        for a in range(len(list)):
                            # Checks if op matches with option - 1
                            if a == (int(option)-1):
                                # Prints logo
                                self.logo("f")

                                # loop
                                while True:
                                    # get update amount
                                    try:
                                        update_amount = int(input(f"\nWhat is the new goal amount for {list[a][2]}: "))
                                        self.db.update_financial_goal_record(self.user_details[0][0], list[a][2], update_amount)
                                        # Print logo
                                        self.logo("f")
                                        break
                                    except Exception:
                                        # Print logo
                                        self.logo("f")
                                        print("\n***** You did not enter an amount! *****")
                                break
                            

                    # Else if option is one more than list length, add category
                    elif int(option) == (len(list) + 1):
                        # Prints logo 
                        self.logo("f")
                        # Input for new category
                        new_category = input("\nEnter your new goal category: ")
                        goal_amount = input("Enter the goal amount: ")
                        self.db.add_financial_goals_record_and_maybe_expense_record(self.user_details[0][0],
                                                                                    new_category,
                                                                                    goal_amount)
                        # updates list
                        list = self.db.get_all_financial_goals_by_id(self.user_details[0][0])
                        # Prints logo 
                        #self.logo("f")

                    # Else if option is two more than list length, break loop to go to previous menu
                    elif int(option) == (len(list) + 2):
                        break

                    # Else, print given option not inserted
                    else:
                        print("\n***** You did not enter a given option! *****")

            except Exception:
                print("\n***** You did not enter a given option! *****")


    def remove_financial_goal_category(self):
        """Removes a financial goal category"""

        # Prints logo
        self.logo("f")

        # Loads all expense categories
        goal_categories = self.db.get_all_financial_goals_by_id(self.user_details[0][0])

        print("\nChoose a category you want to remove (Enter \"E\" to escape): \n")

        while True:
            # assign category option number
            cat_num = 1
            # Print the categories available
            for cat in goal_categories:
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
                    if int(option) > 0 and int(option) <= len(goal_categories):
                        # for loop
                        for op in range(len(goal_categories)):
                            # Checks if op matches with option - 1
                            if op == (int(option)-1):
                                # Deletes record
                                self.db.delete_financial_goal_record_by_category_and_user_id(self.user_details[0][0], cat[2])
                                # Prints Logo
                                self.logo("f")
                                break
                        break
            
            except Exception: 
                # Print logo
                self.logo("f")
                print("\n***** You did not insert a given option! *****\n")


    def view_financial_goal_by_category(self):
        """Views financial goal by category"""
        
        # Print logo
        self.logo("f")
        
        while True:
            # Search category
            search = input("\nEnter the financial goal category you want to view (Enter \"E\" to cancel): ")

            # Checks wether "E" has been entered, breaks loop if so
            if search.upper() == "E":
                break
            
            # Print logo
            self.logo("f")
            # Print searched
            self.print_searched_financial_goal(search)


    def print_searched_financial_goal(self, category_search):
        """Prints the current financial goals
        
            :param string category_search: uses the input to search for category
        """

        # Gets budget list
        goal_list = self.db.get_all_financial_goals_by_id(self.user_details[0][0])

        print("\nYour current financial goals:")
        print(f''' Goal:{" " * 34}Goal reached:{ " " *15}Goal amount:
--------------------------------------------------------------------------------''')
        
        # Total expense of expenses
        expense_total = 0.00
        # Total financial goal
        goal_total = 0.00

        
        for g in goal_list:
            # gets the sum of an category expense
            sum = self.db.get_expense_sum_of_category_and_id(self.user_details[0][0], g[2])

            # Add up the total sum expense
            if sum[0] != None:
                expense_total += sum[0]
            
            # Add up budget total
            goal_total += g[3]

            # Prints budget
            print(f''' {g[2]}{" " * (39 - len(g[2]))}{sum[0]}{" " * (28 - len(str(sum[0])))}{g[3]}''')
    
        # prints total of expenses and financial goal
        print(f'''--------------------------------------------------------------------------------
{" " * 24}Total expenses: {round(expense_total, 2)}{" " * (14 - len(str(expense_total)))}Budget total: {round(goal_total, 2)}   
================================================================================''')

            