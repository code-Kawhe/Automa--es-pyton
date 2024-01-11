import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import psutil

import pyautogui
from time import sleep


def verificar_cor_e_clicar(cor,  x,  y):
    # Captura a cor do pixel nas coordenadas (x,  y)
    pixel_color = pyautogui.pixel(x,  y)
    # Verifica se a cor do pixel é igual à cor desejada
    if pixel_color == cor:
        pyautogui.click(x,  y,  duration=0.1)
        return True
    else:
        # print(f"Pixel ({x},  {y}) - Cor não encontrada - Cor: {pixel_color}")
        return False
    
def execute_function1():

    qt_str = Entry_FNC1_Qt.get()
    qt = int(qt_str) if qt_str.isdigit() else 0

    if qt > 0:
        
        x_inicial = 308
        y = 1056
        
        # Cor desejada
        cor_desejada = (35,  86,  141)

        # Distância entre pixels
        distancia_entre_pixels = 44
        
        # Número de pixels a verificar
        num_pixels = 30 
        
        for i in range(num_pixels):
            x_atual = x_inicial + i * distancia_entre_pixels
            # Verifica se a cor é a desejada e clica se for
            if verificar_cor_e_clicar(cor_desejada,  x_atual,  y):
                # Aguarda um curto período para evitar cliques muito rápidos
                sleep(0.1)
            
        if pyautogui.pixel(1763, 81) == (0, 34, 74) and pyautogui.pixel(1814, 966) == (0, 42, 90) and pyautogui.pixel(106, 979) == (0, 43, 91) and pyautogui.pixel(109, 95) == (0, 28, 61):
            # sleep(0.5)
            # if pyautogui.pixel(845, 885) != (255, 255, 255):
            pyautogui.click(917,  638,  duration=0.1)
            sleep(5)
            pyautogui.click(345,  635,  duration=0.1)
            sleep(5)
            pyautogui.click(194,  83,  duration=0.1)
            sleep(5)
            while qt > 0:
                    pyautogui.click(71,  316,  duration=0.1)  # clica no item
                    pyautogui.click(65,  61,  duration=0.1)  # clica para adicionar o coeficiente
                    pyautogui.click(1546,  224,  duration=0.1)  # clica no campo de coeficiente
                    pyautogui.write("1")  # escreve o coeficiente
                    pyautogui.click(1509,  223,  duration=0.1)  # clica abrir o calendario
                    pyautogui.click(1548,  251,  duration=0.1)  # clica para mudar o mes
                    pyautogui.click(1548,  251,  duration=0.1)  # clica para mudar o ano84167186
                    pyautogui.click(1548,  251,  duration=0.1)  # clica para mudar um pouco mais o ano
                    pyautogui.click(1631,  352,  duration=0.1)  # clica seleciona um par de ano
                    pyautogui.click(1631,  352,  duration=0.1)  # clica seleciona mais um par de ano
                    pyautogui.click(1631,  352,  duration=0.1)  # clica seleciona o mes
                    pyautogui.click(1631,  352,  duration=0.1)  # clica seleciona o dia
                    pyautogui.click(1617,  228,  duration=0.1)  # salva o coeficiente
            
                    qt -= 1
                    sleep(35)
                    pyautogui.click(1204,  645,  duration=0.1)  # clica em ok no erro
                    if qt <= 0:
                        break
            # else:
            #     for i in range(num_pixels):
            #         x_atual = x_inicial + i * distancia_entre_pixels
            #         # Verifica se a cor é a desejada e clica se for84167186
            #         if verificar_cor_e_clicar(cor_desejada,  x_atual,  y):
            #             # Aguarda um curto período para evitar cliques muito rápidos
            #             pyautogui.click(x_atual+188, 887)
            #             sleep(0.1)

        else:
            sleep(1)
            pyautogui.click(857, 488)
            pyautogui.write("84167186")
            pyautogui.press("enter", presses=2)
            sleep(10)
            execute_function1()
        
    else:
        return  
    
