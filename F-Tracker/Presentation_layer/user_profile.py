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


    #=====Shared Methods=====#
    '''Contains all the methods shared among the other sub classes'''

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
            
        # If menu equals "b" print "Budget Menu"
        elif menu_type == "b":
            print('''||  Budget Menu  ||
===================''')
            
        # If menu equals "f" print "Financial Goals Menu"
        elif menu_type == "f":
            print('''||  Financial Goals Menu  ||
============================''')
            

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

            

