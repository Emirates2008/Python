import math
print("Tell me the first side , and the second side of your triangle, and using the pythagorean theorem, I will find the hypotenuse.")
a = float(input("Choose the first side of your triangle."))
b = float(input("Choose the second side of your triangle."))
c = (a * a) + (b * b)
print(math.sqrt(c))
