# importes ###################################
#Importando TKINTER
from tkinter import *
from tkinter import Tk, StringVar, ttk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import filedialog as fd

#importando PILLOW
from PIL import Image, ImageTk

#Importando TKCALENDAR
from tkcalendar import Calendar, DateEntry
from datetime import date

################################################
# Cores ######################
tema = "classic"
co0 = "#2e2d2d"  # Preta
co1 = "#feffff"  # Branca
co2 = "#4fa882"  # Verde
co3 = "#38576b"  # Valor
co4 = "#403d3d"  # Letra
co5 = "#e06636"  # - Profile
co6 = "#038cfc"  # Azul
co7 = "#3fbfb9"  # Verde
co8 = "#263238"  # + Verde
co9 = "#e9edf5"  # + Verde
################################

########### Configuração do tamanho da janela ##################
# Criando janela
janela = Tk()
window_height = 600
window_width = 900

screen_width = janela.winfo_screenwidth()
screen_height = janela.winfo_screenheight()

x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (screen_height / 2.3))

janela.title("SISTEMA DE CADASTRO")
janela.iconbitmap(r"images/tabela.ico")
janela.configure(background=co9)
janela.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use(tema)

#################### Posicionado frames ############################
# Criando frames ------------------------------------------------
frameCima = Frame(janela, width=1043, height=50, bg=co1, relief=FLAT)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=303, bg=co1, padx=20, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co1, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

# Trabalhando no frames cima ##################################################
# abrindo imagem-----------------------------
app_img = Image.open(r"images/inventario.png")
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(
    frameCima,
    image=app_img,
    text="Inventário Doméstico",
    width=900,
    compound=LEFT,
    relief=RAISED,
    anchor=NW,
    font=("Verdana 20 bold"),
    bg=co1,
    fg=co4,
)
app_logo.place(x=0, y=0)

# Trabalhando no frames meio ##################################################
# criando entradas
l_nome = Label(frameMeio, text="Nome", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_nome.place(x=10, y=10)
e_nome = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_nome.place(x=130, y=11)

l_local = Label(frameMeio, text="Sala/Área", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_local.place(x=10, y=40)
e_local = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_local.place(x=130, y=41)

l_descricao = Label(frameMeio, text="Descrição", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_descricao.place(x=10, y=70)
e_descricao = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_descricao.place(x=130, y=71)

l_model = Label(frameMeio, text="Marca/Model", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_model.place(x=10, y=100)
e_model = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_model.place(x=130, y=101)

# Frames Calendario
l_cal = Label(frameMeio, text="Data da Compra", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_cal.place(x=10, y=130)
e_cal = DateEntry(frameMeio, width=12, background="darkblue", bordewidth=2, year=2024)
e_cal.place(x=130, y=131)

l_valor = Label(frameMeio, text="Valor da Compra", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_valor.place(x=10, y=160)
e_valor = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_valor.place(x=130, y=161)

l_serial = Label(frameMeio, text="Número de Série", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_serial.place(x=10, y=190)
e_serial = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_serial.place(x=130, y=191)

janela.mainloop()
