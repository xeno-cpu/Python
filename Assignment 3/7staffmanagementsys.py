
import csv

class Staff:
    def __init__(self, emp_id, name, addr, phone, status, deps, salary):
        self.data = [emp_id, name, addr, phone, status, deps, salary]

def manage_staff():
    filename = "staff.csv"
    while True:
        choice = input("\n1. Add Staff\n2. View Staff\n3. Exit\nSelect: ")
        
        try:
            if choice == '1':
                s = Staff(input("ID: "), input("Name: "), input("Address: "), 
                          input("Phone: "), input("Status: "), 
                          input("Dependents: "), input("Salary: "))
                with open(filename, 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(s.data)
            elif choice == '2':
                with open(filename, 'r') as f:
                    reader = csv.reader(f)
                    for row in reader: print(row)
            elif choice == '3':
                break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    manage_staff()