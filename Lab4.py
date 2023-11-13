for count in range(0,11):
    print(count)
for count in range(1,11):
    print(count)
for count in range(1,10,2):
    print(count)
import math
radius = float(input(' Enter radius of circle'))
print(radius)
area = math.pi * float(radius) ** 2
if area > 0:
    print(area)
else:
    print("Error: The area must be a positive number")
length = float(input('Enter length'))
width = float(input('Enter width'))
areaofrectangle = length * width
if areaofrectangle > 0:
    print(areaofrectangle)
else:
    print("Error: The area must be a positive number")