'''
 Takes student details from user and appends to "records.csv". Author: Your Name
'''
class Learner:
    def __init__(self, roll_no, full_name, enrollment_year, program, group):
        self.roll_no = roll_no
        self.full_name = full_name
        self.enrollment_year = enrollment_year
        self.program = program
        self.group = group

    def display_details(self):
        print("\n--- Learner Details ---")
        for attr, value in self.__dict__.items():
            print(f"{attr.replace('_', ' ').title()}: {value}")

def main():
    r = input("Roll No: ")
    n = input("Full Name: ")
    y = input("Enrollment Year: ")
    p = input("Program: ")
    g = input("Group: ")
    
    student = Learner(r, n, y, p, g)
    student.display_details()

if __name__ == "__main__":
    main()