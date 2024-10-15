# importes ###################################
# Importando TKINTER
from tkinter import *
from tkinter import Tk, StringVar, ttk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import filedialog as fd

# importando PILLOW
from PIL import Image, ImageTk

# Importando TKCALENDAR
from tkcalendar import Calendar, DateEntry
from datetime import date

# Importando View
from view import *

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

# Criando funções ---------------------------------------------------
# função inserir
global tree
def inserir():
    global imagem, imagem_string, l_imagem

    nome = e_nome.get()
    local = e_local.get()
    descricao = e_descricao.get()
    marca = e_modelo.get()
    data = e_cal.get()
    valor = e_valor.get()
    serie = e_serial.get()
    imagem = imagem_string

    lista_inserir = [nome, local, descricao, marca, data, valor, serie, imagem]

    for i in lista_inserir:
        if i == "":
            messagebox.showerror("Erro", "Preenchar todos os campos")
            return

    inserir_form(lista_inserir)

    messagebox.showinfo("Sucesso", "Os campos foram inseridos com sucesso!")

    e_nome.delete(0, "end")
    e_local.delete(0, "end")
    e_descricao.delete(0, "end")
    e_modelo.delete(0, "end")
    e_cal.delete(0, "end")
    e_valor.delete(0, "end")
    e_serial.delete(0, "end")

    mostrar()


# função para escolher imagem
global imagem, imagem_string, l_imagem

def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem

    # abrindo imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170), Image.Resampling.LANCZOS)
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(
        frameMeio,
        image=imagem,
        bg=co1,
        fg=co4,
    )
    l_imagem.place(x=670, y=10)

# função para ver imagem
def ver_imagem():
    global imagem, imagem_string, l_imagem
    
    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    treev_lista = treev_dicionario["values"]
    
    valor = [int(treev_lista[0])]
    
    iten = ver_item(valor)
    imagem = iten[0][8]
    # abrindo imagem-----------------------------
    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170), Image.Resampling.LANCZOS)
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(
        frameMeio,
        image=imagem,
        bg=co1,
        fg=co4,
    )
    l_imagem.place(x=670, y=10)

# Trabalhando no frames cima ##################################################
# abrindo imagem-----------------------------
app_img = Image.open(r"images/inventario.png")
app_img = app_img.resize((45, 45), Image.Resampling.LANCZOS)
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
# frames de nome e criando entradas
l_nome = Label(
    frameMeio, text="Nome", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4
)
l_nome.place(x=10, y=10)
e_nome = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_nome.place(x=130, y=11)
# frames local da compra
l_local = Label(
    frameMeio,
    text="Sala/Área",
    height=1,
    anchor=NW,
    font=("Ivy 10 bold"),
    bg=co1,
    fg=co4,
)
l_local.place(x=10, y=40)
e_local = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_local.place(x=130, y=41)
# frames descrição
l_descricao = Label(
    frameMeio,
    text="Descrição",
    height=1,
    anchor=NW,
    font=("Ivy 10 bold"),
    bg=co1,
    fg=co4,
)
l_descricao.place(x=10, y=70)
e_descricao = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_descricao.place(x=130, y=71)
# frames marcas
l_modelo = Label(
    frameMeio,
    text="Marca/Modelo",
    height=1,
    anchor=NW,
    font=("Ivy 10 bold"),
    bg=co1,
    fg=co4,
)
l_modelo.place(x=10, y=100)
e_modelo = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_modelo.place(x=130, y=101)
# Frames Calendario
l_cal = Label(
    frameMeio,
    text="Data da Compra",
    height=1,
    anchor=NW,
    font=("Ivy 10 bold"),
    bg=co1,
    fg=co4,
)
l_cal.place(x=10, y=130)
e_cal = DateEntry(frameMeio, width=12, background="darkblue", bordewidth=2, year=2024)
e_cal.place(x=130, y=131)
# frames valor da compras
l_valor = Label(
    frameMeio,
    text="Valor da Compra",
    height=1,
    anchor=NW,
    font=("Ivy 10 bold"),
    bg=co1,
    fg=co4,
)
l_valor.place(x=10, y=160)
e_valor = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_valor.place(x=130, y=161)
# frames series
l_serial = Label(
    frameMeio,
    text="Número de Série",
    height=1,
    anchor=NW,
    font=("Ivy 10 bold"),
    bg=co1,
    fg=co4,
)
l_serial.place(x=10, y=190)
e_serial = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_serial.place(x=130, y=191)
# criando botões #######################################
# botão carregar ----------------------------------------
l_carregar = Label(
    frameMeio,
    text="Imagem do Item",
    height=1,
    anchor=NW,
    font=("Ivy 10 bold"),
    bg=co1,
    fg=co4,
)
l_carregar.place(x=10, y=220)
b_carregar = Button(
    frameMeio,
    command=escolher_imagem,
    width=29,
    text="carregar".upper(),
    compound=CENTER,
    anchor=CENTER,
    overrelief=RIDGE,
    font=("Ivy 8"),
    bg=co1,
    fg=co0,
)
b_carregar.place(x=130, y=221)

