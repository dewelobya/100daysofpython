# Fix the program
number = int(input("Please type in a number:"))
value = number - 100


if number >= 100:
  print(f"The number was greater than one hundred")
  print(f"Now its value has decreased by one hundred")
  print(f"Its value is now {value}")
  print(f"{value} must be my lucky number!")
  print(f"Have a nice day!")
else:
  print(f"{number} must be my lucky number!")
  print(f"Have a nice day!")
