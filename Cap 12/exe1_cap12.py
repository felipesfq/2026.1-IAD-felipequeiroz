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

    while True:
        dados = conexao.recv(512)
        if not dados:
            break
        print(dados.decode(errors="replace"), end="")

    conexao.close()
except (ValueError, OSError):
    print("Não foi possível acessar a URL:", url)
