# Bibliotecas
import sys
import ast

#Pegando o arquivo e transformando ele em uma lista
def transforma_arq_em_lista(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        conteudo = ast.literal_eval(f.read().strip())

    # Se vier como tupla, converte em lista
    if isinstance(conteudo, tuple):
        conteudo = list(conteudo)

    return conteudo

#Gerando um novo arquivo com listas sem duplicação
def gera_arq_com_lista_n_duplicada(lista_arquivo, arquivo_saida):

    #abre o arquivo que vamos escrever as listas sem duplicação
    with open(arquivo_saida, "w", encoding="utf-8") as f:

        #Removendo a duplicação das listas
        for lista in lista_arquivo:
            lista_n_duplicada = set(lista)
            lista_n_duplicada = str(lista_n_duplicada)
            f.write(f"{lista_n_duplicada}\n")

    return 
        
#Gera o arquivo com informações sobre sobre cada lista
def gera_relatorio_lista(lista_arquivo):

    qtd_lista_normal = 0
    qtd_lista_n_duplicada = 0
    qtd_duplicado = 0

    #abro o arquivo, faço o for e escrevo as informações lá
    with open("arquivo_informacoes_saida.txt", "w", encoding="utf-8") as f:

        for i, lista in enumerate(lista_arquivo):

            #aqui eu calculo o tamanho para colocar no arquivo quanto de duplicação tem em cada lista
            qtd_lista_normal = len(lista)

            lista_n_duplicada = set(lista)
            qtd_lista_n_duplicada = len(lista_n_duplicada)

            qtd_duplicado = qtd_lista_normal - qtd_lista_n_duplicada

            #Colocando os elementos duplicados dentro de uma lista para colocar no arquivo

            lista_numeros_duplicados = []
            for numero in set(lista):

                if lista.count(numero) > 1:
                    lista_numeros_duplicados.append(numero)

            #Escrevendo no arquivo quantas duplicações eu tenho em cada lista e quais são os números que estão duplicados

            if qtd_duplicado == 0:
                f.write(f"A lista[{i}] não têm números duplicados!\n")
            elif qtd_duplicado == 1:
                f.write(f"A lista[{i}] tem {qtd_duplicado} número duplicado, sendo ele {lista_numeros_duplicados}\n")
            else:
                f.write(f"A lista[{i}] tem {qtd_duplicado} números duplicados, sendo eles {lista_numeros_duplicados}\n")

    return

#Chamando via terminal: python remove_duplicacao_arq.py input.txt saida.txt

try:
    nome_programa = sys.argv[0]
    arquivo_texto = sys.argv[1]
    arquivo_saida = sys.argv[2]
except IndexError:
    print("Parâmetros passados via terminal inválidos!")

lista_arquivo = transforma_arq_em_lista(arquivo_texto)

gera_arq_com_lista_n_duplicada(lista_arquivo, arquivo_saida)

gera_relatorio_lista(lista_arquivo)
