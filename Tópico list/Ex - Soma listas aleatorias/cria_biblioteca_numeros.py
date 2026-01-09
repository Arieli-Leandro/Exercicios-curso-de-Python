def cria_Arquivo_Numeros_Sequencias(numero_parada):
    with open("numeros_sequencias.txt", "w", encoding="utf-8") as f:

        for i in range(numero_parada + 1):
            if i == numero_parada:
                f.write(f"{i}")
            else:
                f.write(f"{i},")


    print("O arquivo foi criado!")
    return


#Caso queira rodar manualmente 

while True:
    try:
        numero_parada = int(input("Digite qual será o último número do arquivo:")) 
        break
    except ValueError:
        print("Digite um valor inteiro!")
cria_Arquivo_Numeros_Sequencias(numero_parada)
