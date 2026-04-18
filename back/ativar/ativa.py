from back.run import run

on = False

def toggle(button,root,numero):
    global on

    def schedule_run():
        if on:
            run(numero,on)
            root.after(30000,lambda: schedule_run())

    if on:
        on = False
        button.config(text="Desativado")

    else:
        on = True
        button.config(text="Ativado")
        schedule_run()
