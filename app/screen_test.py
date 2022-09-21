
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
        self.rmTarefa["command"] = self.removeTarefa

        self.okTarefa = Button(
            text = "Concluir Tarefa",
            font = self.fontePadrao,
            width = 15, height = 2, border= 5)
        self.okTarefa.place(x=420, y= 60)
        self.okTarefa["command"] = self.concluiTarefa
        
        self.okTarefaUm = Label(
            text="Tarefas Concluídas",
            font=("Arial", "13", "bold"),
            bg="light green", width=37, height=2)
        self.okTarefaUm.place(x=750, y= 580)

        self.okTarefaDois = Listbox(
            font=("Arial", "14"),
            width=33, height=10, border=4,
            highlightcolor="light green", highlightbackground="light green", highlightthickness=3)
        self.okTarefaDois.place(x=750, y=620)

        self.lpTarefa = Button(
            text = "Limpar Lista",
            font = self.fontePadrao,
            width = 15, height = 2, border= 5)
        self.lpTarefa.place(x=620, y=60)
        self.lpTarefa["command"] = self.cleanLists
        
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
            bg="yellow", width=37, height=2)
        self.addTarefa.place(x=750, y=150)
        
        self.boxTarefa = Text(
            font= self.fontePadrao,
            width= 40, height= 8, border=4,
            highlightcolor="yellow", highlightbackground="yellow", highlightthickness= 3)
        self.boxTarefa.place(x=750, y=190)

        self.confTarefa = Button(
            text="Adicionar", font = self.fontePadrao,
            width = 10, height = 2, border= 3)
        self.confTarefa.place(x=770, y=370)
        self.confTarefa["command"] = self.addBox

        self.lpTarefa = Button(
            text="Limpar", font = self.fontePadrao,
            width = 10, height = 2, border= 3)
        self.lpTarefa.place(x=900, y=370)
        self.lpTarefa["command"] = self.limparBox

        self.escTarefa = Button(
            text="Esc",font=self.fontePadrao,
            width=5, height=2, border=3)
        self.escTarefa.place(x= 1030, y=370)
        self.escTarefa["command"] = self.closeBox
        
    def limparBox(self):
        self.boxTarefa.delete(1.0, END)

    def closeBox(self):
        self.addTarefa.destroy()
        self.boxTarefa.destroy()
        self.confTarefa.destroy()
        self.lpTarefa.destroy()
        self.escTarefa.destroy()
        return

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
            messagebox.showinfo("Informação", "Espaço vazio. Tente novamente.")
            return 
            
        self.listaTarefas.insert(END, userInput)
        self.boxTarefa.delete(1.0, END)
            
    def removeTarefa(self):
        self.listaTarefas.get(self.listaTarefas.curselection())
        resposta = messagebox.askquestion("Atenção", "Tem certeza que deseja remover essa tarefa?")
        
        if resposta == "yes":
            self.listaTarefas.delete(self.listaTarefas.curselection())

    def concluiTarefa(self):
        self.okTarefaDois.insert(0, self.listaTarefas.get(self.listaTarefas.curselection()))
        self.listaTarefas.delete(self.listaTarefas.curselection())

    def cleanLists(self):
        msgbox = Toplevel()
        msgbox.geometry("400x120")
        msgbox.title("Atenção")
        self.tituloDois = Label(msgbox, text="Qual lista você deseja limpar?")
        self.tituloDois.place(x= 160, y=20)

        self.cleanAllLists = Button(
            msgbox, font=("Arial", "9"), 
            text="Ambas as listas", height=1)
        self.cleanAllLists.place(x= 15, y=80)
        self.cleanAllLists["command"] = self.allLists
        

        self.cleanMainList = Button(
            msgbox, font=("Arial", "9"), 
            text="Tarefas", height=1)
        self.cleanMainList.place(x= 126, y=80)
        self.cleanMainList["command"] = self.listaTarefas.delete(0, END)

        self.cleanSecondList = Button(
            msgbox, font=("Arial", "9"), 
            text="Tarefas Concluídas", height=1)
        self.cleanSecondList.place(x=190, y=80)
        self.cleanSecondList["command"] = self.okTarefaDois.delete(0, END)
        
        self.cleanCancel = Button(
            msgbox, font=("Arial", "9"), 
            text="Cancelar", height=1)
        self.cleanCancel.place(x=320, y=80)
        self.cleanCancel["command"] = msgbox.destroy

    def allLists(self):
        self.listaTarefas.delete(0, END)
        self.okTarefaDois.delete(0, END)

        #emptyList = self.listaTarefas.index("end")
        #if emptyList == 0:
        #    messagebox.showinfo("Informação", "Lista já esta vazia.")
        #    return

        #respostaDois = messagebox.askyesno("Atenção", "Você deseja limpar a lista de tarefas concluídas também?")
        
        #if respostaDois == True:
        #    self.listaTarefas.delete(0, END)
        #    self.okTarefaDois.delete(0, END)
        #else:
        #    self.listaTarefas.delete(0, END)


Aplicativo()
root.mainloop()