
from tkinter import *
from turtle import color


app_rodando = True
root = Tk()
root.title("Lista de Tarefas")
root.geometry("1280x900")
root.config(background= "#DAFAF4")


class Aplicativo:
    def __init__(self):
        self.fontePadrao = ("Arial", "12", "bold")
    
        self.titulo = Label()
        self.titulo["text"] ="Aplicativo de Lista de Tarefas"
        self.titulo["font"] = ("Arial", "14", "bold")
        self.titulo["bg"] = "light blue"
        self.titulo["padx"] = 960
        self.titulo["pady"] = 10
        self.titulo.pack()

        self.nvTarefa = Button(
            text = "Adicionar Tarefa",
            font = self.fontePadrao,
            width = 15, height = 2, border= 5)
        self.nvTarefa.place(x=20, y=60)
        #####
        self.addTarefa = Entry()
        self.addTarefa.bind("<Button-1>")
        self.addTarefa.place(x = 900, y = 150)



        self.rmTarefa = Button(
            text = "Remover Tarefa",
            font = self.fontePadrao,
            width = 15, height = 2, border= 5)
        self.rmTarefa.place(x=220, y=60)

        self.okTarefa = Button(
            text = "Concluir Tarefa",
            font = self.fontePadrao,
            width = 15, height = 2, border= 5)
        self.okTarefa.place(x=420, y= 60)

        self.lpTarefa = Button(
            text = "Limpar Lista",
            font = self.fontePadrao,
            width = 15, height = 2, border= 5)
        self.lpTarefa.place(x=620, y=60)
        
        self.endTarefa = Button(
            text = "Encerrar Aplicativo",
            font = self.fontePadrao,
            width = 15, height = 2, border= 5)
        self.endTarefa.place(x=820, y= 60)
        self.endTarefa["command"] = self.endTarefa.quit
       
        self.listaTarefas = Listbox(
            font= ("Arial", "18"),
            width=50, height=25, border = 4,
            highlightcolor="grey", highlightbackground="grey", highlightthickness= 3)
        self.listaTarefas.insert(0 ,"Varrer a casa", "Dormir cedo", "Lavar roupa", "Limpar chao")
        self.listaTarefas.place(x= 20, y=150)
        

        return None

    #def adicionarTarefa(self, event):





Aplicativo()
root.mainloop()