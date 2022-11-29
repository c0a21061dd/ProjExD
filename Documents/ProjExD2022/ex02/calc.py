import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo("", f"{num}ボタンがクリックされました")
    #entry.insert(tk.END, num)
    if num == "=":
        siki = entry.get()
        res = eval(siki)
        entry.delete(0, tk.END)
        entry.insert(tk.END, res)
    elif num == "c":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, num)



root = tk.Tk()
root.geometry("300x500")

entry = tk.Entry(root, justify="right", width=10, font=("", 30))
entry.grid(row=0, column=0, columnspan=3)

r, c = 1, 0
operators = ["+", "-", "*", "/"]
operators_add = ["**0.5", "**2", "="]

for ope in operators:
    button = tk.Button(root, text=f"{ope}", width=4, height=2, font=("", 20))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1

r += 1
for sign in operators_add:
    button = tk.Button(root, text=f"{sign}", width=4, height=2, font=("", 20))
    button.grid(row=r, column=3)
    button.bind("<1>", button_click)
    operators_add
    r += 1

r, c = 4, 0
for num in range(1, 10, +1):
    button = tk.Button(root, text=f"{num}", width=4, height=2, font=("", 20))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r -= 1
        c = 0

button = tk.Button(root, text="c", width=4, height=2, font=("", 20))
button.grid(row=5, column=0)
button.bind("<1>", button_click)

button = tk.Button(root, text="0", width=4, height=2, font=("", 20))
button.grid(row=5, column=1)
button.bind("<1>", button_click)

button = tk.Button(root, text=".", width=4, height=2, font=("", 20))
button.grid(row=5, column=2)
button.bind("<1>", button_click)

root.mainloop()

