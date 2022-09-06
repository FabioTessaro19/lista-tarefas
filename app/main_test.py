



menu = ["Adicionar tarefa", "Remover tarefa", "Concluir tarefa"]
tarefas = ["Varrer a casa", "Dormir cedo", "Lavar roupa", "Limpar chao"]

def mostrar_tarefas():
    print("---------------------")
    print("-- LISTA DE TAREFAS -")
    for i, item in enumerate(tarefas):
        print(f"{i + 1}) {item}") 
    print("---------------------")
    

app_rodando = True
while app_rodando:

    mostrar_tarefas()

    print("------- MENU -------")
    for i, opcao in enumerate(menu):
        print(f"{i + 1}) {opcao}")
    print("---------------------")
    
    

    user = input("Escolha uma opção: ")
    try:
        user = int(user)
                    
    except ValueError:
        print("Dígito inválido! Tente novamente.")
        continue

    if user > len(menu) or user < 1:
        print("Opção inexiste! Tente novamente.")
        continue
    
    print("---------------------")
    if user == 1:
        nv_tarefa = input("Informe a tarefa a ser adicionada: ")
        tarefas.append(nv_tarefa)
            
    elif user == 2:
        rm_tarefa = int(input("Informe o número da tarefa a ser removida: "))
        for id, it in enumerate(tarefas):
            if rm_tarefa == id + 1:
                tarefas.pop(id)
                continue
    
    elif user == 3:
            ok_tarefa = int(input("Informe o número da tarefa a ser concluida: "))
            for id, it in enumerate(tarefas):
                if ok_tarefa == id + 1:
                    tarefas[id] += " = OK"


       



