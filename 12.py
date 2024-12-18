import tkinter as tk
def on_hello_click():
text_box.delete(0, tk.END)
text_box.insert(tk.END, "Hello, World!")
root = tk.Tk()
# Create textbox
text_box = tk.Entry(root)
text_box.pack()
# Create buttons
hello_button = tk.Button(root, text="Hello", command=on_hello_click)
hello_button.pack()
exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack()
root.mainloop()