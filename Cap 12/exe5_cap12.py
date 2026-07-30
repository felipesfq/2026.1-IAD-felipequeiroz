import socket

url = input("Digite uma URL HTTP: ")

try:
    partes = url.split("/")
    if len(partes) < 3 or partes[0] != "http:" or not partes[2]:
        raise ValueError

    hospedeiro = partes[2]
    caminho = "/" + "/".join(partes[3:])

    conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conexao.connect((hospedeiro, 80))
    pedido = f"GET {caminho} HTTP/1.0\r\nHost: {hospedeiro}\r\n\r\n"
    conexao.sendall(pedido.encode())

    resposta = b""
    while True:
        dados = conexao.recv(512)
        if not dados:
            break
        resposta += dados

    conexao.close()
    _, separador, corpo = resposta.partition(b"\r\n\r\n")

    if separador:
        print(corpo.decode(errors="replace"), end="")
    else:
        print("Cabeçalhos HTTP não encontrados")
except (ValueError, OSError):
    print("Não foi possível acessar a URL:", url)
