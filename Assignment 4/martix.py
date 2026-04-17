'''
Description: Inputs two matrices and performs addition, subtraction, 
and multiplication with dimension validation.
'''
import numpy as np

def matrix_arithmetic():
    try:
        # Example 2x2 matrices
        mat_a = np.array([[1, 2], [3, 4]])
        mat_b = np.array([[5, 6], [7, 8]])
        
        # Validation and Operations 
        if mat_a.shape != mat_b.shape:
            raise ValueError("Dimensions mismatched for addition/subtraction.")
        
        print("Addition:\n", np.add(mat_a, mat_b))
        print("Subtraction:\n", np.subtract(mat_a, mat_b))
        print("Multiplication (Dot Product):\n", np.dot(mat_a, mat_b))
        
    except ValueError as e:
        print(f"Matrix Error: {e}")

if __name__ == "__main__":
    matrix_arithmetic()