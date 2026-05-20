def calculoPagamento(horas, taxaHora):
    if horas > 40:
        horas_extras = horas - 40
        pagamento = (40 * taxaHora) + (horas_extras * taxaHora * 1.5)
    else:
        pagamento = horas * taxaHora

    return pagamento


horas = input('Insira as Horas: ')
taxaHora = input('Insira o valor da Hora de Trabalho: ')

horas = float(horas)
taxaHora = float(taxaHora)

pagamento = calculoPagamento(horas, taxaHora)

print('Pagamento:', pagamento)
