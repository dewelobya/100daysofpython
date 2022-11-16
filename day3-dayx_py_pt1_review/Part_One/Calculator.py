#Boolean values and Boolean expressions
# Please write a program which asks the user for two numbers and an operation.
# If the operation is add, multiply or subtract,
#  the program should calculate and print out the result of the operation with 
# the given numbers. 
# 2If the user types in anything else, the program should print out nothing.


number1 = int(input("Number 1:"))
number2 = int(input("Number 2:"))
choice = input("Operation:")

if choice == "add":
    print( f"{number1} + {number2} = {number1 + number2}")
 
elif choice == "subtract":
    print( f"{number1} - {number2} = {number1 - number2}")
 
elif choice == "multiply":
   print( f"{number1} * {number2} = {number1*number2}")

else:
    print(" ")
