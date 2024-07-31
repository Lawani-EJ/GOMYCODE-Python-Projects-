# #  To create a calculator app that can perform basic arithmetic operations.
# operation = input("Enter Your Operator: ")
# number_1 = int(input("Enter Your first number: "))
# number_2 = int(input("Enter Your second number: "))

# if operation == "+":
#     result = number_1+number_2
#     print(result)
# elif operation == "-":
#     result = number_1 - number_2
#     print(result)
# elif operation == "/":
#     result = number_1 / number_2
#     print(result)
# elif operation == "*":
#     result = number_1*number_2
#     print(result)
# else:
#     print(f"{operation} This value you have entered is not a valid operator please try again.")

def calculator(num1,num2):
        operation = input("Enter Your Operator: ")
        if operation == "+":
            result = num1+num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "/":
            if num2 == 0:
                print("Error: O division is not allowed")
            else:
                result = num1 / num2
        elif operation == "*":
            result = num1*num2
        else:
                print(f"{operation} This value you have entered is not a valid operator please try again.")
        return result

num1 = int(input("Enter Your first number: "))
num2 = int(input("Enter Your second number: "))

result = calculator(num1,num2)
print(result)