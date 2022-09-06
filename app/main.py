

menu = ["Adicionar tarefa", "Remover tarefa", "Concluir tarefa", "Limpar lista de tarefas", "Encerrar aplicativo"]
tarefas = ["Varrer a casa", "Dormir cedo", "Lavar roupa", "Limpar chao"]

def mostrar_tarefas():
    print("---------------------")
    print("-- LISTA DE TAREFAS -")
    if len(tarefas) > 0:
        for i, item in enumerate(tarefas):
            print(f"{i + 1}) {item}") 
    else:
        print("     Lista vazia")
    print("---------------------")
    
def mostrar_menu():
    print("------- MENU -------")
    for i, opcao in enumerate(menu):
        print(f"{i + 1}) {opcao}")
    print("---------------------")

app_rodando = True
while app_rodando:
    
    mostrar_tarefas()
    mostrar_menu()
    
    user = input("Escolha uma opção: ")
    try:
        user = int(user)
        
    except ValueError:
        print("Dígito inválido! Tente novamente. (ERROR 406)")
        continue

    if user > len(menu) or user < 1:
        print("Opção inexiste! Tente novamente. (ERROR 404)")
        continue

    print("---------------------")
    if user == 1:
        nv_tarefa = input("Informe a tarefa a ser adicionada: ")
        numero = False
        try:
            nv_tarefa = int(nv_tarefa)
            numero = True
            print("Dígito inválido! Tente novamente. (ERROR 406)")
            continue
        except:
            pass
        
        if len(nv_tarefa) <= 0:
            print("Dígito inválido! Tente novamente. (ERROR 406)")
            continue
        
        if nv_tarefa.isspace() == True:
            print("Dígito inválido! Tente novamente. (ERROR 406)")
            continue

        tarefas.append(nv_tarefa)

    elif user == 2:
        rm_tarefa = input("Informe o número da tarefa a ser removida: ")
        try:
            rm_tarefa = int(rm_tarefa)

        except ValueError:
            print("Dígito inválido! Tente novamente. (ERROR 406)")
            continue

        if rm_tarefa < 1 or rm_tarefa > len(tarefas)  :
            print("Opção inexiste! Tente novamente. (ERROR 404)")
            continue

        for id, it in enumerate(tarefas):
            if rm_tarefa == id + 1:
                tarefas.pop(id)
                continue

    elif user == 3:
        ok_tarefa = input("Informe o número da tarefa a ser concluida: ")
        try:
            ok_tarefa = int(ok_tarefa)

        except ValueError:
            print("Dígito inválido! Tente novamente. (ERROR 406)")
            continue

        if ok_tarefa < 1 or ok_tarefa > len(tarefas)  :
            print("Opção inexiste! Tente novamente. (ERROR 404)")
            continue

        for id, it in enumerate(tarefas):
            if ok_tarefa == id + 1:
                tarefas[id] += " = OK"

    elif user == 4:
        print("Limpando lista de tarefas...")
        lp_tarefa = input("Deseja confirmar? (y/n) : ")
        lp_tarefa = lp_tarefa.lower()
        if lp_tarefa == "n":
            print("---------------------")
            print("Solicitação de limpeza cancelada.")
            continue
        elif lp_tarefa == "y":
            print("---------------------")
            print("Solicitação de limpeza confirmada.")
            tarefas.clear()
            continue
        else:
            print("Opção inválida! Tente novamente. (ERROR 404)")
            continue
    
    elif user == 5:
        print("Encerrando atividades...")
        off_tarefa = input("Tem certeza que deseja encerrar o aplicativo? (y/n) : ")
        off_tarefa = off_tarefa.lower()
        if off_tarefa == "n":
            print("---------------------")
            print("Solicitação de encerramento cancelada.")
            continue
        elif off_tarefa == "y":
            print("---------------------")
            print("Aplicativo encerrado.")
            app_rodando = False
            break
        else:
            print("Opção inválida! Tente novamente. (ERROR 404)")
            continue



