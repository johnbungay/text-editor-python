from tkinter import *
from tkinter import filedialog

# Create the main window
root = Tk()
root.title("Text Editor")
root.geometry("700x500")

# Create Text widget
text_area = Text(root, wrap=WORD, font=("Helvetica", 12))
text_area.pack(expand=True, fill=BOTH)

# Save file function
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            content = text_area.get("1.0", END)
            file.write(content)

# Open file function
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text_area.delete("1.0", END)
            text_area.insert("1.0", content)

# Menu bar setup
menu_bar = Menu(root)
root.config(menu=menu_bar)

# File menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Run the application
root.mainloop()