def execute_function2():
    
    Mes = Entry_FNC2_Mes.get()
    Ano = Entry_FNC2_Ano.get()
    
    if Ano:
        if Mes:
            x_inicial = 308
            y = 1056

            # Cor desejada
            cor_desejada = (35,  86,  141)

            # Distância entre pixels
            distancia_entre_pixels = 44
            
            # Número de pixels a verificar
            num_pixels = 25
            
            for i in range(num_pixels):
                x_atual = x_inicial + i * distancia_entre_pixels
                # Verifica se a cor é a desejada e clica se for
                if verificar_cor_e_clicar(cor_desejada,  x_atual,  y):
                    # Aguarda um curto período para evitar cliques muito rápidos
                    sleep(0.1)
                    
            if pyautogui.pixel(1763, 81) == (0, 34, 74) and pyautogui.pixel(1814, 966) == (0, 42, 90) and pyautogui.pixel(106, 979) == (0, 43, 91) and pyautogui.pixel(109, 95) == (0, 28, 61):
                # Seleciona a obra =====================
                pyautogui.click(1017,  632,  duration=0.1)
                sleep(2)
                pyautogui.click(877,  590,  duration=0.1)
                sleep(2)
                pyautogui.click(203,  93,  duration=0.1)
                pyautogui.click(194,  125,  duration=0.1)
                # Seleciona a obra =====================
                
                # Seleciona a data inicial ======================
                pyautogui.click(269,  91,  duration=0.1)
                pyautogui.write("01")
                pyautogui.click(289,  91,  duration=0.1)
                pyautogui.write(str(Mes))
                pyautogui.click(312,  91,  duration=0.1)
                pyautogui.write(str(Ano))
                # Seleciona a data inicial ======================
                    
                # Seleciona a data final ======================
                pyautogui.click(269,  132,  duration=0.1)
                if Mes == "01":
                    pyautogui.write("30")
                elif Mes == "02":
                    pyautogui.write("28")
                elif Mes == "03":
                    pyautogui.write("31")
                elif Mes == "04":
                    pyautogui.write("30")
                elif Mes == "05":
                    pyautogui.write("31")
                elif Mes == "06":
                    pyautogui.write("30")
                elif Mes == "07":
                    pyautogui.write("31")
                elif Mes == "08":
                    pyautogui.write("31")
                elif Mes == "09":
                    pyautogui.write("30")
                elif Mes == "10":
                    pyautogui.write("31")
                elif Mes == "11":
                    pyautogui.write("30")
                elif Mes == "12":
                    pyautogui.write("31")
                pyautogui.click(289,  132,  duration=0.1)
                pyautogui.write(str(Mes))
                pyautogui.click(312,  132,  duration=0.1)
                pyautogui.write(str(Ano))
                # Seleciona a data final ======================
                
                # Busca ======================
                pyautogui.click(137, 175, duration=0.1)
                pyautogui.press("enter")
                # Busca ======================
                
                # Busca ======================
                pyautogui.click(23, 391, duration=0.1)
                sleep(3)
                pyautogui.click(789, 432, duration=0.1)
                pyautogui.click(948, 698, duration=0.1)
                pyautogui.click(943, 542, duration=0.1)
                pyautogui.click(857, 593, duration=0.1)
                pyautogui.click(950, 639, duration=0.1)
                # Busca ======================
            else:
                sleep(1)
                pyautogui.click(857, 488)
                pyautogui.write("84167186")
                pyautogui.press("enter", presses=2)
                sleep(10)
                execute_function2()
        else:
            return
    else:
        return

def execute_function3():
    x_inicial = 308
    y = 1056

    # Cor desejada
    cor_desejada = (35,  86,  141)

    # Distância entre pixels
    distancia_entre_pixels = 44
    
    # Número de pixels a verificar
    num_pixels = 25
    
    for i in range(num_pixels):
        x_atual = x_inicial + i * distancia_entre_pixels
        # Verifica se a cor é a desejada e clica se for
        if verificar_cor_e_clicar(cor_desejada,  x_atual,  y):
            # Aguarda um curto período para evitar cliques muito rápidos
            sleep(0.1)
            
    if pyautogui.pixel(1763, 81) == (0, 34, 74) and pyautogui.pixel(1814, 966) == (0, 42, 90) and pyautogui.pixel(106, 979) == (0, 43, 91) and pyautogui.pixel(109, 95) == (0, 28, 61):
        pyautogui.click(918, 638, duration=0.1)
        sleep(1)
        pyautogui.click(1418, 612, duration=0.1)
        sleep(1)
        pyautogui.click(487, 68, duration=0.1)
        pyautogui.click(890, 570, duration=0.1)
        pyautogui.click(1043, 413, duration=0.1)
        pyautogui.click(1881, 71, duration=0.1)
        sleep(5)
        pyautogui.click(25, 384, duration=0.1)
        pyautogui.click(961, 690, duration=0.1)
        sleep(1)
        pyautogui.click(944, 539, duration=0.1)
        pyautogui.click(955, 629, duration=0.1)
    else:
        sleep(1)
        pyautogui.click(857, 488)
        pyautogui.write("84167186")
        pyautogui.press("enter", presses=2)
        sleep(10)
        execute_function2()
        
