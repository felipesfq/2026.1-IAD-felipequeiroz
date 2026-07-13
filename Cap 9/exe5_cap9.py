nome_arquivo = input("Digite o nome do arquivo: ")
dominios = {}
try:
    arquivo = open(nome_arquivo)
except FileNotFoundError:
    print("Não foi possível abrir o arquivo:", nome_arquivo)
else:
    for linha in arquivo:
        palavras = linha.split()
        if len(palavras) > 1 and palavras[0] == "From":
            dominio = palavras[1].split("@")[-1]
            dominios[dominio] = dominios.get(dominio, 0) + 1
    print(dominios)
    arquivo.close()
