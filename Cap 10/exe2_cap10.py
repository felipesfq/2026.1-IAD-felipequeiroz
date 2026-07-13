nome_arquivo = input("Digite o nome do arquivo: ")
horas = {}
try:
    arquivo = open(nome_arquivo)
except FileNotFoundError:
    print("Não foi possível abrir o arquivo:", nome_arquivo)
else:
    for linha in arquivo:
        palavras = linha.split()
        if len(palavras) > 5 and palavras[0] == "From":
            hora = palavras[5].split(":")[0]
            horas[hora] = horas.get(hora, 0) + 1
    for hora, quantidade in sorted(horas.items()):
        print(hora, quantidade)
    arquivo.close()
