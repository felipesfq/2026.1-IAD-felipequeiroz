nome_arquivo = input("Digite o nome do arquivo: ")
mensagens = {}
try:
    arquivo = open(nome_arquivo)
except FileNotFoundError:
    print("Não foi possível abrir o arquivo:", nome_arquivo)
else:
    for linha in arquivo:
        palavras = linha.split()
        if len(palavras) > 1 and palavras[0] == "From":
            endereco = palavras[1]
            mensagens[endereco] = mensagens.get(endereco, 0) + 1
    contagens = []
    for endereco, quantidade in mensagens.items():
        contagens.append((quantidade, endereco))
    contagens.sort(reverse=True)
    if contagens:
        quantidade, endereco = contagens[0]
        print(endereco, quantidade)
    arquivo.close()
