"""
Description: Generates random integers, sorts them, and reshapes into a 3x4 or 4x3 matrix.
"""

import numpy as np
# Generate 12 random integers between 1 and 100 
arr = np.random.randint(1, 100, 12)

print("Original Array:", arr)

# Sort the array
arr.sort()
print("Sorted Array:", arr)

# reshaping into 3x4 matrix
matrix = arr.reshape(3, 4)

print("Reshaped Matrix (3x4):")
print(matrix)