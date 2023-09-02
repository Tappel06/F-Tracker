'''This file serves as the main controller of the program. It checks wether all data is loaded and databases 
exist, and then starts up the program'''

#=====Imports====#
from Business_Layer.database_connect import Database_Connection
from Presentation_layer.user_login import User_login


#=====Run Program====#

# Establishes database connection
test = Database_Connection()

# Opens Login options
login = User_login()


