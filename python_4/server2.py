import socket
import threading
import requests


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socked created")

addrs = ("127.0.0.1", 4545)

API_KEY = "2b2f6591fbc68598845fb43e2851abb2"

def handle_message(client, addrs):
    while True:
        msg = client.recv(1024).decode("utf-8")
        if msg == "/stop":
            client.close()
            print(f"Active conections:> {threading.active_count() - 1}")
            break
        else:    
            print(f"Message:> {msg} | from:> {addrs}")
            weather = requests.get(f"api.openweathermap.org/data/2.5/weather?q={msg},uk&APPID={API_KEY}")  
            client.send(weather.content)

server.bind(addrs)
server.listen(5)

while True:
    client, addrs = server.accept()  
    thread = threading.Thread(target=handle_message, args=(client, addrs))
    thread.start()
    print(f"Active conections:> {threading.active_count() - 1}")