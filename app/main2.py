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

    if user.isdigit():
        user = int(user)

        if user > len(menu) or user < 1:
          print("Opção inexiste! Tente novamente. (ERROR 404)")

    print("---------------------")
    if user == 1:
        nv_tarefa = input("Informe a tarefa a ser adicionada: ")
        numero = False

        if nv_tarefa.isdigit():
            nv_tarefa = int(nv_tarefa)
        
        if not len(nv_tarefa):
            print("Dígito inválido! Tente novamente. (ERROR 406)")
            continue
        
        if nv_tarefa.isspace():
            print("Dígito inválido! Tente novamente. (ERROR 406)")
            continue

        tarefas.append(nv_tarefa)

    elif user == 2:
        rm_tarefa = input("Informe o número da tarefa a ser removida: ")

        if rm_tarefa.isdigit():
            rm_tarefa = int(rm_tarefa)
        else:
            print("Dígito inválido! Tente novamente. (ERROR 406)")
            continue

        if rm_tarefa < 1 or rm_tarefa > len(tarefas)  :
            print("Opção inexiste! Tente novamente. (ERROR 404)")
            continue

        tarefas.pop(rm_tarefa-1)

    elif user == 3:
        ok_tarefa = input("Informe o número da tarefa a ser concluida: ")

        if ok_tarefa.isdigit():
            ok_tarefa = int(ok_tarefa)
        else:
            print("Dígito inválido! Tente novamente. (ERROR 406)")
            continue

        if ok_tarefa < 1 or ok_tarefa > len(tarefas)  :
            print("Opção inexiste! Tente novamente. (ERROR 404)")
            continue
        
        tarefas[ok_tarefa-1] += " = OK"

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

