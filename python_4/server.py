import socket
import json
import threading


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socked created")

addrs = ("127.0.0.1", 4545)

with open("weather.json", "r") as obj:
    weather = json.load(obj)

def handle_message(client, addrs):
    while True:
        msg = client.recv(1024).decode("utf-8")
        if msg == "/stop":
            client.close()
            print(f"Active conections:> {threading.active_count() - 1}")
            break
        else:    
            print(f"Message:> {msg} | from:> {addrs}")
            if msg not in weather:
                client.send("Not found".encode("utf-8"))   

            else:
                response = weather[msg]
                client.send(response.encode("utf-8"))   

server.bind(addrs)
server.listen(5)

while True:
    client, addrs = server.accept()  
    thread = threading.Thread(target=handle_message, args=(client, addrs))
    thread.start()
    print(f"Active conections:> {threading.active_count() - 1}")