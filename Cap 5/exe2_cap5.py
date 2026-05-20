maior = None
menor = None

while True:
    entrada = input('Digite um número: ')

    if entrada == 'pronto':
        break

    try:
        numero = float(entrada)
    except:
        print('Entrada Inválida')
        continue

    if maior is None or numero > maior:
        maior = numero

    if menor is None or numero < menor:
        menor = numero

print('Máximo:', maior)
print('Mínimo:', menor)
