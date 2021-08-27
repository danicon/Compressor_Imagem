from tkinter import *
from tkinter.filedialog import *
from PIL import Image
from tkinter import messagebox


# Cores
co0 = "#000000"  # black
co1 = "#cc1d4e"  # red
co2 = "#feffff"  # white
co3 = "#0074eb"  # blue
co4 = "#435e5a"  # #435e5a
co5 = "#59b356"  # green
co6 = "#d9d9d9"  # grey

janela = Tk()
janela.geometry("400x250")
janela.title("Compressor de Imagem")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(background=co2)

frame = Frame(janela, width=400, height=250, bg=co2, relief="flat")
frame.grid(row=0, column=0, sticky=NSEW)

app_name = Label(frame, text="Compressor de Imagem", width=24, height=1, anchor=CENTER,
                pady=7, padx=10, relief="flat", font=("Courier 20 bold"), bg=co2, fg=co0)
app_name.grid(row=0, column=0, columnspan=2, sticky=NSEW, pady=1)




# Paraabrir um novo arquivo
def novoArquivo():
    #Abrindo Imagem
    ficheiro = askopenfilename()
    img = Image.open(ficheiro)

    # Tamanho da imagem original
    img_altura, img_largura = img.size

    def converter():
        # Obtendo o valor da altura e largura a partir do entry
        altura = int(entrada_altura.get())
        largura = int(entrada_largura.get())
        # print(altura, largura)

        novo_valor = (altura, largura)
        nova_img = img.resize(novo_valor)

        img_salvar = asksaveasfilename()
        nova_img.save(img_salvar + ".JPG")

        messagebox.showinfo("Sucesso", "A imagem foi convertida com Sucesso!!!")

        tamanho_original.destroy()
        nova_altura.destroy()
        nova_largura.destroy()
        entrada_altura.destroy()
        entrada_largura.destroy()
        b_converter.destroy()


    tamanho_original = Label(frame, text="Altura e Largura Original " + str(img_altura) + "x" + str(img_largura), width=24, height=1, anchor=CENTER,
                pady=7, padx=10, relief="flat", font=("Courier 12 bold"), bg=co2, fg=co3)
    tamanho_original.grid(row=2, column=0, columnspan=2, sticky=NSEW, pady=1)

    nova_altura = Label(frame, text="Digite nova altura", width=10, height=1, anchor=CENTER,
                pady=7, padx=10, relief="flat", font=("Courier 10 bold"), bg=co2, fg=co0)
    nova_altura.grid(row=3, column=0, sticky=NSEW, pady=5)

    nova_largura = Label(frame, text="Digite nova largura", width=10, height=1, anchor=CENTER,
                    pady=7, padx=10, relief="flat", font=("Courier 10 bold"), bg=co2, fg=co0)
    nova_largura.grid(row=3, column=1, sticky=NSEW, pady=5)

    entrada_altura = Entry(frame, width=9, justify="center")
    entrada_altura.grid(row=4, column=0, sticky=NSEW, pady=5)

    entrada_largura = Entry(frame, width=9, justify="center")
    entrada_largura.grid(row=4, column=1, sticky=NSEW, pady=5)

    b_converter = Button(frame, text="Converter", width=10, height=1, font="5", anchor=CENTER,
                    relief=RAISED, bg=co5, fg=co2, command=converter)
    b_converter.grid(row=5, column=0, columnspan=2, pady=5)



b_novo = Button(frame, text="+ Novo", width=10, height=1, font="5", anchor=CENTER,
                relief=RAISED, bg=co3, fg=co2, command=novoArquivo)
b_novo.grid(row=1, column=0, columnspan=2, sticky=NSEW, pady=1)




janela.mainloop()