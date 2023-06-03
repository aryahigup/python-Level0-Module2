import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer

    # Make a variable and initialize it to a random number between 0 and 3
    rand_num = random.randint(0,3)
    # If the random number is 0
    if rand_num == 0:
        # tell the user "Yes"
        messagebox.showinfo(title="Magic 8 Ball", message="Yes")
    # If the random number is 1
    elif rand_num == 1:
        # tell the user "No"
        messagebox.showinfo(title="Magic 8 Ball", message="No")
    # If the random number is 2
    elif rand_num == 2:
        # tell the user "Maybe you should ask Google?"
        messagebox.showinfo(title="Magic 8 Ball", message="Maybe you should ask Google?")
    # If the random number is 3
    elif rand_num == 3:
        # write your own answer
        messagebox.showinfo(title="Magic 8 Ball", message="50-50 shot")
