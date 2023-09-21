import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addrs = ("127.0.0.1", 4545)

client.connect(addrs)
while True:
    data = input("Enter message: ")
    client.send(data.encode("utf-8"))
    if data == "/stop":
        break
    responce = client.recv(1024).decode("utf-8")
    print(responce)   