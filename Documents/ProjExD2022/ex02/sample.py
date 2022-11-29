import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("おためしか")
root.geometry("500x200")

label = tk.Label(
    root,
    text = "ラベルを書いてみた件",
    font=("", 20)
)
label.pack() #上からパーっと表示する。無いと画面に何も出ない。

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"[{txt}]ボタンが押されました")

button = tk.Button(root, text="押すな", command=button_click)
button.bind("<1>", button_click)
button.pack()

entry = tk.Entry(root, width=30) #root別に要らんけどあった方がいい
entry.insert(tk.END, "fugapiyo") #指定した位置に文字入れとくみたいな
entry.pack()

root.mainloop()

