# datatypes_demo.py
# Task 2: Demonstration of Python Data Types and Operations

# 1. Declaring variables of different data types
integer_var = 10            # int type
float_var = 25.5            # float type
string_var = "Python"       # string type
boolean_var = True          # boolean type

# 2. Printing the type of each variable
print("Data Types:")
print("integer_var:", type(integer_var))
print("float_var:", type(float_var))
print("string_var:", type(string_var))
print("boolean_var:", type(boolean_var))

# 3. Performing arithmetic operations
sum_result = integer_var + float_var
product_result = integer_var * float_var

print("\nArithmetic Operations:")
print("Sum:", sum_result)
print("Product:", product_result)

# 4. Taking string input from user
user_input = input("\nEnter a number: ")

# 5 & 6. Type casting with error handling
try:
    int_value = int(user_input)        # converting string to integer
    float_value = float(user_input)    # converting string to float

    print("Integer value:", int_value)
    print("Float value:", float_value)

except ValueError:
    print("Invalid input! Please enter a numeric value.")

# 7. Concatenating strings and numbers properly
age = 20
message = "My age is " + str(age)   # converting number to string
print("\nString Concatenation:")
print(message)

# 8. Demonstrating dynamic typing
value = 100          # initially integer
print("\nDynamic Typing Example:")
print("Value:", value, "| Type:", type(value))

value = "Now a string"   # reassigned as string
print("Value:", value, "| Type:", type(value))
