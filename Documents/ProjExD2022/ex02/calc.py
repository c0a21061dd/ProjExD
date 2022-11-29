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
#for文で全部回してみました！！
operators = ["+", "-", "*", "/", "7", "8", "9", "**0.5", "4", "5", "6", "**2", "3", "2", "1", "=", "c", "0", "."]

#表の(1,0)から右へ進み、四つ目のボタンまで届けば、下の段へ移行します
for ope in operators:
    button = tk.Button(root, text=f"{ope}", width=4, height=2, font=("", 20))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c == 4:
        r += 1
        c -= 4


root.mainloop()

