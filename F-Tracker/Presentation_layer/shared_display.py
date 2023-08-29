'''This file contains all the functions shared with other files, cocerning with display printouts'''

#=====Imports=====#
'''This section contains all the imports'''
import os


#=====Functions=====#
'''This section contains all the functions'''

def logo():
    """This function prints out the logo"""
    print('''   _____        _______   _____                ___             _____   _____
  |                |     |     \      /\      /      |    /   |       |     \\
  |_____   ____    |     |_____/     /  \    /       |___/    |_____  |_____/
  |                |     |     \    /----\   \       |   \    |       |     \\
  |                |     |      \  /      \   \___   |    \   |_____  |      \\
================================================================================''')


def clear_console():
    """This function clears the console"""
    os.system("cls||clear")

def header():
    """This function clears the console, and prints the logo"""
    clear_console()
    logo()