
import socket #networking communications
import threading #multiple connections


host="127.0.0.1"
port=2120

#the socket(socket.AF_INET uses IPv4 adresses
#the second argument is all about the Tcp networ
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#binding which tells the Os to to listen here
server.bind(("127.0.0.1", 2120))
#waits for connections
server.listen()
print(f"Server is connected to {host}:{port}")


# stores the socket objects and nickname 
clients = {}
nicknames = {}
rooms = {}

print(f"Server is listening on 27.0.0.1, 2120")

def broadcast(message):
    """ The messages goe to everyone"""
    print(f"Broadcasting to {len(clients)} clients")

    for client in clients:
          try:
          #sending message if fails client disconnected
             client.send(message.encode())
          except Exception as error:
             print(f"No able to send to client:{error}")

def handle_client(client):
     while True:
          try: # infite loop on and on of receiving thr clients message
               while True:
                   receive_message = client.recv(1024).decode("utf-8")
                   print(f"Received")
                   broadcast(receive_message)

                   if receive_message == '<rooms>':
                       if len(rooms) == 0:
                          client.send(f"Rooms available are zero".encode("utf-8"))
                          client.send(f"Create room with '<create> room_name'..encode("utf-8")")
                          continue
                       
                        # show the rooms that are there if there
                       else:
                           client.send(f"Rooms:".encode("utf-8"))


                           
                     #creating rooms
                   elif '<create>' in receive_message:
                       room_name = receive_message.split()[1]
                     #check if it exits
                       if  room_name in rooms.keys():
                           client.send(f"This room name has been used".encode("utf-8"))
                           continue

                       room = Room(room_name)
                       rooms[room_name] = room
                       client.send(f"You have created {room_name}".encode("utf-8"))
                       continue
                   
                     #  join rooms
                   elif '<join>' in receive_message:
                        room_name = receive_message.split()[1]

                     #   check if the room is not available
                        if  room_name not in  rooms.keys():
                            client.send(f"The room is not available".encode("utf-8"))
                            continue
                        
                        client.current_room_name = room_name
                        client.current_room = rooms[room_name]
                        client.send("You are in {room_name}.".encode("utf-8"))

                        client.current_room.broadcast(f"{nickname} has joined!")
                        continue
                   
                           # seeing the users available
                   elif receive_message == '<users>':
                            # check if they are in a current room
                       if client.current_room == "None":
                           client.send(f"cant list any room".encode("utf-8"))
                           continue
                            # if they are in a room show me
                       else:
                           client = client.current_room.show_client()
                           for name in client.keys():
                               client.send(name.encode("utf-8"))
                               continue
                           
                           # leaving room
                   elif receive_message == '<leave>':
                       if client.current_room == "None":
                          client.send(f"You cant be removed coz u are not in a current room".encode("utf-8"))
                          continue
                       
                       else:
                          client.current_room.broadcast(f"{nickname} has left".encode("utf-8"))
                          client.current_room.leave_room(client.name, client.send)
                          current_room_name = "None"
                          client.current_room = "None"
                          continue
                       

                        # messagse to send then formatted with the name 
                   sent_message = f"<{client.name}> {receive_message}"
                   print(sent_message)
                          # check if the user in the room
                   if client.current_room == "None":
                       client.send(f"Join a room first".encode('utf-8'))
                   else:
                       client.current_room.broadcast(sent_message)
          except Exception as error:
           print(f"Error")
     
          finally:
           client.close() 
           break
          
def receive():
    while True:
        try:
               #waiting for a connection to come
             client, address= server.accept()
             print(f"Connect to server")

                   # ask for name
             client.send("NICK".encode("utf-8"))

                 #now you have the name
             nickname = client.recv(1024).decode("utf-8")

                 # store the name 
             clients[nickname] = client

                   # here we tell everyone we have it
             client.send("Successfully connected".encode("utf-8"))
             broadcast(f"{nickname} has joined!")


             thread= threading.Thread(target=handle_client, args=(client,))
             thread.start()
             
        except Exception as error:
              print(f"Error")
              break

if __name__ == "__main__":
    receive()  





     




   








            


          


     






