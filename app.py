import tkinter as tk
import tkinter.font as tkFont

import pyautogui
from time import sleep

def verificar_cor_e_clicar(cor, x, y):
    # Captura a cor do pixel nas coordenadas (x, y)
    pixel_color = pyautogui.pixel(x, y)

    # Verifica se a cor do pixel é igual à cor desejada
    if pixel_color == cor:
        # Se for, clica no pixel
        pyautogui.click(x, y, duration=0.1)
        x_2 = x + 44
        pyautogui.click(x_2,940, duration=0.2)
        # print(f"Clicou no pixel ({x}, {y}) - Cor encontrada - Cor: {pixel_color}")
        return True
    else:
        # print(f"Pixel ({x}, {y}) - Cor não encontrada - Cor: {pixel_color}")
        return False

def execute_function1():

    qt_str = Entry_FNC1_Qt.get()
    qt = int(qt_str) if qt_str.isdigit() else 0

    if qt > 0:
        x_inicial = 308
        y = 1056

        # Cor desejada
        cor_desejada = (35, 86, 141)

        # Distância entre pixels
        distancia_entre_pixels = 44
        
        # Número de pixels a verificar
        num_pixels = 25
        
        for i in range(num_pixels):
            x_atual = x_inicial + i * distancia_entre_pixels
            # Verifica se a cor é a desejada e clica se for
            if verificar_cor_e_clicar(cor_desejada, x_atual, y):
                # Aguarda um curto período para evitar cliques muito rápidos
                sleep(0.1)
                
        pyautogui.click(917, 638, duration=0.1)
        sleep(5)
        pyautogui.click(345, 635, duration=0.1)
        sleep(5)
        pyautogui.click(194, 83, duration=0.1)
        sleep(5)
        while qt > 0:
                pyautogui.click(71, 316, duration=0.1)  # clica no item
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
                pyautogui.click(1204, 645, duration=0.1)  # clica em ok no erro
                if qt <= 0:
                    break
    else:
        return  
    
def execute_function2():
    
    x_inicial = 308
    y = 1056

    # Cor desejada
    cor_desejada = (35, 86, 141)

    # Distância entre pixels
    distancia_entre_pixels = 44
    
    # Número de pixels a verificar
    num_pixels = 25
    
    for i in range(num_pixels):
        x_atual = x_inicial + i * distancia_entre_pixels
        # Verifica se a cor é a desejada e clica se for
        if verificar_cor_e_clicar(cor_desejada, x_atual, y):
            # Aguarda um curto período para evitar cliques muito rápidos
            sleep(0.1)
                
    pyautogui.click(1017, 632, duration=0.1)
    sleep(2)
    pyautogui.click(877, 590, duration=0.1)
    sleep(2)
    pyautogui.click(203, 93, duration=0.1)
    pyautogui.click(194, 125, duration=0.1)
    

janela = tk.Tk()

# config da janela -----------------------------------------
janela.title("automações pytho")
width=600
height=600
screenwidth = janela.winfo_screenwidth()
screenheight = janela.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
janela.geometry(alignstr)
janela.resizable(width=False, height=False)
# config da janela -------------------------------------------

# Nome da função ---------------------------------------------
Label_FNC1_Nome=tk.Label(janela)
Label_FNC1_Nome["font"] = tkFont.Font(family='Arial',size=10)
Label_FNC1_Nome["fg"] = "#333333"
Label_FNC1_Nome["justify"] = "center"
Label_FNC1_Nome["text"] = "Coeficientes plannix"
Label_FNC1_Nome.place(x=0,y=0,width=600,height=70)
# Nome da função ----------------------------------------------

# Descriçao da função -----------------------------------------
Label_FNC1_Desc=tk.Label(janela)
Label_FNC1_Desc["font"] = tkFont.Font(family='Arial',size=10)
Label_FNC1_Desc["fg"] = "#333333"
Label_FNC1_Desc["justify"] = "center"
Label_FNC1_Desc["text"] = "Adicona os coeficientes de produção das peças"
Label_FNC1_Desc.place(x=0,y=50,width=600,height=35)
# Descriçao da função -----------------------------------------

# Butão da função ---------------------------------------------
Buton_FNC1=tk.Button(janela)
Buton_FNC1["bg"] = "#f0f0f0"
Buton_FNC1["font"] = tkFont.Font(family='Arial',size=10)
Buton_FNC1["fg"] = "#000000"
Buton_FNC1["justify"] = "center"
Buton_FNC1["text"] = "Executar"
Buton_FNC1.place(x=220,y=100,width=165,height=45)
Buton_FNC1["command"] = execute_function1
Buton_FNC1["cursor"] = "target"
# Butão da função ---------------------------------------------

# Varialvel da função -----------------------------------------
Entry_FNC1_Qt=tk.Entry(janela)
Entry_FNC1_Qt["font"] = tkFont.Font(family='Arial',size=10)
Entry_FNC1_Qt["fg"] = "#333333"
Entry_FNC1_Qt["justify"] = "center"
Entry_FNC1_Qt["textvariable"] = "Qt"
Entry_FNC1_Qt.place(x=220,y=150,width=165,height=35)
Entry_FNC1_Qt.bind("<Return>", "on_change")  
# Varialvel da função -----------------------------------------

# Separação ---------------------------------------------------
Label_Line_Nome=tk.Label(janela)
Label_Line_Nome["font"] = tkFont.Font(family='Arial',size=10)
Label_Line_Nome["bg"] = "black"
Label_Line_Nome.place(x=0,y=200,width=600,height=2)
# Separação ---------------------------------------------------

# Nome da função ---------------------------------------------
Label_FNC2_Nome=tk.Label(janela)
Label_FNC2_Nome["font"] = tkFont.Font(family='Arial',size=10)
Label_FNC2_Nome["fg"] = "#333333"
Label_FNC2_Nome["justify"] = "center"
Label_FNC2_Nome["text"] = "Romaneios do mes"
Label_FNC2_Nome.place(x=0,y=210,width=600,height=70)
# Nome da função ----------------------------------------------

# Descriçao da função -----------------------------------------
Label_FNC2_Desc=tk.Label(janela)
Label_FNC2_Desc["font"] = tkFont.Font(family='Arial',size=10)
Label_FNC2_Desc["fg"] = "#333333"
Label_FNC2_Desc["justify"] = "center"
Label_FNC2_Desc["text"] = "Faz o pdf dos romaneio do mes no plannix"
Label_FNC2_Desc.place(x=0,y=260,width=599,height=35)
# Descriçao da função -----------------------------------------

# Butão da função ---------------------------------------------
Buton_FNC2=tk.Button(janela)
Buton_FNC2["bg"] = "#f0f0f0"
Buton_FNC2["font"] = tkFont.Font(family='Arial',size=10)
Buton_FNC2["fg"] = "#000000"
Buton_FNC2["justify"] = "center"
Buton_FNC2["text"] = "Executar"
Buton_FNC2.place(x=220,y=310,width=166,height=45)
Buton_FNC2["command"] = execute_function2
Buton_FNC2["cursor"] = "target"
# Butão da função ---------------------------------------------

# Separação ---------------------------------------------------
Label_Line_Nome=tk.Label(janela)
Label_Line_Nome["font"] = tkFont.Font(family='Arial',size=10)
Label_Line_Nome["bg"] = "black"
Label_Line_Nome.place(x=0,y=370,width=600,height=2)
# Separação ---------------------------------------------------

janela.mainloop()