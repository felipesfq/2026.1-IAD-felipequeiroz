nome_arquivo = input("Digite o nome do arquivo: ")
quantidade = 0
try:
    arquivo = open(nome_arquivo)
except FileNotFoundError:
    print("Não foi possível abrir o arquivo:", nome_arquivo)
else:
    for linha in arquivo:
        palavras = linha.split()
        if len(palavras) > 1 and palavras[0] == "From":
            print(palavras[1])
            quantidade += 1
    print("Havia", quantidade, "linhas no arquivo com From como primeira palavra")
    arquivo.close()
