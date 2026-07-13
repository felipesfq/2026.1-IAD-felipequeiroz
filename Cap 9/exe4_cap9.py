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
    maior_endereco = None
    maior_quantidade = None
    for endereco, quantidade in mensagens.items():
        if maior_quantidade is None or quantidade > maior_quantidade:
            maior_endereco = endereco
            maior_quantidade = quantidade
    if maior_endereco is not None:
        print(maior_endereco, maior_quantidade)
    arquivo.close()
