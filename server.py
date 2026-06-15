import socket #networking communications
import threading #multiple connections

# chat server class
class ChatServer:
     """
     With this the server can accept multiple connects,store, receive messeges and send broadcasting messeges
     """
def __init__(self, host="127.0.0.1" , port=2707):

#creating the socket for server and client
#the socket(socket.AF_INET uses IPv4 adresses
#the second argument is all about the Tcp network

    self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#binding which tells the Os to to listen here
    self.server.bind(("127.0.0.1", 2707 ))

#waits for connections
    self.server.listen()
    print(f"Server is connected to {host}:{port}")

#data structure to store clients socket objets and nicknames
    self.clients = []
    self.nicknames = []


def broadcasting(self, message,sender_client=None)
     """ here we send messages to every client """




#infite loop(the server prints connection message then closes connection)
while True:
    client_socket, client_address = server.accept()
    print("The client is connected")
    client_socket.close()