import re

expressao = input("Digite uma expressão regular: ")
quantidade = 0

try:
    padrao = re.compile(expressao)
    arquivo = open("mbox.txt", encoding="utf-8")
except re.error:
    print("Expressão regular inválida")
except FileNotFoundError:
    print("Arquivo não pôde ser aberto: mbox.txt")
else:
    for linha in arquivo:
        if padrao.search(linha):
            quantidade += 1

    arquivo.close()
    print("mbox.txt teve", quantidade, "linhas que corresponderam a", expressao)