def execute_function4():
    
    qt_str2 = Entry_FNC4_Qt.get()
    qt2 = int(qt_str2) if qt_str2.isdigit() else 0
    
    print(qt2)
    
    initialP = 268
    
    while qt2 > 0:
        pyautogui.click(847,initialP, duration=0.1)
        pyautogui.click(776,896, duration=0.1)
        sleep(1)
        pyautogui.click(1359,555, duration=0.1)
        pyautogui.click(1507,941, duration=0.1)
        pyautogui.click(1340,861, duration=0.1)
        pyautogui.click(1552,691, duration=0.1)
        qt2 -= 1
        initialP += 15
        

    
janela = tk.Tk()

# config da janela -----------------------------------------
bara = Scrollbar(janela)
canvas = Canvas(janela, yscrollcommand = bara.set)
bara.config(command=canvas.yview)
bara.pack(side = "right", fill="y")
frame = Frame(canvas)
canvas.pack(side = "top", fill="both", expand=True)
canvas.create_window(0, 0, window=frame, width=350, height=600)
janela.title("automações python")
janela.geometry("350x600")
janela.resizable(width=False,  height=False)
# config da janela -------------------------------------------

# Nome da função ---------------------------------------------
Label_FNC1_Nome=tk.Label(frame)
Label_FNC1_Nome["font"] = tkFont.Font(family='Arial', size=10)
Label_FNC1_Nome["fg"] = "#333333"
Label_FNC1_Nome["justify"] = "center"
Label_FNC1_Nome["text"] = "Coeficientes plannix"
Label_FNC1_Nome.grid(column=0, row=0, columnspan=2)
# Nome da função ----------------------------------------------

# Descriçao da função -----------------------------------------
Label_FNC1_Desc=tk.Label(frame)
Label_FNC1_Desc["font"] = tkFont.Font(family='Arial', size=10)
Label_FNC1_Desc["fg"] = "#333333"
Label_FNC1_Desc["justify"] = "center"
Label_FNC1_Desc["text"] = "Adicona os coeficientes de produção das peças"
Label_FNC1_Desc.grid(column=0, row=1, columnspan=2)
# Descriçao da função -----------------------------------------

# Butão da função ---------------------------------------------
Buton_FNC1=tk.Button(frame)
Buton_FNC1["bg"] = "#f0f0f0"
Buton_FNC1["font"] = tkFont.Font(family='Arial', size=10)
Buton_FNC1["fg"] = "#000000"
Buton_FNC1["justify"] = "center"
Buton_FNC1["text"] = "Executar"
Buton_FNC1["command"] = execute_function1
Buton_FNC1["cursor"] = "target"
Buton_FNC1.grid(column=0, row=2, columnspan=2, pady=5)
# Butão da função ---------------------------------------------

# Varialvel da função -----------------------------------------
Label_FNC2_Nome_Input2=tk.Label(frame)
Label_FNC2_Nome_Input2["font"] = tkFont.Font(family='Arial', size=10)
Label_FNC2_Nome_Input2["fg"] = "#333333"
Label_FNC2_Nome_Input2["justify"] = "right"
Label_FNC2_Nome_Input2["text"] = "Quantidade:"
Label_FNC2_Nome_Input2.grid(column=0, row=3, sticky=E, pady=5)

Entry_FNC1_Qt=tk.Entry(frame)
Entry_FNC1_Qt["font"] = tkFont.Font(family='Arial', size=10)
Entry_FNC1_Qt["fg"] = "#333333"
Entry_FNC1_Qt["justify"] = "center"
Entry_FNC1_Qt["textvariable"] = "Qt"
Entry_FNC1_Qt.bind("<Return>",  "on_change")  
Entry_FNC1_Qt.grid(column=1, row=3, sticky=W, pady=5)
# Varialvel da função -----------------------------------------

# ==================================================================

# Separação ---------------------------------------------------
separator_frame = Frame(frame, height=2, width=300, bd=1, relief=SUNKEN, bg="black")
separator_frame.grid(column=0, row=4, columnspan=2, pady=15)
# Separação ---------------------------------------------------

# ==================================================================

