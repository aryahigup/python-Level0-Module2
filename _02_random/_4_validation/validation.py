import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    random_number = random.randint(1, 5)



    # TODO 1) Use each value of random_number to give the user a random compliment
    def check_num():
        random_number = random.randint(1, 5)
        print(random_number)
        if random_number == 1:
            print("You are very smart")
        elif random_number == 2:
            print("You have a kind smile")
        elif random_number == 3:
            print("You are a great person")
        elif random_number == 4:
            print("Your outfit is great")
        elif random_number == 5:
            print("You are a great programmer")

    # TODO 2) Repeat all the code above 10 times
    for i in range(10):
        check_num()
    # TODO 3) Find someone to test out your program. They will like it :)
