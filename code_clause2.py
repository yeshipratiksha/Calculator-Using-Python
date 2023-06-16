import tkinter as tk
from tkinter import font

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")
window.configure(bg="#212121")

# Styling
entry_bg_color = "#424242"
button_bg_color = "#616161"
button_fg_color = "#FFFFFF"
button_font = font.Font(family="Times New Roman", size=18, weight="bold")

# Create the entry widget
entry = tk.Entry(window, width=20, font=("Times New Roman", 20), bg=entry_bg_color, fg="#FFFFFF", bd=0, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, ipady=10)

# Create the number buttons
for i in range(9):
    button = tk.Button(window, text=str(i + 1), padx=20, pady=10, font=button_font, bg=button_bg_color, fg=button_fg_color,
                       bd=0, activebackground="#9E9E9E", activeforeground="#212121",
                       command=lambda num=i + 1: button_click(num))
    button.grid(row=2 + (i // 3), column=i % 3, padx=5, pady=5)

# Create the zero button
button_zero = tk.Button(window, text="0", padx=20, pady=10, font=button_font, bg=button_bg_color, fg=button_fg_color,
                        bd=0, activebackground="#9E9E9E", activeforeground="#212121",
                        command=lambda: button_click(0))
button_zero.grid(row=5, column=0, padx=5, pady=5)

# Create the operator buttons
operators = ['+', '-', '*', '/']
for i in range(len(operators)):
    button = tk.Button(window, text=operators[i], padx=20, pady=10, font=button_font, bg=button_bg_color, fg=button_fg_color,
                       bd=0, activebackground="#9E9E9E", activeforeground="#212121",
                       command=lambda op=operators[i]: button_click(op))
    button.grid(row=2 + i, column=3, padx=5, pady=5)

# Create the equal button
button_equal = tk.Button(window, text="=", padx=20, pady=10, font=button_font, bg="#c0388c", fg=button_fg_color,
                         bd=0, activebackground="#FF8A65", activeforeground="#212121",
                         command=button_equal)
button_equal.grid(row=5, column=1, padx=5, pady=5, columnspan=2, sticky=tk.W+tk.E)

# Create the clear button
button_clear = tk.Button(window, text="C", padx=20, pady=10, font=button_font, bg="#c0388c", fg=button_fg_color,
                         bd=0, activebackground="#E57373", activeforeground="#212121",
                         command=button_clear)
button_clear.grid(row=5, column=3, padx=5, pady=5)

# Start

window.mainloop()