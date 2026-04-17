num = []
def get_input():# input function 
    print("Enter names of the students (or q to quit) :")
    while True:
        urs_inp = input("> ") 
        if urs_inp.lower() == 'q':
            break

        try:
            val = str(urs_inp)
            num.append(val)
        except ValueError:
            print("Please enter a valid integer.")

get_input()

num.sort(key=str.lower, reverse =True)

print(f"The name in reverse order is :\n {num}")
