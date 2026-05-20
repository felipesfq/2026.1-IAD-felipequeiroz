try:
    horas = input('Digite as Horas: ')
    horas = float(horas)

    taxa = input('Digite a taxa: ')
    taxa = float(taxa)

    if horas > 40:
        horas_extras = horas - 40
        pagamento = (40 * taxa) + (horas_extras * taxa * 1.5)
    else:
        pagamento = horas * taxa

    print('Pagamento:', pagamento)

except:
    print('Erro, por favor utilize uma entrada numérica')
