
num = []

def get_input():# input function 
    print("Enter integers (or q to quit) :")
    while True:
        urs_inp = input("> ") 
        if urs_inp.lower() == 'q':
            break

        try:
            val = int(urs_inp)
            num.append(val)
        except ValueError:
            print("Please enter a valid integer.")

get_input()


print("\nChecking for Armstrong numbers...")

for n in num:
    digits = str(n)
    power = len(digits)
    
    total = sum(int(d) ** power for d in digits)
        
    if total == n:
        print(f"{n} is an Armstrong number.")
    else:
        print(f"{n} is not an Armstrong number.")

