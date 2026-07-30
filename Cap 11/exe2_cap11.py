import re

nome_arquivo = input("Digite o nome do arquivo: ")
numeros = []

try:
    arquivo = open(nome_arquivo, encoding="utf-8")
except FileNotFoundError:
    print("Arquivo não pôde ser aberto:", nome_arquivo)
else:
    for linha in arquivo:
        encontrados = re.findall(r"^New Revision: ([0-9]+)", linha)
        for numero in encontrados:
            numeros.append(int(numero))

    arquivo.close()

    if numeros:
        print(int(sum(numeros) / len(numeros)))
    else:
        print("Nenhuma revisão foi encontrada")
