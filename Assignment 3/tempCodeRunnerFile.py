
import csv

def append_record():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll No: ")
    prog = input("Enter Program: ")
    year = input("Enter Year: ")
    grp = input("Enter Group: ")

    fieldnames = ['student_name', 'roll_no', 'program', 'year', 'group']
    
    # mode 'a' is for appending
    with open('records.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # Write header only if file is empty
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow({
            'student_name': name, 'roll_no': roll, 
            'program': prog, 'year': year, 'group': grp
        })
    print("Record added successfully.")

if __name__ == "__main__":
    append_record()