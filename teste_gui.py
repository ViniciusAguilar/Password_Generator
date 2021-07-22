
import tkinter
from tkinter import *
import random

# Vars
chars = "abcdefghiklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%&*'?"

# func


def generator(pass_len, pass_count):
    for x in range(0, pass_count):
        password = ""
        for x in range(0, pass_len):
            pass_char = random.choice(chars)
            password += pass_char
        print("Senha: ", password)
        createlabel(password)


def createlabel(l_password):
    l_pass = Label(window, text="Senha: " + l_password)
    l_pass.pack()


# window
window = tkinter.Tk()
window.title("Passwor generator")
window.minsize(300, 300)

# texto
label = Label(window, text="Gerador de senhas")
label.pack()

# texto
tamanho = Label(window, text="qual o tamanho da senha?")
tamanho.pack()

# caixa
passw_len = StringVar()
passw_len = Entry(window, textvariable=passw_len)
passw_len.pack()


# texto
quant = Label(window, text="Quantas senhas?")
quant.pack()

# caixa
passw_count = StringVar()
passw_count = Entry(window, textvariable=passw_count)
passw_count.pack()


# botao
botao = Button(window, text="Gerar", command=lambda: generator(
    int(passw_len.get()), int(passw_count.get())))
botao.pack()


window.mainloop()
