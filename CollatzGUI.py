from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import sys


# Função para plotar o gráfico com base nos valores do vetor
def plot_grafico():
    vetor = np.array(list_1)

    fig, ax = plt.subplots(figsize=(6.04, 4.84), dpi=100)
    fig.patch.set_facecolor("black")

    # Configurações do gráfico
    ax.plot(range(1, len(vetor) + 1), vetor, color="lime", linewidth=2)
    ax.set_xlabel("Indice", color="white")
    ax.set_ylabel("Valor", color="white")
    ax.set_title("Valores intermediários", color="white", fontsize=16)
    ax.set_facecolor("black")

    # Configuração dos eixos
    ax.spines["bottom"].set_color("lime")
    ax.spines["left"].set_color("lime")
    ax.spines["top"].set_color("lime")
    ax.spines["right"].set_color("lime")
    ax.tick_params(colors="lime", labelsize=10)
    ax.title.set_color("lime")
    ax.xaxis.label.set_color("lime")
    ax.yaxis.label.set_color("lime")
    ax.tick_params(axis="both", which="both", top=False, right=False)

    # Configurações da grade do gráfico
    ax.grid(True, color="lime", linestyle="dashed", linewidth=0.5)

    # Salva o gráfico em uma imagem temporária
    temp_filename = "temp_plot.png"
    plt.savefig(temp_filename, facecolor="black", bbox_inches="tight", dpi=100)

    # Abre a imagem e exibe na interface
    image = Image.open(temp_filename)
    photo = ImageTk.PhotoImage(image)
    label_imagem.configure(image=photo)
    label_imagem.image = photo

# Função para calcular a sequência de Collatz com base no número digitado pelo usuário
def Collatz():

    try:
        counter = 0
        orbital = 0

        # Limpa a lista, atualiza a interface e obtém o número digitado
        list.delete(0, END)
        list_1.clear()
        root.update()
        c0 = int(text_c0.get())

        if c0 < 1:
            sys.exit()

        # Adiciona o número inicial à lista
        list_1.append(c0)

        while c0 != 1:
        # Insere o número atual na lista

            list.insert(counter, c0)
            # Se o número atual é par, divide por 2
            if c0 % 2 == 0:
                c0 /= 2
                counter += 1
                list_1.append(c0)

            else:
                # Se o número atual é impar, multiplica por 3 e adiciona 1
                c0 = 3 * c0 + 1
                counter += 1
                list_1.append(c0)

            # Atualiza o número orbital (maior encontrado até agora)
            if orbital < c0:
                orbital = c0

        # Insere número final, o número de passos e o maior número na lista
        string_number = str(counter)
        string_number2 = str(orbital)
        list.insert(END, c0)
        list.insert(END, "Etapas: " + string_number)
        list.insert(END, "O maior número: " + string_number2)

    except:
        error()

    # Chama a função para plotar o gráfico
    plot_grafico()

    # Faz a lista rolar até o final e atualiza a barra de rolagem
    list.see(END)
    scrollbar.set(*list.yview())

# Função para exibir janela de erro caso a entrada não seja válida
def error():
    # Define uma janela superior
    erro = Toplevel()
    erro.title("Erro.")

    # Dimensões da janela superior
    width = 500
    height = 110

    # Define a cor do plano de fundo como preta
    erro["bg"] = "black"

    # Centraliza a janela erro na tela
    posx = largura_screen / 2 - width / 2
    posy = altura_screen / 2 - height / 2
    erro.geometry("%dx%d+%d+%d" % (width, height, posx, posy))

    # Define o tamanho mínimo e máximo da janela
    erro.minsize(500, 110)
    erro.maxsize(500, 110)

    # Rotulo mensagem de erro
    label_erro = Label(
        erro,
        text = "Utilize um algorismo válido. ",
        font = "Times 25 bold",
        bg = "black",
        fg = "red",
        padx = 10,
        pady = 7,
    ).pack()

    # Botão erro
    btn_erro = Button(
        erro,
        text = "OK",
        bg = "black",
        fg = "red",
        width = 4,
        height = 2,
        command = erro.destroy,
    ).pack()

# Lista vazia para armazenar os valores da sequência de Collatz
list_1 = []

# Definição da cor lime para ser utilizada em vários elementos da interface
lime = "#00ff00"

root = Tk()

# Dimensões da janela
width = 1280
height = 620

# Centraliza a janela na tela
largura_screen = root.winfo_screenwidth()
altura_screen = root.winfo_screenheight()
posx = largura_screen / 2 - width / 2
posy = altura_screen / 2 - height / 2
root.geometry("%dx%d+%d+%d" % (width, height, posx, posy))

# Define o tamanho mínimo e máximo da janela
root.minsize(1280, 620)
root.maxsize(1280, 620)

# Define a cor de fundo da janela como preta
root["bg"] = "black"

# Define o título da janela
root.title("A Hipótese de Collatz")

# Define o ícone da janela
root.iconbitmap("icons/pythonlogo.ico")

# Cria uma instância do estilo padrão do ttk para personalizar os elementos da interface
style = ttk.Style()
style.theme_use("default")

# Configurações da barra de rolagem
style.configure(
    "TScrollbar",
    background=lime,
    troughcolor="black",
    gripcount=0,
    darkcolor=lime,
    lightcolor=lime,
)

# Rótulo principal
label_1 = Label(
    root,
    text="The Collatz Conjecture",
    font="Times 20 bold italic",
    bg="black",
    fg=lime,
    anchor=CENTER,
    justify=CENTER,
)

# Rótulo para instrução
label_2 = Label(
    root,
    text="Digite um número:",
    font="Times 13 bold",
    bg="black",
    fg=lime,
    anchor=CENTER,
    justify=CENTER,
)

# Ícone do Python
img = PhotoImage(file="images/rsz_snake.png")

# Rótulo para exibir a imagem do ícone
label_imagem = Label(
    root,
    image=img,
    background="black",
)

# Barra de rolagem vertical
scrollbar = ttk.Scrollbar(root, style="TScrollbar")

# Lista para exibir os valores da sequência de Collatz
list = Listbox(
    root,
    width=100,
    height=30,
    background="black",
    fg="lime",
    yscrollcommand=scrollbar.set,
)

# Campo de entrada para o número inicial
text_c0 = Entry(
    root, 
    bg="lime", 
    fg="black", 
    width="100",
)

# Botão para iniciar o algoritmo de Collatz
btn1 = Button(
    root, 
    text="Enviar", 
    bg="black", 
    fg="lime", 
    command=Collatz
)

# Posicionamento dos elementos na interface
label_1.grid(row=0, column=0)
label_imagem.grid(row=1, column=1, padx=15)
list.grid(row=1, column=0, sticky=NE, padx=(10, 0))
scrollbar.grid(row=1, column=1, sticky="wns")
scrollbar.config(command=list.yview)
label_2.grid(row=2, column=0, sticky=SW, padx=(10, 0))
text_c0.grid(row=3, column=0, sticky=W, padx=(10, 0))
btn1.grid(row=4, column=0, sticky=E, pady=3)

root.mainloop()
