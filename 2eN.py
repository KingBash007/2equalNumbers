# Program to check if user input numbers are equal without using any comparison operator
def checkifsame(number1, number2):
    if((number1^number2)!=0):
        print("numbers are not equal")
    else:
        print("both numbers are equal")
# Taking input
number1 = int(input("Enter the first number to compare:"))
number2 = int(input("Enter the second number to compare:"))
checkifsame(number1, number2)            