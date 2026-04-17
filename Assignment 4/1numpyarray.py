'''
Description: Creates a NumPy array [10, 20, 30, 40, 50] and performs sum, mean, max, and min operations.
'''
import numpy as np

def array_stats():
    # Generate array [cite: 57]
    arr = np.array([10, 20, 30, 40, 50])

    print("Original Array:", arr)

    # Calculate operations [cite: 58]
    total_sum = np.sum(arr)
    mean_val = np.mean(arr)
    max_val = np.max(arr)
    min_val = np.min(arr)
    
    print(f"Array: {arr}")
    print(f"Total Sum: {total_sum}")
    print(f"Mean Value: {mean_val}")
    print(f"Smallest Value: {min_val}")
    print(f"Largest Value: {max_val}")

if __name__ == "__main__":
    array_stats()