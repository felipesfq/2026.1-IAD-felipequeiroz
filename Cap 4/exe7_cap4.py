def computarNotas(pontuacao):
    if pontuacao < 0.0 or pontuacao > 1.0:
        return 'Pontuação Inválida'
    elif pontuacao >= 0.9:
        return 'A'
    elif pontuacao >= 0.8:
        return 'B'
    elif pontuacao >= 0.7:
        return 'C'
    elif pontuacao >= 0.6:
        return 'D'
    else:
        return 'F'


try:
    pontuacao = input('Insira a pontuação: ')
    pontuacao = float(pontuacao)

    nota = computarNotas(pontuacao)
    print(nota)

except:
    print('Pontuação Inválida')
