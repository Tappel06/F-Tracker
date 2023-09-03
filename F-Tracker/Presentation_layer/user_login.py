'''This file contains the class that displays login and registration options'''

#=====Imports=====#
'''This section contains all the imports'''
import Presentation_layer.shared_display
from Business_Layer.database_connect import Database_Connection
from Presentation_layer.main_menu import Main_menu


#=====Classes=====#
'''This section contains all the classes'''

class User_login():
    
    def __init__(self):
        """This is the constructor,it shows the options to login or register."""

        # Establishes database connection
        self.db = Database_Connection()

        self.logo("m")
        self.print_login_register_options()
        self.login_register_options()
    

    def print_login_register_options(self):
        """This method displays the options to login or to register"""
        
        # Prints the options
        print('''
1. Login
2. Register
3. Exit''')
        

    def login_register_options(self):
        """This method contains the options to select login or register"""

        # Loops input
        while True:
            # Gets option input
            option = input("\nOption: ")

            # If option one is selected, go to Login method
            if option == "1":
                # Login method
                self.login()

            # Else if option two is selected, go to register method
            elif option == "2":
                self.register()

            # Else if option three is selcted, exit program
            elif option == "3":
                exit()

            # Else, indicate that the given option was not selected
            else:
                # Reload logo
                self.logo("m")
                # Print that a given option is not selected
                print("\n*****You have not selected a given option!*****")
                # Print options
                self.print_login_register_options()

            # Reprints logo and options
            self.logo("m")
            self.print_login_register_options()


    def login(self):
        """Takes the inputs for login, if correct, logs in the user"""
        
        # Prints logo
        self.logo("l")
        # Print escape option
        print("\nType \"E\" to return to previous menu\n")

        # Loops Login
        while True:
            # Username input
            username = input("Username: ")
            # Checks if "E" has been typed
            if username.upper() == "E":
                break

            # Password input
            password = input("Password: ")
            # Checks if "E" has been typed
            if password.upper() == "E":
                break

            # Special root
            if self.root(username, password) == True:
                break


            # Checks if user exist
            if self.db.user_authenticater(username, password) == True:
                # Login the user
                login = Main_menu(self.db.get_user_record(username, password))
                login.main_menu_options()
                break

            # prints username or password is incorrect
            else:
                # Prints logo
                self.logo("l")
                # Prints username or password is incorrect
                print("\n***** The username or password is incorrect! *****")
                # Print escape option
                print("\nType \"E\" to return to previous menu\n")



    def register(self):
        """Takes user inputs, then registers the user"""

        # Loops register
        while True:
            # E
            # Prints logo
            self.logo("r")
            # Print escape option
            print("\nType \"E\" to return to previous menu\n")

            # loop to find out if username already taken
            while True:
                # Gets username input
                username = input("What is your username: ")
                # Checks wether "E" has been entered
                if username.upper() == "E":
                    break

                if self.db.username_exists(username) == False:
                    break
                else:
                    print("*****This username is already in use, please enter another!*****")

            # Gets first_name input
            first_name = input("What is your first name: ")
            # Checks wether "E" has been entered
            if first_name.upper() == "E":
                break

            # Gets last_name input
            last_name = input("What is your last name: ")
            # Checks wether "E" has been entered
            if last_name.upper() == "E":
                break

            # password authenticated match boolean
            password_match = False

            # Password authenticate loop
            while True:

                # Gets first password
                password_1 = input("Choose your password: ")
                # Checks wether "E" has been entered
                if password_1.upper() == "E":
                    break

                # Gets second password
                password_2 = input("Please retype your password: ")
                # Checks wether "E" has been entered
                if password_2.upper() == "E":
                    break

                # If passwords do not match, print that it did not match, reloop
                if password_1 != password_2:
                    print("\n*****Your passwords did not match, please re-enter them*****\n")
                
                # Breaks the loop, and sets password_match to true
                else:
                    password_match = True
                    break
            
            # Checks wether password_match is False, then breaks the loop to exit to previous menu
            if password_match == False:
                break

            # Prints logo
            self.logo("r")
            # Prints out the details entered
            print(f'''\nYour entered details are:\n
Username: {username}
First name: {first_name}
Last name: {last_name}''')
            
            # If user registere boolean
            register = False

            while True:
                # Option if the user want to complete their registration
                complete_registration = input("\nComplete registration? (Y/N): ")

                # if "Y", turn registered to True
                if complete_registration.upper() == "Y":
                    register = True
                    break

                # Else if "N", break loop
                elif complete_registration.upper() == "N":
                    break

                # Else print that the user did not put in "Y" or "N"
                else:
                    print("*****You did not enter \"Y\" or \"N\"*****")

            # register user if "registered" is equal to True
            if register == True:
                self.db.add_user_record(username, first_name, last_name, password_1)
                break



    def logo(self, option):
        """This method generates the logo for all meus in login
        
        :param string option: Gets options "m", "l", or "r"
        """

        # Prints main login register menu
        if option == "m":
            Presentation_layer.shared_display.header()
            print('''|| Login or register ||
=======================''')
        
        # Prints register menu
        elif option == "l":
            Presentation_layer.shared_display.header()
            print('''|| Login ||
===========''')
            
        # Prints login menu
        elif option == "r":
            Presentation_layer.shared_display.header()
            print('''|| Register ||
==============''')
            

    def root(self, username, password):
        """Special admin function that opens a user list, returns True

            :param string username: reads username
            :param string password: read password

            :returns: True if rooted

            :rtype: boolean
        """
        # Checks wether both username and password equals "root"

        # Rooted boolean
        rooted = False

        if username == "root" and password == "root":
            # Sets rooted to true
            rooted = True
            # Gets user list
            user_list = self.db.get_all_users()

            Presentation_layer.shared_display.clear_console()

            print("Here is a list of all the users:\n")

            # Prints a list of all the users
            for user in user_list:
                print(f'''============================================================
User_id: {user[0]}
Username: {user[1]}
First name: {user[2]}
Last name: {user[3]}
============================================================\n''')

            # exit root
            while True:
                exit_root = input("Type \"E\" to exit root: ")
                # Checks if "E" has been typed
                if exit_root.upper() == "E":
                    break

            # Returns true
            return rooted
        
            