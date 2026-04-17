
import os

def safe_copy():
    src = input("Enter source file name: ")
    dest = input("Enter destination file name: ")

    try:
        if not os.path.exists(src):
            raise FileNotFoundError(f"Source file '{src}' does not exist.")
        
        if os.path.exists(dest):
            print(f"Error: Output file '{dest}' already exists.")
            return

        with open(src, 'r') as s_file, open(dest, 'w') as d_file:
            d_file.write(s_file.read())
        print("File copied successfully.")

    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    safe_copy()