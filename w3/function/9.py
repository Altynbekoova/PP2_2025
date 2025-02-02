# v = 4/3 p * r^3
import math

def volume(r):
    return 4/3 * math.pi * r**3

r = int(input())
print(volume(r))