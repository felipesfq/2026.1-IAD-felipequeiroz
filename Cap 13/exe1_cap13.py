import json
import urllib.error
import urllib.parse
import urllib.request

servico = "https://py4e-data.dr-chuck.net/json?"
local = input("Digite uma localização: ")
url = servico + urllib.parse.urlencode({"address": local, "key": 42})

try:
    resposta = urllib.request.urlopen(url)
    dados = json.loads(resposta.read().decode())
    resposta.close()
except (urllib.error.URLError, OSError, json.JSONDecodeError):
    print("Não foi possível recuperar ou interpretar os dados")
else:
    resultados = dados.get("results", [])

    if not resultados:
        print("Localização não encontrada")
    else:
        resultado = resultados[0]
        codigo_pais = None

        for componente in resultado.get("address_components", []):
            if "country" in componente.get("types", []):
                codigo_pais = componente.get("short_name")
                break

        print("Endereço:", resultado.get("formatted_address", "Desconhecido"))

        if codigo_pais:
            print("Código do país:", codigo_pais)
        else:
            print("A localização não pertence a um país identificado")
