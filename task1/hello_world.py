# hello_world.py
# Task 1: Python Environment Setup & First Script
# This program takes user input and prints details with today's date

# Importing datetime module to get current date
import datetime

# Asking user for their name
name = input("Enter your name: ")

# Asking user for internship role
role = input("Enter your internship role: ")

# Getting today's date
today = datetime.date.today()

# Displaying the output
print("\n--- Internship Details ---")
print("Name:", name)
print("Internship Role:", role)
print("Date:", today)
