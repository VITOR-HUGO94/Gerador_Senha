import random
import PySimpleGUI as sg
import tkinter
import os


class PassGen:

    def __init__(self):
        # Layout
        sg.theme('Black')
        layout = [
            [sg.Text('Site/Software', size=(10, 1)),
             sg.Input(key='site', size=(20, 1))],
            [sg.Text('E-mail/Usuario', size=(10, 1)),
             sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=(
                range(30)), key='total_chars', default_value=1, size=(3, 1))],
            [sg.Output(size=(35, 5))],
            [sg.Button('Gerar Senha')]

        ]
        # Declara janela
        self.janela = sg.Window('Password Generator', layout)

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
        pass

    def salvar_senha(self):
        pass


gen = PassGen()
gen.Iniciar()        