import socket
import threading

HOST = "127.0.0.1"
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

print(f"Server started on {HOST}:{PORT}")

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            
            message = message.decode()

            if message.lower() == "exit":
                print("Client disconnected.")
                break

            print("Client:", message)
    
            
            if not message:
                break

            print("Client:", message.decode())

            reply = input("Server: ")
            client.send(reply.encode())

        except:
            break

    client.close()

while True:
    client, address = server.accept()
    print(f"Connected with {address}")

    clients.append(client)

    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()