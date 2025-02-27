import time
import math

number = int(input("Sample Input:"))
delay = int(input("Sample Output:"))

time.sleep(delay / 1000)  
sqrt_result = math.sqrt(number)  

print(f"Square root of {number} after {delay} miliseconds is {sqrt_result}")