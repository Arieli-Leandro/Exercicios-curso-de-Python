import cria_biblioteca_numeros
import random

arquivo_principal = "numeros_sequencias.txt"

def abre_Arquivo_Cria_Lista_Numerica():
    try:
        with open(arquivo_principal, 'r', encoding='utf-8') as f:

            #Lista vazia
            lista_numerica = []

            #Atribuindo valores á lista vazia
            linha = f.readlines()
            for i in linha:
                lista_numerica.append(i)

        #Pega a lista_numerica e retira os espaços dela, transformando-a em realmente uma lista útil
        lista_sequencial_numerica = [int(x) for x in lista_numerica[0].replace("\n", "").split(",")]
        return lista_sequencial_numerica


    except FileNotFoundError:
        print("O arquivo principal não foi aberto, criando um novo arquivo..")
        cria_biblioteca_numeros.cria_Arquivo_Numeros_Sequencias(100)
        print("Por favor, recompile o programa!")
        exit(1)


def cria_Lista_Aleatoria(lista_sequencial_numerica):

    lista = []

    #definindo o tamanho que vai ter a lista
    tamanho_lista = random.choice(lista_sequencial_numerica)

    #A partir do tamanho, agora vamos gerar aleatoriamente os números dentro da lista

    for i in range(tamanho_lista):

        numero_aleatorio = random.choice(lista_sequencial_numerica)
        lista.append(numero_aleatorio)

    return lista
    


def soma_Listas(l1,l2):
    #Definindo a lista resultante
    lista_resultante = []

    #Achando a lista menor
    if len(l1) < len(l2):
        menor_lista = l1
    else:
        menor_lista = l2

    for indice, lista in enumerate(menor_lista):
        soma = lista + l2[indice]
        lista_resultante.append(soma)

    return lista_resultante




lista_sequencial_numerica = abre_Arquivo_Cria_Lista_Numerica()

l1 = cria_Lista_Aleatoria(lista_sequencial_numerica)
print(l1)

l2 = cria_Lista_Aleatoria(lista_sequencial_numerica)
print(l2)

lista_resultante = soma_Listas(l1,l2)
print(f"Lista resultante - {lista_resultante}")