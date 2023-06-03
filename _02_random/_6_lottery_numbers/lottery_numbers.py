import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    r1 = random.randint(0, 9)
    r2 = random.randint(0, 9)
    r3 = random.randint(0, 9)
    r4 = random.randint(0, 9)
    r5 = random.randint(0, 9)
    r6 = random.randint(0, 9)
    # TODO 2) Display the selected numbers to the user in a pop-up
    messagebox.showinfo(title="Lottery Ticket", message="Your lottery ticket numbers are: " + str(r1) + " " + str(r2) + " " +
    str(r3) + " " + str(r4) + " " + str(r5) + " " + str(r6))
    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
