logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

# Created function to operate the addition, subtraction, multiplication, division
# Mentioned the inputs number 1 nad number 2 as n1 and n2 respectively

def add(n1, n2):
    return  n1 + n2

def subtract(n1, n2):
    return  n1 - n2

def multiply(n1, n2):
    return  n1 * n2

def divide(n1,n2):
    return  n1 / n2


#Created the main calculator project

def cal_project():

    #print the logo

    print(logo)

    # Ask the user for first number

    num1 = float(input("What's the first number?: "))

    # Operators array or list of operators

    operators = ["+", "-", "*", "/"]

    # Continue the calculation process by loop mode till user type 'NO'.

    python_calci = False
    while not python_calci:

        #display the operator symbols
        for i in operators:
            print(i)

        user_operation = input("Pick an operation: ")
        num2 = float(input("what's the next number?: "))

        symbols_value = {
            "+" : add(num1, num2),
            "-" : subtract(num1, num2),
            "*" : multiply(num1, num2),
            "/" : divide(num1, num2)
        }
         
        # Return the function by calling the dictionary 
        
        calculation = symbols_value[user_operation]
        

        print(f"{num1} {user_operation} {num2} = {calculation}")

        continue_calculation = input(f"Type 'y' to continue calculating with {calculation}, or type 'n' to start a new calculation:").lower()

        if continue_calculation == "y":
            num1 = calculation

        else:
            python_calci = True
            print("\n" * 20)
            cal_project()


cal_project()
