def encontra_duplicacao(listas_usuario):
   
   qtd_duplicado = 0
   qtd_lista_nao_duplicada = 0
   qtd_lista_normal = 0

   for i, lista in enumerate(listas_usuario):

        lista_nao_duplicada = set(lista)
        qtd_lista_nao_duplicada = len(lista_nao_duplicada)
        qtd_lista_normal = len(lista)
        
        lista_duplicado = []

        qtd_duplicado = qtd_lista_normal - qtd_lista_nao_duplicada

        #Colocando os duplicados numa lista
        for numero in set(lista):
            if lista.count(numero) > 1:
                lista_duplicado.append(numero)

        if qtd_duplicado == 0:
            print(f"Na lista[{i}] não há números duplicados!")
        elif qtd_duplicado == 1:
            print(f"Na lista[{i}] há apenas {qtd_duplicado} número duplicado! Sendo eles {lista_duplicado}")
        else:
            print(f"Na lista[{i}] há {qtd_duplicado} números duplicados! Sendo eles {lista_duplicado}")

   return

listas_exercicio = [
    [3, 7, 2, 5, 3, 9, 1, 7],
    [10, 4, 6, 8, 2, 6, 4, 11],
    [5, 5, 5, 2, 3, 9, 2, 8],
    [1, 2, 3, 4, 5, 6, 7, 8, 1],
    [12, 14, 15, 12, 16, 17, 18, 14],
    [12, 1, 2, 3, 4, 5, 6, 7],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


encontra_duplicacao(listas_exercicio)