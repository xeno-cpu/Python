#  mathematical operations on a single number
#libary 
import math
#input 
num = float(input("Enter a number: "))
#calculation 
cube = num ** 3
cube_root = num ** (1/3)
natural_log = math.log(num)
base2_log = math.log2(num)
power_of_6 = num ** 6
#display 
print(f"Cube: {cube}")
print(f"Cube Root: {cube_root}")
print(f"Natural Logarithm: {natural_log}")
print(f"Base-2 Logarithm: {base2_log}")
print(f"Number raised to the power of 6: {power_of_6}")

