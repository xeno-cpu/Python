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

num1=list(set(num))
num1.sort(reverse = False)
print(num1)
