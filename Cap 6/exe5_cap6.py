texto = "X-DSPAM-Confidence: 0.8475"
inicio = texto.find(":") + 1
confianca = float(texto[inicio:].strip())

print(confianca)
