nome_arquivo = input("Digite o nome do arquivo: ")
if nome_arquivo == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
    try:
        arquivo = open(nome_arquivo)
    except FileNotFoundError:
        print("Não foi possível abrir o arquivo:", nome_arquivo)
    else:
        quantidade = 0
        for linha in arquivo:
            if linha.startswith("Subject:"):
                quantidade += 1
        print("Há", quantidade, "linhas de assunto em", nome_arquivo)
        arquivo.close()
