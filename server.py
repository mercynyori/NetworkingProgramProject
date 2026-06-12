import socket

#the host and port number 
Host = "127.0.0.1"
Port = 2707

#creating the socket for server and client
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#attaching server to the address
server.bind(("127.0.0.1", 2707 ))

#waits for connections
server.listen()


print(f"server is listening on host and port {Host}, {Port} well ")

#infite loop(the server prints connection message then closes connection)
while True:
    client_socket, client_address = server.accept()
    print("The client is connected")
    client_socket.close()