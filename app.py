from tkinter import *
from tkinter import messagebox
import pyautogui
from time import sleep

def execute_function():
    pyautogui.click(960, 1060, duration=1)
    pyautogui.click(1039, 963, duration=1)
    qt = 1
    while qt > 0:
        pyautogui.click(189, 313, duration=0.1)  # clica no item
        pyautogui.click(65, 61, duration=0.1)  # clica para adicionar o coeficiente
        pyautogui.click(1546, 224, duration=0.1)  # clica no campo de coeficiente
        pyautogui.write("1")  # escreve o coeficiente
        pyautogui.click(1509, 223, duration=0.1)  # clica abrir o calendario
        pyautogui.click(1548, 251, duration=0.1)  # clica para mudar o mes
        pyautogui.click(1548, 251, duration=0.1)  # clica para mudar o ano
        pyautogui.click(1548, 251, duration=0.1)  # clica para mudar um pouco mais o ano
        pyautogui.click(1631, 352, duration=0.1)  # clica seleciona um par de ano
        pyautogui.click(1631, 352, duration=0.1)  # clica seleciona mais um par de ano
        pyautogui.click(1631, 352, duration=0.1)  # clica seleciona o mes
        pyautogui.click(1631, 352, duration=0.1)  # clica seleciona o dia
        pyautogui.click(1617, 228, duration=0.1)  # salva o coeficiente
        qt -= 1
        sleep(35)
        pyautogui.click(1204, 645, duration=0.5)  # clica em ok no erro
        messagebox.showinfo("Completo", "Uma das funções foi executadas, restan" + qt)

janela = Tk()
janela.title("Automaçoes")
texto1 = Label(janela, text="Automações")
texto1.grid(column=0, row=0, padx=10, pady=10)
botao = Button(janela, text="Coeficiente plannix" , command=execute_function)
botao.grid(column=0, row=1, padx=10, pady=10)
texto2 = Label(janela, text="Adiciona os coeficiente de produção no plannix")
texto2.grid(column=0, row=0, padx=10, pady=10)
janela.mainloop()