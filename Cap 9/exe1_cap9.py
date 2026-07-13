palavras = {}
try:
    arquivo = open("words.txt")
except FileNotFoundError:
    print("Não foi possível abrir o arquivo: words.txt")
else:
    for linha in arquivo:
        for palavra in linha.split():
            palavras[palavra] = True
    print(palavras)
    arquivo.close()
