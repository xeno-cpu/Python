import random 

def guess_the_dice():
    dice = [1, 2, 3, 4, 5, 6]
    target = random.choice(dice)

    try:
        a = int(input("Roll your dice .Guess the outcome \n >"))
    except ValueError:
        print("(;﹏;)")
        return

    difference = abs(a - target)

    if difference == 0:
        print("(^_^)")
    elif difference == 1:
        print("((-_-))")
    else:
        print("(;﹏;)")

def main():
    guess_the_dice()

if __name__ == "__main__":
    main()