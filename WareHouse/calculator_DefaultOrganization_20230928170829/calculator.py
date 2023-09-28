'''
This file contains the Calculator class which represents the basic calculator.
It uses tkinter library for GUI implementation.
'''
import tkinter as tk
import ast
class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Basic Calculator")
        self.entry = tk.Entry(self.root, width=30)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.create_buttons()
    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        row = 1
        col = 0
        for button in buttons:
            tk.Button(self.root, text=button, width=5, command=lambda button=button: self.button_click(button)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1
    def button_click(self, button):
        current = self.entry.get()
        if button == '=':
            try:
                result = ast.literal_eval(current)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except ValueError:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Invalid expression")
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, button)
    def run(self):
        self.root.mainloop()