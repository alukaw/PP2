#Task1

import math
degree = int(input())
radian = degree * (math.pi / 180)
print(radian)

#Task2

height = int(input())
base = int(input())
top = int(input())
area = ((base + top)/2) * height
print(area)

#Task3

n = int(input())
s = float(input())
area_polygon = (n * s ** 2) / (4 * math.pi / n)
print(round(area_polygon, 2))

#Task4

b = int(input())
h = int(input())
area_parallelogram = b * h
print(area_parallelogram)
