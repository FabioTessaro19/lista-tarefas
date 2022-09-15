
from tkinter import *
from tkinter import messagebox


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
        self.nvTarefa["command"] = self.adicionarTarefa
        

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

    def adicionarTarefa(self):
        self.addTarefa = Label(
            text="Adicionando Tarefa...",
            font= ("Arial", "13", "bold"),
            bg="light green", width=37, height=2)
        self.addTarefa.place(x=750, y=150)
        
        self.boxTarefa = Text(
            font= self.fontePadrao,
            width= 40, height= 8, border=4,
            highlightcolor="light green", highlightbackground="light green", highlightthickness= 3)
        self.boxTarefa.place(x=750, y=190)

        self.confTarefa = Button(
            text="Adicionar", font = self.fontePadrao,
            width = 10, height = 2, border= 3)
        self.confTarefa.place(x=820, y=370)
        self.confTarefa["command"] = self.addBox

        self.lpTarefa = Button(
            text="Limpar", font = self.fontePadrao,
            width = 10, height = 2, border= 3)
        self.lpTarefa.place(x=950, y=370)
        self.lpTarefa["command"] = self.limparBox
        
    def limparBox(self):
        self.boxTarefa.delete(1.0, END)

    def addBox(self):
        userInput = self.boxTarefa.get(1.0, "end-1c")
        
        for i in userInput:
            if i.isdigit():
                messagebox.showinfo("Informação", "Não são permitidos números. Tente novamente.")
                return 

        if userInput.isspace():
            messagebox.showinfo("Informação", "Espaço vazio. Tente novamente.")
            return

        if len(userInput) == 0:
            return messagebox.showinfo("Informação", "Espaço vazio. Tente novamente.")
            
        self.listaTarefas.insert(END, userInput)
            
        
        
        
        





Aplicativo()
root.mainloop()