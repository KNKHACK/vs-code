# write a simple Python program that adds two numbers   
def add_numbers(num1, num2):
    return num1 + num2

# Get user input
try:
    user_num1 = float(input("Enter the first number: "))
    user_num2 = float(input("Enter the second number: "))
    result = add_numbers(user_num1, user_num2)
    print(f"The sum of {user_num1} and {user_num2} is: {result}")
except ValueError:
    print("Invalid input. Please enter numeric values.")      
# End of main.py    