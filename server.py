
import socket #networking communications
import threading #multiple connections


host="127.0.0.1"
port=2902

#the socket(socket.AF_INET uses IPv4 adresses
#the second argument is all about the Tcp networ
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#binding which tells the Os to to listen here
server.bind(("127.0.0.1", 2902))
#waits for connections
server.listen()
print(f"Server is connected to {host}:{port}")


# stores the socket objects and nickname 
clients = []
nicknames = []

print(f"Server is listening on 27.0.0.1, 2902")

def broadcast(message):
    """ The messages goe to everyone"""
    for client in clients:
          try:
          #sending message if fails client disconnected
             clients.send(message)
          except Exception as error:
             print(f"No able to send to client:{error}")

def handle_client(client):
     while True:
          try: # infite loop on and on of receiving thr clients message
               message = clients.recv(1024).decode()
               print("Received", message)

          except:
               if client in clients:
                  index = clients.index(client) #find there index n nicknames

                  nickname = nicknames[index]
                  clients.remove(client) #remove client from list

                  client.close()# close connection

               broadcast(f" {nickname} has left chat".encode())
               break
          
def receive():
    while True:
        #waiting for a connection to come
        client, address= server.accept()
        print(f"Connect to server")

          # ask for name
        client.send("NICK".encode())

        #now you have the name
        nickname = client.recv(1024).decode()

        #  store the name 
        nicknames.append(nickname)
        clients.append(client)

        #   here we tell everyone we have it
        client.send("Successfully connected".encode())
        broadcast(f"{nickname} has joined!".encode())


        thread= threading.Thread(target=handle_client, args=(client,))
        thread.start()


if __name__ == "__main__":
    receive()  





     




   








            


          


     






