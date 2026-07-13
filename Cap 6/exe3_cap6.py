def count(texto, letra):
    """Retorna quantas vezes letra aparece em texto."""
    quantidade = 0
    for caractere in texto:
        if caractere == letra:
            quantidade += 1
    return quantidade


texto = input("Digite uma string: ")
letra = input("Digite a letra a contar: ")

if len(letra) != 1:
    print("Digite exatamente um caractere para a letra.")
else:
    print(count(texto, letra))
