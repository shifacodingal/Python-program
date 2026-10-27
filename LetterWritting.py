
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

# PART 1: Main window
window = Tk()
window.title("Letter Writing Application")
window.geometry("600x500")

window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)


# PART 2: Open an existing letter
def open_letter():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return

    txt_edit.delete("1.0", END)

    with open(filepath, "r") as file:
        text = file.read()

    txt_edit.insert(END, text)
    window.title(f"Letter Writing Application - {filepath}")


# PART 3: Save the letter under a new name
def save_letter():
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return

    with open(filepath, "w") as file:
        text = txt_edit.get("1.0", END)
        file.write(text)

    window.title(f"Letter Writing Application - {filepath}")


# PART 4: Create widgets
txt_edit = Text(window)

fr_buttons = Frame(window, relief=RAISED, bd=2)

btn_open = Button(fr_buttons, text="Open Letter", command=open_letter)
btn_save = Button(fr_buttons, text="Save Letter As...", command=save_letter)


# PART 5: Arrange widgets using grid
btn_open.grid(row=0, column=0, sticky="ew")
btn_save.grid(row=1, column=0, sticky="ew")

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")


# PART 6: Start the program
window.mainloop()