# Botao de inserir------------------------------------------
# Abrindo imagem
img_add = Image.open(r"images/adicionar.png")
img_add = img_add.resize((20, 20), Image.Resampling.LANCZOS)
img_add = ImageTk.PhotoImage(img_add)

b_inserir = Button(
    frameMeio,
    command=inserir,
    image=img_add,
    width=95,
    text="  Adicionar".upper(),
    compound=LEFT,
    anchor=NW,
    overrelief=RIDGE,
    font=("Ivy 8"),
    bg=co1,
    fg=co0,
)
b_inserir.place(x=330, y=10)

# botao atualizar
img_update = Image.open(r"images/atualizar.png")
img_update = img_update.resize((20, 20), Image.Resampling.LANCZOS)
img_update = ImageTk.PhotoImage(img_update)

b_update = Button(
    frameMeio,
    command=atualizar_form,
    image=img_update,
    width=95,
    text="  Atualizar".upper(),
    compound=LEFT,
    anchor=NW,
    overrelief=RIDGE,
    font=("Ivy 8"),
    bg=co1,
    fg=co0,
)
b_update.place(x=330, y=50)

# botao deletar
img_delete = Image.open(r"images/deleta.png")
img_delete = img_delete.resize((20, 20), Image.Resampling.LANCZOS)
img_delete = ImageTk.PhotoImage(img_delete)

b_delete = Button(
    frameMeio,
    command=deletar_form,
    image=img_delete,
    width=95,
    text="  Deletar".upper(),
    compound=LEFT,
    anchor=NW,
    overrelief=RIDGE,
    font=("Ivy 8"),
    bg=co1,
    fg=co0,
)
b_delete.place(x=330, y=90)

# botao ver imagem
img_item = Image.open(r"images/caixa.png")
img_item = img_item.resize((20, 20), Image.Resampling.LANCZOS)
img_item = ImageTk.PhotoImage(img_item)

b_item = Button(
    frameMeio,
    command=ver_imagem,
    image=img_item,
    width=95,
    text="  Ver itens".upper(),
    compound=LEFT,
    anchor=NW,
    overrelief=RIDGE,
    font=("Ivy 8"),
    bg=co1,
    fg=co0,
)
b_item.place(x=330, y=221)

# Labels Quantidade total e valores
l_total = Label(
    frameMeio,
    text="",
    width=14,
    height=2,
    pady=5,
    anchor=CENTER,
    font=("Ivy 17 bold"),
    bg=co7,
    fg=co1,
)
l_total.place(x=450, y=12)

l_titulo_total = Label(
    frameMeio,
    text=" Valor Total",
    height=1,
    anchor=NW,
    font=("Ivy 10 bold"),
    bg=co7,
    fg=co1,
)
l_titulo_total.place(x=450, y=12)

# valores total
l_qtd = Label(
    frameMeio,
    text="",
    width=14,
    height=2,
    pady=5,
    anchor=CENTER,
    font=("Ivy 17 bold"),
    bg=co7,
    fg=co1,
)
l_qtd.place(x=450, y=92)

l_titulo_qtd = Label(
    frameMeio,
    text=" Quantidade de Itens",
    height=1,
    anchor=NW,
    font=("Ivy 10 bold"),
    bg=co7,
    fg=co1,
)
l_titulo_qtd.place(x=450, y=92)


# Trabalhando com tabela baixo ##################################################
# Tabela
def mostrar():
    global tree
    # Criando uma visualização em tabela com barras de rolagem duplas
    tabela_head = [
        "#Item",
        "Nome",
        "Sala/Àrea",
        "Descrição",
        "Marca/Modelo",
        "Data da compra",
        "Valor da compra",
        "Número de série",
    ]

    lista_itens = ver_form()

    tree = ttk.Treeview(
        frameBaixo, selectmode=EXTENDED, columns=tabela_head, show="headings"
    )

    # Vertical barra de rolagem ------------------------------------------------
    vbr = ttk.Scrollbar(frameBaixo, orient=VERTICAL, command=tree.yview)
    # Horizontal barra de rolagem -------------------------------------------------
    hbr = ttk.Scrollbar(frameBaixo, orient=HORIZONTAL, command=tree.xview)

    tree.configure(yscrollcommand=vbr.set, xscrollcommand=hbr.set)

    # posicionado barra de rolagem
    tree.grid(column=0, row=0, sticky=NSEW)
    vbr.grid(column=1, row=0, sticky=NS)
    hbr.grid(column=0, row=1, sticky=EW)
    frameBaixo.grid_rowconfigure(0, weight=12)

    hd = [
        "center",
        "center",
        "center",
        "center",
        "center",
        "center",
        "center",
        "center",
    ]
    h = [40, 140, 100, 120, 130, 110, 119, 115]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # ajustando a largura da coluna para o titulo---------------------------------------
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1

    # inserindo itens dentro da tabela ---------------------------------------------------------
    for item in lista_itens:
        tree.insert("", "end", values=item)

    quantidade = []
    
    for iten in lista_itens:
        quantidade.append(iten[6])

    total_valor = sum(quantidade)
    total_itens = len(quantidade)

    l_total["text"] = f"R$ {total_valor:,.2f}"
    l_qtd["text"] = total_itens


mostrar()

janela.mainloop()
