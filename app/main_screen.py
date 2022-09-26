
import json
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile
import pygame

root = Tk()
root.title("Lista de Tarefas")
root.geometry("1200x900")

root.resizable(0,0)
root.config(background= "#DAFAF4")

pygame.mixer.init()

class Aplicativo:
    aberto = False
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
        #self.listaTarefas.insert(0 ,"Varrer a casa", "Dormir cedo", "Lavar roupa", "Limpar chao")
        self.listaTarefas.place(x= 20, y=150)

        self.saveButton = Button(
            text="Salvar", font=self.fontePadrao,
            width = 10, height = 2, border= 5)
        self.saveButton.place(x=1020, y=60)
        self.saveButton["command"] = self.saveFile 

        return None

    def adicionarTarefa(self):
     
        if Aplicativo.aberto == False:
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

            Aplicativo.aberto = True
    
    def limparBox(self):
        self.boxTarefa.delete(1.0, END)

    def closeBox(self):
        self.addTarefa.place_forget()
        self.boxTarefa.place_forget()
        self.confTarefa.place_forget()
        self.lpTarefa.place_forget()
        self.escTarefa.place_forget()
        Aplicativo.aberto = False
    
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
        if not self.listaTarefas.curselection():
            messagebox.showinfo("Informação", "Selecione uma tarefa para remove-lá.")
            
        self.listaTarefas.get(self.listaTarefas.curselection())
        resposta = messagebox.askquestion("Atenção", "Tem certeza que deseja remover essa tarefa?")
        
        if resposta == "yes":
            self.listaTarefas.delete(self.listaTarefas.curselection())

    def concluiTarefa(self):
        if not self.listaTarefas.curselection():
            messagebox.showinfo("Informação", "Selecione uma tarefa para conclui-lá.")

        self.okTarefaDois.insert(0, self.listaTarefas.get(self.listaTarefas.curselection()))
        self.listaTarefas.delete(self.listaTarefas.curselection())

    def cleanLists(self):
        msgbox = Toplevel(root)
        msgbox.title("Atenção")
        msgbox.config(background = "#ffffff")
        msgbox.resizable(0,0)
        x_position = 780
        y_position = 470
        msgbox.geometry(f"400x120+{x_position}+{y_position}")
        msgbox.grab_set()
        
        pygame.mixer.music.load("D:/Users/v3nd4/python_downloader_videos/sound_exit_ok.mp3")
        pygame.mixer.music.play(loops = 0)

        self.iconeUm = PhotoImage(file="C:/Users/Fabio/lista-tarefas/app/images/icon.PNG")
        self.iconeTest = Label(msgbox, image= self.iconeUm, bg="#ffffff")
        self.iconeTest.place(x=100, y=23)

        
        
        self.tituloDois = Label(msgbox, text="Qual lista você deseja limpar?", background="#ffffff")
        self.tituloDois.place(x= 160, y=30)

        self.barra = Label(msgbox, width=57, height=3, background="#f0f0f0")
        self.barra.place(x=0, y=75)

        self.cleanAllLists = Button(
            msgbox, font=("Arial", "9"), 
            text="Ambas as listas")
        self.cleanAllLists.place(x= 15, y=85)
        self.cleanAllLists["command"] = lambda: self.allList(msgbox)
        
        self.cleanMainList = Button(
            msgbox, font=("Arial", "9"), 
            text="Tarefas")
        self.cleanMainList.place(x= 126, y=85)
        self.cleanMainList["command"] = lambda: self.mainList(msgbox)
        
        self.cleanSecondList = Button(
            msgbox, font=("Arial", "9"), 
            text="Tarefas Concluídas")
        self.cleanSecondList.place(x=190, y=85)
        self.cleanSecondList["command"] = lambda: self.secondList(msgbox)
        
        self.cleanCancel = Button(
            msgbox, font=("Arial", "9"), 
            text="Cancelar")
        self.cleanCancel.place(x=320, y=85)
        self.cleanCancel["command"] = msgbox.destroy

    def allList(self, msgbox):
        self.listaTarefas.delete(0, END)
        self.okTarefaDois.delete(0, END)
        msgbox.grab_release()
        msgbox.destroy()
        
    def mainList(self, msgbox):
        self.listaTarefas.delete(0, END)
        msgbox.grab_release()
        msgbox.destroy()
        
    def secondList(self, msgbox):
        self.okTarefaDois.delete(0, END)
        msgbox.grab_release()
        msgbox.destroy()

    def saveFile(self):
        nameFile = asksaveasfile(mode="w", defaultextension= json)
        textList = self.listaTarefas.get(1.0, END)
        nameFile.write(textList)
        nameFile.close()
        

Aplicativo()
root.mainloop()


