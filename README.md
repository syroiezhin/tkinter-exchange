# <p id="UP">Would you like to implement a call to a Tkinter object from another file into the main application window?</p>

## <p align="center">Give thanks : 5168 7450 1701 5535 <a href="https://en.privatbank.ua/all-ways-to-receive-send-an-international-transfer"><img src="https://upload.wikimedia.org/wikipedia/uk/f/ff/%D0%9B%D0%BE%D0%B3%D0%BE%D1%82%D0%B8%D0%BF_%D0%9F%D1%80%D0%B8%D0%B2%D0%B0%D1%8224.png" width = "25" alt="Privat Bank UA"> </a></p>

- [x] you can modify existing main file objects from an additional project file:
```bash
label1.config(text="I change the contents of Label by calling file2.")
```
> to do this you need to pass the object variable to the <i>def show_message(label1, ...)</i> function itself.
- [x] to call this function from an additional file, you need to import it as a library:
```bash
from addprogcont import show_message
```
- [x] if you want to create an interface from scratch in an additional file, displaying it when called in the main program, then to do this you need to pass the root object def show_message(..., root), to display all objects in the main program.
```bash
show_message(label1, root)
```
- [x] to implement switching the contents of an additional window between on and off states, we need a mechanism for storing...
```bash
show_label2 = getattr(root, "show_label2", True)
```
- [x] ... and a mechanism for switching:
```bash
setattr(root, "show_label2", False)
```