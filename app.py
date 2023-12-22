import tkinter as tk
import tkinter.font as tkFont

import pyautogui
from time import sleep


def execute_function1():
    pyautogui.click(960, 1060, duration=1)
    pyautogui.click(1039, 963, duration=1)
    qt = 1 
    while qt > 0:
        pyautogui.click(189, 313, duration=0.5)  # clica no item
        pyautogui.click(65, 61, duration=0.5)  # clica para adicionar o coeficiente
        pyautogui.click(1546, 224, duration=0.5)  # clica no campo de coeficiente
        pyautogui.write("1")  # escreve o coeficiente
        pyautogui.click(1509, 223, duration=0.5)  # clica abrir o calendario
        pyautogui.click(1548, 251, duration=0.5)  # clica para mudar o mes
        pyautogui.click(1548, 251, duration=0.5)  # clica para mudar o ano
        pyautogui.click(1548, 251, duration=0.5)  # clica para mudar um pouco mais o ano
        pyautogui.click(1631, 352, duration=0.5)  # clica seleciona um par de ano
        pyautogui.click(1631, 352, duration=0.5)  # clica seleciona mais um par de ano
        pyautogui.click(1631, 352, duration=0.5)  # clica seleciona o mes
        pyautogui.click(1631, 352, duration=0.5)  # clica seleciona o dia
        pyautogui.click(1617, 228, duration=0.5)  # salva o coeficiente
        qt -= 1
        sleep(35)
        pyautogui.click(1204, 645, duration=0.5)  # clica em ok no erro     

root = tk.Tk()

root.title("automações pytho")
width=600
height=500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

GLabel_686=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_686["font"] = ft
GLabel_686["fg"] = "#333333"
GLabel_686["justify"] = "center"
GLabel_686["text"] = "label"
GLabel_686.place(x=0,y=0,width=602,height=69)

GButton_395=tk.Button(root)
GButton_395["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Times',size=10)
GButton_395["font"] = ft
GButton_395["fg"] = "#000000"
GButton_395["justify"] = "center"
GButton_395["text"] = "Button"
GButton_395.place(x=220,y=100,width=166,height=43)
GButton_395["command"] = execute_function1

GLabel_309=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_309["font"] = ft
GLabel_309["fg"] = "#333333"
GLabel_309["justify"] = "center"
GLabel_309["text"] = "label"
GLabel_309.place(x=0,y=170,width=599,height=32)
root.mainloop()