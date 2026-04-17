'''
Description: Generates a NumPy array and calculates the total sum, 
mean, maximum, and minimum values.
'''
import numpy as np

def array_stats():
    # Generate array [cite: 57]
    data = np.array([10, 20, 30, 40, 50])
    
    # Calculate operations [cite: 58]
    total_sum = np.sum(data)
    mean_val = np.mean(data)
    max_val = np.max(data)
    min_val = np.min(data)
    
    print(f"Array: {data}")
    print(f"Total Sum: {total_sum}")
    print(f"Mean Value: {mean_val}")
    print(f"Smallest Value: {min_val}")
    print(f"Largest Value: {max_val}")

if __name__ == "__main__":
    array_stats()