from tkinter import *
from tkinter import Tk, StringVar, ttk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import filedialog as fd

from PIL import Image, ImageTk


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

# abrindo imagem------------------------------------------
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


janela.mainloop()
