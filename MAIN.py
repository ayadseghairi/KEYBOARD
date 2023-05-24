import tkinter as tk
from tkinter import font


def button_click(letter):
    entry.insert(tk.END, letter)

import tkinter as tk

def button_click(letter):
    entry.insert(tk.END, letter)

def copy_text():
    text = entry.get()
    root.clipboard_clear()
    root.clipboard_append(text)

def delete_last_character():
    entry.delete(len(entry.get()) - 1, tk.END)
    
    
def clear_text():
    entry.delete(0, tk.END)
    
root = tk.Tk()
root.title("Keyboard Buttons")


keyboard_letters = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M'],
    ['ض', 'ص', 'ث', 'ق', 'ف', 'غ', 'ع', 'ه', 'خ', 'ح', 'ج'],
    ['ش', 'س', 'ي', 'ب', 'ل', 'ا', 'ت', 'ن', 'م', 'ك', 'ط'],
    ['ذ', 'ئ', 'ء', 'ؤ', 'ر', 'لا', 'ى', 'ة', 'و', 'ز', 'ظ', 'د'],
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
]


for row in keyboard_letters:
    button_row = tk.Frame(root)
    button_row.pack(pady=5)
    for letter in row:
        button = tk.Button(button_row, text=letter, font=font.Font(family='Arial', size=12), width=5, command=lambda l=letter: button_click(l))
        button.pack(side=tk.LEFT, padx=5)

# إضافة زر "نسخ"
copy_button = tk.Button(root, text="copy", command=copy_text)
copy_button.pack(pady=10)


delete_button = tk.Button(root, text="     ←     ", command=delete_last_character)
delete_button.pack(pady=5)

spys_button = tk.Button(root, text="                 ", command=lambda l=' ': button_click(l))
spys_button.pack(pady=5)
clear_button = tk.Button(root, text="Clear", command=clear_text)
clear_button.pack(pady=5)

entry = tk.Entry(root, font=font.Font(family='Arial', size=12), width=30)

entry.pack(pady=10)

root.mainloop()
