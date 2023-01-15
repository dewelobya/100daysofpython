#Program which estimates a user's typical food expenditure.


times = float(input("How many times a week do you eat at the student cafeteria?"))
price = float(input("The price of a typical student lunch?"))
money = float(input("How much money do you spend on groceries in a week?"))

avgD = (times*price)/7 + (money/7)
avgW = times*price + money

print(f"Average food expenditure:")
print(f"Daily: {avgD} euros")
print(f"Weekly: {avgW} euros")

