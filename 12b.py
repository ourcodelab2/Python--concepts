import tkinter as tk
root = tk.Tk()
# Create listbox
listbox = tk.Listbox(root)
listbox.pack()
# Add items to the listbox
for item in ["Item 1", "Item 2", "Item 3"]:
listbox.insert(tk.END, item)