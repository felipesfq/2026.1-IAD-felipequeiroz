nome_arquivo = input("Digite o nome do arquivo: ")
letras = {}
try:
    arquivo = open(nome_arquivo)
except FileNotFoundError:
    print("Não foi possível abrir o arquivo:", nome_arquivo)
else:
    for linha in arquivo:
        for caractere in linha.lower():
            if "a" <= caractere <= "z":
                letras[caractere] = letras.get(caractere, 0) + 1
    frequencias = []
    for letra, quantidade in letras.items():
        frequencias.append((quantidade, letra))
    frequencias.sort(reverse=True)
    for quantidade, letra in frequencias:
        print(letra, quantidade)
    arquivo.close()
