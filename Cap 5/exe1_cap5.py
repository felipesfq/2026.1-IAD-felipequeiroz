soma = 0
quantidade = 0

while True:
    entrada = input('Digite um número: ')

    if entrada == 'pronto':
        break

    try:
        numero = float(entrada)
    except:
        print('Entrada Inválida')
        continue

    soma = soma + numero
    quantidade = quantidade + 1

media = soma / quantidade

print(soma, quantidade, media)
