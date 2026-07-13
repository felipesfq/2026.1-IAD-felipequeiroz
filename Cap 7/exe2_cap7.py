nome_arquivo = input("Digite o nome do arquivo: ")
try:
    arquivo = open(nome_arquivo)
except FileNotFoundError:
    print("Não foi possível abrir o arquivo:", nome_arquivo)
else:
    total = 0
    quantidade = 0
    for linha in arquivo:
        if linha.startswith("X-DSPAM-Confidence:"):
            total += float(linha.split(":")[1])
            quantidade += 1
    if quantidade > 0:
        print("Média de confiança de spam:", total / quantidade)
    arquivo.close()
