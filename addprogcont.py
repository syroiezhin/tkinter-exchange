from tkinter import Label
def show_message(label1, root, show_label2 = True):
    show_label2 = getattr(root, "show_label2", True)
    if show_label2:
        label1.config(text="I change the contents of Label by calling file2.")
        root.label2 = Label(root, text="I create a new Label object by calling file2.")
        root.label2.pack()
        setattr(root, "show_label2", False)
    else:
        label1.config(text="")
        root.label2.destroy()
        setattr(root, "show_label2", True)