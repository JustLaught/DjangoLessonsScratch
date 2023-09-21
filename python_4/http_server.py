import socket

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5000
FORMAT = "utf-8"
print(SERVER)

ADDRS = (SERVER, PORT)
HDRS = "HTTP/1.1 200 OK\r\nContent-type: text/html; charset=utf-8\r\n\r\n".encode(FORMAT)
HDRS_404 = "HTTP/1.1 404 OK\r\nContent-type: text/html; charset=utf-8\r\n\r\n".encode(FORMAT)

def load_page(page):
    try:
        with open(page, "rb") as file:
            content = file.read()
        return HDRS + content
    except FileNotFoundError:
        return HDRS_404 + "Sory file not found".encode(FORMAT)


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDRS)
    server.listen(5)
    print("Server started!\n")
    while True:
        conn, address = server.accept()
        data = conn.recv(1024).decode(FORMAT).split(" ")[1][1:]
        content = load_page(data)
        conn.send(content)
        conn.close()
        # print(data)
        # print("shoutdown")

if __name__ == "__main__":
    start_server()