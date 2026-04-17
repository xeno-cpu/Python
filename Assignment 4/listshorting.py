'''
Description: Takes 12 user-input numbers, sorts the list, 
and extracts specific index slices.
'''
def list_operations():
    try:
        # Input 12 elements [cite: 59]
        user_input = input("Enter 12 numbers separated by spaces: ")
        num_list = [float(x) for x in user_input.split()]
        
        if len(num_list) < 12:
            print("Error: Please enter at least 12 numbers.")
            return

        # Sort and Slice [cite: 60]
        num_list.sort()
        print(f"Sorted List: {num_list}")
        print(f"Slice 3-6: {num_list[3:6]}")
        print(f"Slice 6-9: {num_list[6:9]}")
        print(f"Slice 4-10: {num_list[4:10]}")
        
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    list_operations()