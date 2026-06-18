
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


def broadcasting(self, message,sender_client=None):
     """ here we send messages to every client """
     #loop through all the clients that we got
     for client in self.client:
        try:
          #sending message if fails client disconnected
          client.send(message)
        except Exception as error:
            print(f"No able to send to client:{error}")


def remove_client(self,client):
# here we remove the client once they disconnect
    """here we clear the client when they disconnect so that we dont have memory leaks"""
    for client in self.clients:
        # find the index then use index to get the nickname
        index = self.clients.index(client)
        
        nickname = self.clients.nicknames[index]

# we remove the socket of the index and nickname
        self.index.remove(index)
        self.nicknames.remove(nickname)

        client.socket()

# inform everyone that the person has left
left_room_message = f"{nickname} has left the room". encode()
self.broadcasting(left_room_message)

print(f"{nickname} has left the room")


def handle_client(self, client):
    """Here the server listens to any message whether broadcasting or single based messeges"""
    try:
         while True : # infite loop on and on 
            message = client.recv(1024)

            if message:
                self.broadcast(message, sender_client=client)
            else:
                self.remove(client)
                break
    except:  # if client has left the room
    self.remove_client(client)
    break

def accept_client(self, client):
    """ Here the server is constantly waiting for someone to come forever, asks for their name  then accepts"""
while True:
    # wait for the client to come
    client, address = self.server.accept()
    #  ask for there name 
    client.send("MERCY".encode())
    # check if the name exists
    if nickname in self.nicknames:
        client.send("name taken chose another one".encode())
    # check if the name exists
        client.send("MERCY".encode())
    else:
        break # exist 


# add client to the chat
    self.client.append(client)
    self.nickname.append(nickname)
    self.broadcast(f"{nickname}" entered!. encode())

    # create the thread to listen
    thread = threading.Thread(target= self.handle_client, args=(client,))
    thread.start
    
    # start button for the server program
    if__name__ == "__main__":
    server = ChatServer()
    server.run()





   








            


          


     




#infite loop(the server prints connection message then closes connection)
while True:
    client_socket, client_address = server.accept()
    print("The client is connected")
    client_socket.close()

