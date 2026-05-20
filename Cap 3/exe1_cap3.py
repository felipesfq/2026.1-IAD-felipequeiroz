horas = input('Digite as Horas: ')
taxa = input('Digite a taxa: ')

horas = float(horas)
taxa = float(taxa)

if horas > 40:
    horas_extras = horas - 40
    pagamento = (40 * taxa) + (horas_extras * taxa * 1.5)
else:
    pagamento = horas * taxa

print('Pagamento:', pagamento)
