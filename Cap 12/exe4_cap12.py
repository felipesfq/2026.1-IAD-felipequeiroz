from urllib.error import URLError
from urllib.request import urlopen

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Instale beautifulsoup4 com: python -m pip install beautifulsoup4")
    raise SystemExit

url = input("Digite uma URL: ")

try:
    resposta = urlopen(url)
    pagina = BeautifulSoup(resposta.read(), "html.parser")
    resposta.close()
except (ValueError, URLError, OSError):
    print("Não foi possível acessar a URL:", url)
else:
    print("Quantidade de parágrafos:", len(pagina("p")))
