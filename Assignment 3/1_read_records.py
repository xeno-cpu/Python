'''
Description: Reads a CSV file "records.csv" and displays student details 
             (student_name, roll_no, program, year, group).
'''
import csv
def read_records():
    try:
        with open('records.csv', mode='r') as file:
            reader = csv.DictReader(file)
            print(f"{'Name':<20} {'Roll':<10} {'Program':<15} {'Year':<10} {'Group'}")
            print("-" * 65)
            for row in reader:
                print(f"{row['student_name']:<20} {row['roll_no']:<10} "
                      f"{row['program']:<15} {row['year']:<10} {row['group']}")
    except FileNotFoundError:
        print("Error: 'records.csv' not found. Please create the file first.")
if __name__ == "__main__":
    read_records()