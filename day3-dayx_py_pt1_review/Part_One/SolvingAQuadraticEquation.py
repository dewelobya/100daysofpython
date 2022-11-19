# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5


a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))

# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

# calculate the discriminant
x = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(x))/(2*a)
sol2 = (-b+cmath.sqrt(x))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))