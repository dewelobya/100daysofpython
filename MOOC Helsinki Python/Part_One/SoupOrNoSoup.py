# This is a program which asks for the user's name. 
# If the name is anything but "Jerry", 
# the program then asks for the number of portions and 
# prints out the total cost. The price of a single portion is 5.90.

name = input("Please tell me your name: ")
if name != "Jerry":
    soup = int (input("How many portions of soup? "))
    print(f"The total cost is { soup * 5.90}")
print ("Next please!")