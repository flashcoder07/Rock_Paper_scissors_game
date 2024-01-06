import random

def play():
    sign = input("'r' for rock 'p' for paper 's' for scissors")
    comp = random.choice(['r', 'p', 's'])
    if sign == comp:
        print("tie")
    elif (sign == "r" and comp == "s") or (sign == "s" and comp == "p") or (sign == "p" and comp == "r"):
        print("user win")
    else:
        print("i win")
    print(f"mine was {comp}")





play()

