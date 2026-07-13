def chop(lista):
    del lista[0]
    del lista[-1]


def middle(lista):
    return lista[1:-1]


numeros = [1, 2, 3, 4, 5]
print(middle(numeros))
chop(numeros)
print(numeros)
