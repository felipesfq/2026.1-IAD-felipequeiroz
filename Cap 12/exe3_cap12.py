from urllib.error import URLError
from urllib.request import urlopen

url = input("Digite uma URL: ")

try:
    resposta = urlopen(url)
    conteudo = resposta.read().decode(errors="replace")
    resposta.close()
except (ValueError, URLError, OSError):
    print("Não foi possível acessar a URL:", url)
else:
    print(conteudo[:3000])
    print("Total de caracteres:", len(conteudo))
