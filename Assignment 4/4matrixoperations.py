'''
Description: Inputs two matrices and performs addition, subtraction, and multiplication with basic dimension checking.
'''
import numpy as np

def matrix_arithmetic():
    try:
        # taking simple input
        mat_a = np.array([[int(x) for x in input("Enter Matrix A (row): ").split()],
                          [int(x) for x in input().split()]])
        
        mat_b = np.array([[int(x) for x in input("Enter Matrix B (row): ").split()],
                          [int(x) for x in input().split()]])

        # checking for addition/subtraction
        if mat_a.shape == mat_b.shape:
            print("Addition:\n", mat_a + mat_b)
            print("Subtraction:\n", mat_a - mat_b)
        else:
            print("Addition/Subtraction not possible")

        # checking for multiplication
        if mat_a.shape[1] == mat_b.shape[0]:
            print("Multiplication:\n", np.dot(mat_a, mat_b))
        else:
            print("Multiplication not possible")

    except:
        print("Error in matrix input")

if __name__ == "__main__":
    matrix_arithmetic()