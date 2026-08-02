import socket

HOST = "127.0.0.1"
PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected to Server")

while True:
    message = input("Client: ")

    client.send(message.encode())
    if message.lower() == "exit":
        break

    reply = client.recv(1024).decode()

    print("Server:", reply)

    if message.lower() == "exit":
        break

client.close()