from tkinter import *
from random import randint
altura = 250
largura = 400

class Numeros(object):
    def __init__(self, i):

        self.font = ("Calibri", "16", "bold")

        self.frame1 = Frame(i)
        self.frame2 = Frame(i)
        self.frame3 = Frame(i)
        self.frame4 = Frame(i)


        self.numeros_lotofacil = Button(self.frame1, font=self.font, text="LOTOFACIL", width=15, command=self.Lotofacil)
        self.numeros_megasena = Button(self.frame2, font=self.font, text="MEGA-SENA", width=15, command=self.MegaSena)

        self.numeros_sorteados = Label(self.frame3, font=self.font, text="")

        self.botao_voltar = Button(self.frame4, font=self.font, text="Voltar", command=self.voltar)

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.numeros_lotofacil.pack(pady=5)
        self.numeros_megasena.pack(pady=5)


    def mudaTela(self):
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.numeros_sorteados.pack(pady=15)
        self.botao_voltar.pack()
        self.numeros_sorteados["text"] = self.sorteados

    def Lotofacil(self, *args):
        self.sorteados = []
        while len(self.sorteados) < 15:
            numeros = randint(1, 25)
            if numeros not in self.sorteados:
                self.sorteados.append(numeros)
                self.sorteados.sort()
                self.mudaTela()
            else:
                None

    def MegaSena(self, *args):
        self.sorteados = []
        while len(self.sorteados) < 6:
            numeros = randint(1, 60)
            if numeros not in self.sorteados:
                self.sorteados.append(numeros)
                self.sorteados.sort()
                self.mudaTela()
            else:
                None

    def voltar(self):
        self.botao_voltar.pack_forget()
        self.numeros_sorteados.pack_forget()
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.numeros_lotofacil.pack(pady=5)
        self.numeros_megasena.pack(pady=5)


janela = Tk()
jogos = Numeros(janela)
janela.title("JOGOS LOTERIA")


largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

janela.mainloop()