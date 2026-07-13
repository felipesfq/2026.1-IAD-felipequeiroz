nome_arquivo = input("Digite o nome do arquivo: ")
try:
    arquivo = open(nome_arquivo)
except FileNotFoundError:
    print("Não foi possível abrir o arquivo:", nome_arquivo)
else:
    for linha in arquivo:
        print(linha.rstrip().upper())
    arquivo.close()
