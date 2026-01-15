# Import datetime module to work with dates
import datetime

# Ask the user to enter their name
name = input("Enter your name: ")

# Ask the user to enter their internship role
role = input("Enter your internship role: ")

# Store today's date
today_date = datetime.date.today()

# Print a separator line
print("\n----------------------------")

# Display intern details in a clean format
print("INTERN DETAILS")
print("----------------------------")
print("Name            :", name)
print("Internship Role :", role)
print("Date            :", today_date)

# Print ending line
print("----------------------------")
