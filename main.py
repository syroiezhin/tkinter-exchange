from tkinter import Tk, Button, Label
from addprogcont import show_message
def launch(): show_message(label1, root)
if __name__ == '__main__':
    root = Tk()
    root.title("Main")
    button = Button(root, text="Launch", command=launch)
    button.pack()
    label1 = Label(root, text="")
    label1.pack()
    root.mainloop()