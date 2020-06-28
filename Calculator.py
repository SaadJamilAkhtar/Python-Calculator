import tkinter as tk
from tkinter import ttk
def Clicked(but):
    if but['text'] == '=':
        try:
            result = str(eval(expression.get()))
        except:
            result = "error"
        expression.delete(0, len(expression.get()))
        expression.insert(0, result)
    else:
        expression.insert(len(expression.get()), but["text"])
win = tk.Tk()
win.title('Calculator')
win.resizable(0,0)
buttons = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '.', '0', '=', '+']
col, row = 0, 1
expression = ttk.Entry(win, width=85)
expression.grid(row=0, column=0, columnspan=4)
for i in range(16):
    button = ttk.Button(win, text=buttons[i], width=20)
    button.configure(command=lambda but=button: Clicked(but))
    button.grid(column=col, row=row)
    col = col + 1 if col < 3 else 0
    row += 1 if col == 0 else 0
win.mainloop()
