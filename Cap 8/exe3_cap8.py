nome_arquivo = input("Digite o nome do arquivo: ")
try:
    arquivo = open(nome_arquivo)
except FileNotFoundError:
    print("Não foi possível abrir o arquivo:", nome_arquivo)
else:
    for linha in arquivo:
        palavras = linha.split()
        if len(palavras) < 3 or palavras[0] != "From":
            continue
        print(palavras[2])
    arquivo.close()
