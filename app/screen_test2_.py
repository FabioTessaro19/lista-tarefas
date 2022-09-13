
from tkinter import * 

class Aplicativo:
    def __init__(self, topoTela = None):
        self.widget1 = Frame(topoTela)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg.pack()
        self.encerrar = Button(self.widget1)
        self.encerrar["text"] = "Encerrar aplicativo"
        self.encerrar["font"] = ("Arial", "10")
       # self.encerrar["width"] = 15
        self.encerrar["command"] = self.widget1.quit
        self.encerrar.pack()
        self.testerUm = Button(self.widget1)
        self.testerUm["text"] = "Clique aqui"
        self.testerUm["font"] = ("Arial", "10")
        self.testerUm["command"] = self.mudarTexto
        self.testerUm.pack()

    def mudarTexto(self):
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão foi clicado"




    #  self.atividade = Entry(self.segundoContainer)
       # self.atividade["width"] = 30
       # self.atividade["font"] = self.fontePadrao
       # self.atividade.place(side=LEFT)
    
        #self.primeiroContainer = Frame(topoTela)
        #self.primeiroContainer["pady"] = 10
        #self.primeiroContainer.place()
        #self.segundoContainer = Frame(topoTela)
        #self.segundoContainer.place()
        #self.terceiroContainer = Frame(topoTela)
        #self.terceiroContainer.place()
        #self.quartoContainer = Frame(topoTela)
        #self.quartoContainer.place()

root = Tk()
Aplicativo(root)
root.mainloop()