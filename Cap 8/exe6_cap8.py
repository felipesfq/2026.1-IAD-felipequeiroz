numeros = []
while True:
    entrada = input("Digite um número: ")
    if entrada == "done":
        break
    try:
        numeros.append(float(entrada))
    except ValueError:
        print("Entrada inválida")
if numeros:
    print("Máximo:", max(numeros))
    print("Mínimo:", min(numeros))
