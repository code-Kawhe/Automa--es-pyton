import pyautogui
from time import sleep

pyautogui.click(960,1060, duration=1)
pyautogui.click(1039,963, duration=1)


qt = 8

while qt > 0:
    pyautogui.click(189,313, duration=0.1) #clica no item
    pyautogui.click(65,61, duration=0.1) #clica para adicionar o coeficiente
    pyautogui.click(1546,224, duration=0.1) #clica no campo de coeficiente
    pyautogui.write("1") #escreve o coeficiente
    pyautogui.click(1509,223, duration=0.1) #clica abrir o calendario
    pyautogui.click(1548,251, duration=0.1) #clica para mudar o mes
    pyautogui.click(1548,251, duration=0.1) #clica para mudar o ano
    pyautogui.click(1548,251, duration=0.1) #clica para mudar um pouco mais o ano
    pyautogui.click(1631,352, duration=0.1) #clica seleciona um par de ano
    pyautogui.click(1631,352, duration=0.1) #clica seleciona mais um par de ano
    pyautogui.click(1631,352, duration=0.1) #clica seleciona o mes
    pyautogui.click(1631,352, duration=0.1) #clica seleciona o dia
    pyautogui.click(1617,228, duration=0.1) #salva o coeficiente
    qt -= 1
    sleep(35)
    pyautogui.click(1204,645, duration=0.5) #clika em ok no erro