# Nome da função ---------------------------------------------
Label_FNC2_Nome=tk.Label(frame)
Label_FNC2_Nome["font"] = tkFont.Font(family='Arial', size=10)
Label_FNC2_Nome["fg"] = "#333333"
Label_FNC2_Nome["justify"] = "center"
Label_FNC2_Nome["text"] = "Romaneios do mes"
Label_FNC2_Nome.grid(column=0, row=5, columnspan=2)
# Nome da função ----------------------------------------------

# Descriçao da função -----------------------------------------
Label_FNC2_Desc=tk.Label(frame)
Label_FNC2_Desc["font"] = tkFont.Font(family='Arial', size=10)
Label_FNC2_Desc["fg"] = "#333333"
Label_FNC2_Desc["justify"] = "center"
Label_FNC2_Desc["text"] = "Faz o pdf dos romaneio do mes no plannix"
Label_FNC2_Desc.grid(column=0, row=6, columnspan=2)
# Descriçao da função -----------------------------------------

# Butão da função ---------------------------------------------
Buton_FNC2=tk.Button(frame)
Buton_FNC2["bg"] = "#f0f0f0"
Buton_FNC2["font"] = tkFont.Font(family='Arial', size=10)
Buton_FNC2["fg"] = "#000000"
Buton_FNC2["justify"] = "center"
Buton_FNC2["text"] = "Executar"
Buton_FNC2["command"] = execute_function2
Buton_FNC2["cursor"] = "target"
Buton_FNC2.grid(column=0, row=7, columnspan=2, pady=5)
# Butão da função ---------------------------------------------

# Varialveis da função -----------------------------------------
Label_FNC2_Nome_Input2=tk.Label(frame)
Label_FNC2_Nome_Input2["font"] = tkFont.Font(family='Arial', size=10)
Label_FNC2_Nome_Input2["fg"] = "#333333"
Label_FNC2_Nome_Input2["justify"] = "right"
Label_FNC2_Nome_Input2["text"] = "Mes:"
Label_FNC2_Nome_Input2.grid(column=0, row=8, sticky=E, pady=5)

Entry_FNC2_Mes=tk.Entry(frame)
Entry_FNC2_Mes["font"] = tkFont.Font(family='Arial', size=10)
Entry_FNC2_Mes["fg"] = "#333333"
Entry_FNC2_Mes["textvariable"] = "Mes"
Entry_FNC2_Mes.bind("<Return>",  "on_change")  
Entry_FNC2_Mes.grid(column=1, row=8, sticky=W, pady=5)

Label_FNC2_Nome_Input2=tk.Label(frame)
Label_FNC2_Nome_Input2["font"] = tkFont.Font(family='Arial', size=10)
Label_FNC2_Nome_Input2["fg"] = "#333333"
Label_FNC2_Nome_Input2["justify"] = "right"
Label_FNC2_Nome_Input2["text"] = "Ano:"
Label_FNC2_Nome_Input2.grid(column=0, row=9, sticky=E, pady=5)

Entry_FNC2_Ano=tk.Entry(frame)
Entry_FNC2_Ano["font"] = tkFont.Font(family='Arial', size=10)
Entry_FNC2_Ano["fg"] = "#333333"
Entry_FNC2_Ano["textvariable"] = "Ano"
Entry_FNC2_Ano.bind("<Return>",  "on_change")
Entry_FNC2_Ano.grid(column=1, row=9, sticky=W, pady=5)
# Varialveis da função -----------------------------------------

# ==================================================================

# Separação ---------------------------------------------------
separator_frame = Frame(frame, height=2, width=300, bd=1, relief=SUNKEN, bg="black")
separator_frame.grid(column=0, row=10, columnspan=2, pady=15)
# Separação ---------------------------------------------------

# ==================================================================

# Nome da função ---------------------------------------------
Label_FNC3_Nome=tk.Label(frame)
Label_FNC3_Nome["font"] = tkFont.Font(family='Arial', size=10)
Label_FNC3_Nome["fg"] = "#333333"
Label_FNC3_Nome["justify"] = "center"
Label_FNC3_Nome["text"] = "Lista de fabricação"
Label_FNC3_Nome.grid(column=0, row=11, columnspan=2)
# Nome da função ----------------------------------------------

