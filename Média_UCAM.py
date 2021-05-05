from tkinter import *

def bt_Resultado():

    if (str(float(n1.get()).is_integer() and str(float(n2.get()).is_integer()))):
        a = float(n1.get())
        b = float(n2.get())
        
        lb3["text"] = ((a*3) + (b*7)) / 10

    else:
        lb3["text"] = "Valores informados inválidos"

def bt_Cancelar():
        janela.destroy()
        return

janela = Tk()
janela.title('Calculo de Média Ponderada UCAM')
janela["bg"]="black"
janela.geometry("400x250+600+300")

lb = Label(janela, text='Sempre informar nota em decimal separada por ponto (8.0).', background='black', foreground='white')
lb.place(x=20, y=25)

lb1 = Label(janela, text='Digite a primeira nota', background='black', foreground='white')
lb1.place(x=30, y=65)
n1 = Entry(janela)
n1.place(x=200, y=65)

lb2 = Label(janela, text='Digite a segunda nota', background='black', foreground='white')
lb2.place(x=30, y=105)
n2 = Entry(janela)
n2.place(x=200, y=105)

bt = Button(janela, width="10", text="Resultado", command=bt_Resultado)
bt.place(x=100, y=150)

bt1 = Button(janela, width="10", text="Cancelar", command=bt_Cancelar)
bt1.place(x=200, y=150)

lb3 = Label(janela, text="Média Final")
lb3.place(x=70, y=200)


janela.mainloop()
