nome_arquivo = input("Digite o nome do arquivo: ")
palavras_unicas = []
try:
    arquivo = open(nome_arquivo)
except FileNotFoundError:
    print("Não foi possível abrir o arquivo:", nome_arquivo)
else:
    for linha in arquivo:
        for palavra in linha.split():
            if palavra not in palavras_unicas:
                palavras_unicas.append(palavra)
    palavras_unicas.sort()
    print(palavras_unicas)
    arquivo.close()
