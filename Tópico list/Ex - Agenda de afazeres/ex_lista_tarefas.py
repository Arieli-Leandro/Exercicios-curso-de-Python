from tabulate import tabulate

def listar_tarefas(lista):

    if not lista:
        print("Lista de tarefas vazia!")
    else:

        tabela = []

        for i in lista:
            tabela.append([i])

        print("\n")
        print(tabulate(tabela, headers=["Tarefa"], tablefmt="grid"))
        print("\n")
    
    return


def adiciona_tarefas(lista):
   
    tarefa = input("Digite a tarefa que deseja adicionar á lista:")
    lista.append(tarefa)

    return lista


def desfazer_tarefa(lista):

    ultimo_adicionado = len(lista) - 1
    global tarefas_refazer

    tarefas_refazer.append(lista[ultimo_adicionado])

    nova_lista = lista
    nova_lista = nova_lista[:-1]

    return nova_lista

def refazer_tarefa(lista, tarefas_refazer):
    
    ultimo_adicionado_tarefas_refazer = len(tarefas_refazer) - 1
    lista.append(tarefas_refazer[ultimo_adicionado_tarefas_refazer])

    tarefas_refazer = tarefas_refazer[:-1]

    return lista


#Main

lista_tarefas = []
tarefas_refazer = []

sair_programa = False

while sair_programa == False:

    while True:

        print("Escolha uma opção:")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Desfazer")
        print("4 - Refazer")
        print("5 - Sair do menu de opções")
        opcao_menu = int(input(""))
    
        if opcao_menu >= 1 and opcao_menu <= 5:
            break
        else:
            print("Digite uma opção válida do menu de opcões!")

    match opcao_menu:
        case 1: #Adiciona uma nova tarefa
            lista_tarefas = adiciona_tarefas(lista_tarefas)
        case 2: #Lista todas as tarefas
            listar_tarefas(lista_tarefas)
        case 3: #Desfazer o que o usuário fez
            lista_tarefas = desfazer_tarefa(lista_tarefas)
        case 4: #Refazer o que o usuário fez
            lista_tarefas = refazer_tarefa(lista_tarefas, tarefas_refazer)
        case 5:
            sair_programa = True
            print("Obrigada por utilizar este software!")


