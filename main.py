"""GERADOR DE SENHAS EM PY V1 """
"""DESENVOLVIDO POR FREDERICO ALMEIDA"""
""" Analista de T.I Junior     """

import random, string
from tkinter import *
import pyperclip

#Inicializa a Janela

janela = Tk()
janela.geometry("400x400")  # Tamanho da Janela

# Titulo da Janela
janela.title("Gerador de Senha em PY")

"""------------- Gerando senha aleatoria ------------- """

output_pass = StringVar()

all_combi = [string.punctuation, string.ascii_uppercase, string.digits,
             string.ascii_lowercase]  # list of all possible characters

def senha_aleatoria():
    password = ""  #Para Guardar a seha
    for y in range(senha.get()):
        char_type = random.choice(all_combi)  # to randomize the occurance of alphabet, digit or symbol
        password = password + random.choice(char_type)

    output_pass.set(password)


""" ------------- COPIAR PARA AREA DE TRANSFERENCIA ------------- """

def copiar_senha():
    pyperclip.copy(output_pass.get())


""" ------------- Formatando Janela ------------- """

pass_head = Label(janela, text='Tamanho da Senha ', font='arial 12 bold').pack(pady=10)  # Cabeçalho

senha = IntVar()  # Tamanho da senha

length = Spinbox(janela, from_=4, to=32, textvariable=senha, width=24, font='arial 16').pack()

""" ------------- Botão de gerar senha ------------- """

Button(janela, command=senha_aleatoria, text="Gerar Senha", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5).pack(pady=20)

pass_label = Label(janela, text='Senha Gerada: ', font='arial 12 bold').pack(pady="30 10")
Entry(janela, textvariable=output_pass, width=24, font='arial 16').pack()

# Copy to clipboard button

Button(janela, text='Copiar Para o Ctrl V', command=copiar_senha, font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5).pack(pady=20)

janela.mainloop()
