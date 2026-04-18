import tkinter as tk
from back.ativar.ativa import toggle
from back.log.log import log

def gui():
    root = tk.Tk()
    root.title("Toca No Teto!")
    root.geometry("300x250")
    root.resizable(False, False)

    mainl = tk.Label(root, text="Toca No Teto!"
                     , font=("Arial", 20, "bold"))
    mainl.place(x=55, y=20)


    numerol = tk.Label(root, text="Número :"
                         , font=("Arial", 12))
    numerol.place(x=10, y=70)

    numeroe = tk.Entry(root,
                       font=("Arial", 12))
    numeroe.place(x=10, y=100)
    numeroe.insert(0, "925455628")
    

    toggleb = tk.Button(root, text="Desativado",
                         font=("Arial", 12, "bold")
                         ,command=lambda: toggle(toggleb,root,numeroe.get()))
    toggleb.place(x=10, y=165)

    logb = tk.Button(root, text="Log",
                     font=("Arial", 12, "bold")
                     ,command=log)
    logb.place(x=140, y=165)

    root.mainloop()
