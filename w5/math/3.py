import math

n = int(input("number of sides: "))
s = float(input("length if side: "))

area = (n * s**2) / (4 * math.tan(math.pi / n))
print("area of the polygon is: ", round(area, 2))