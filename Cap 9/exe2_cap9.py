nome_arquivo = input("Digite o nome do arquivo: ")
dias = {}
try:
    arquivo = open(nome_arquivo)
except FileNotFoundError:
    print("Não foi possível abrir o arquivo:", nome_arquivo)
else:
    for linha in arquivo:
        palavras = linha.split()
        if len(palavras) > 2 and palavras[0] == "From":
            dia = palavras[2]
            dias[dia] = dias.get(dia, 0) + 1
    print(dias)
    arquivo.close()
