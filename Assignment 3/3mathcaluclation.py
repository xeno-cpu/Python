'''
Description: Takes list of integers, performs operations, saves results with timestamp.
             Continues until user exits, then shows file content.
'''
from datetime import datetime

def math_logger():
    filename = "math_results.txt"
    
    while True:
        print("\n--- Math Logger ---")
        try:
            nums = input("Enter integers separated by space (or 'exit' to quit): ")
            if nums.lower() == 'exit':
                break
            
            int_list = [int(x) for x in nums.split()]
            if not int_list: continue

            # Calculations
            addition = sum(int_list)
            # Starting subtraction/division with the first element
            subtraction = int_list[0] - sum(int_list[1:])
            
            multiplication = 1
            for n in int_list: multiplication *= n
            
            division = int_list[0]
            for n in int_list[1:]: division /= n

            # Writing to file
            with open(filename, "a") as f:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                result_str = (f"Time: {timestamp} | Input: {int_list} | "
                             f"Add: {addition}, Sub: {subtraction}, "
                             f"Mul: {multiplication}, Div: {division:.2f}\n")
                f.write(result_str)
            print("Results saved.")

        except ValueError:
            print("Error: Please enter valid integers.")
        except ZeroDivisionError:
            print("Error: Division by zero encountered.")

    # Display final file content
    print("\n--- Final Formatted Log ---")
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No logs recorded.")

if __name__ == "__main__":
    math_logger()