# Descriçao da função -----------------------------------------
Label_FNC3_Desc=tk.Label(frame)
Label_FNC3_Desc["font"] = tkFont.Font(family='Arial', size=10)
Label_FNC3_Desc["fg"] = "#333333"
Label_FNC3_Desc["justify"] = "center"
Label_FNC3_Desc["text"] = "Faz o pdf das lista de fabricação"
Label_FNC3_Desc.grid(column=0, row=12, columnspan=2)
# Descriçao da função -----------------------------------------

# Butão da função ---------------------------------------------
Buton_FNC3=tk.Button(frame)
Buton_FNC3["bg"] = "#f0f0f0"
Buton_FNC3["font"] = tkFont.Font(family='Arial', size=10)
Buton_FNC3["fg"] = "#000000"
Buton_FNC3["justify"] = "center"
Buton_FNC3["text"] = "Executar"
Buton_FNC3["command"] = execute_function3
Buton_FNC3["cursor"] = "target"
Buton_FNC3.grid(column=0, row=13, columnspan=2, pady=5)
# Butão da função ---------------------------------------------

# ==================================================================

# Separação ---------------------------------------------------
separator_frame = Frame(frame, height=2, width=300, bd=1, relief=SUNKEN, bg="black")
separator_frame.grid(column=0, row=14, columnspan=2, pady=15)
# Separação ---------------------------------------------------

# ==================================================================

# Nome da função ---------------------------------------------
Label_FNC4_Nome=tk.Label(frame)
Label_FNC4_Nome["font"] = tkFont.Font(family='Arial', size=10)
Label_FNC4_Nome["fg"] = "#333333"
Label_FNC4_Nome["justify"] = "center"
Label_FNC4_Nome["text"] = "cota para restrição (REVIT)"
Label_FNC4_Nome.grid(column=0, row=15, columnspan=2)
# Nome da função ----------------------------------------------

# Descriçao da função -----------------------------------------
Label_FNC4_Desc=tk.Label(frame)
Label_FNC4_Desc["font"] = tkFont.Font(family='Arial', size=10)
Label_FNC4_Desc["fg"] = "#333333"
Label_FNC4_Desc["justify"] = "center"
Label_FNC4_Desc["text"] = "Passa cota para restrição (REVIT)"
Label_FNC4_Desc.grid(column=0, row=16, columnspan=2)
# Descriçao da função -----------------------------------------

# Varialvel da função -----------------------------------------
Label_FNC4_Nome_Input2=tk.Label(frame)
Label_FNC4_Nome_Input2["font"] = tkFont.Font(family='Arial', size=10)
Label_FNC4_Nome_Input2["fg"] = "#333333"
Label_FNC4_Nome_Input2["justify"] = "right"
Label_FNC4_Nome_Input2["text"] = "Quantidade:"
Label_FNC4_Nome_Input2.grid(column=0, row=17, sticky=E, pady=5)

Entry_FNC4_Qt=tk.Entry(frame)
Entry_FNC4_Qt["font"] = tkFont.Font(family='Arial', size=10)
Entry_FNC4_Qt["fg"] = "#333333"
Entry_FNC4_Qt["justify"] = "center"
Entry_FNC4_Qt["textvariable"] = "Qt"
Entry_FNC4_Qt.bind("<Return>",  "on_change")  
Entry_FNC4_Qt.grid(column=1, row=17, sticky=W, pady=5)
# Varialvel da função -----------------------------------------

# Butão da função ---------------------------------------------
Buton_FNC4=tk.Button(frame)
Buton_FNC4["bg"] = "#f0f0f0"
Buton_FNC4["font"] = tkFont.Font(family='Arial', size=10)
Buton_FNC4["fg"] = "#000000"
Buton_FNC4["justify"] = "center"
Buton_FNC4["text"] = "Executar"
Buton_FNC4["command"] = execute_function4
Buton_FNC4["cursor"] = "target"
Buton_FNC4.grid(column=0, row=18, columnspan=2, pady=5)
# Butão da função ---------------------------------------------

# ==================================================================

# Separação ---------------------------------------------------
separator_frame = Frame(frame, height=2, width=300, bd=1, relief=SUNKEN, bg="black")
separator_frame.grid(column=0, row=19, columnspan=2, pady=15)
# Separação ---------------------------------------------------

# Configure o frame para centralizar os widgets no eixo x
for i in range(frame.grid_size()[0]):  # Loop through columns in the frame
    frame.grid_columnconfigure(i, weight=1)  # Set column weight to make widgets centered

# ...

janela.update()
canvas.config(scrollregion = canvas.bbox("all"))
janela.mainloop()