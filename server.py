
import socket #networking communications
import threading #multiple connections


host="127.0.0.1"
port=2120

#the socket(socket.AF_INET uses IPv4 adresses
#the second argument is all about the Tcp networ
server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#binding which tells the Os to to listen here
server.bind(("127.0.0.1", 2120))
#waits for connections
server.listen()
print(f"Server is connected to {host}:{port}")


# stores the socket objects and nickname 
clients = {}
rooms = {}

print(f"Server is listening on 27.0.0.1, 2120")


def handle(user):
     while True:
          try: # infite loop on and on of receiving thr clients message
               while True:
                   receive_message = user.sock.recv(1024).decode("utf-8")
                   print(f"Received")
                  

                   if receive_message == '<rooms>':
                       if len(rooms) == 0:
                          user.sock.send(f"Rooms available are zero".encode("utf-8"))
                          user.sock.send(f"Create room with '<create> room_name'.".encode("utf-8"))
                          continue
                       
                        # show the rooms that are there if there
                       else:
                           user.sock.send(f"Rooms:".encode("utf-8"))


                           
                     #creating rooms
                   elif '<create>' in receive_message:
                       room_name = receive_message.split()[1]
                     #check if it exits
                       if  room_name in rooms.keys():
                           user.sock.send(f"This room name has been used".encode("utf-8"))
                           continue

                       room = Room(room_name)
                       rooms[room_name] = room
                       user.sock.send(f"You have created {room_name}".encode("utf-8"))
                       continue
                   
                     #  join rooms
                   elif '<join>' in receive_message:
                        room_name = receive_message.split()[1]

                     #   check if the room is not available
                        if  room_name not in  rooms.keys():
                            user.sock.send(f"The room is not available".encode("utf-8"))
                            continue
                        
                        user.current_room_name = room_name
                        user.current_room = rooms[room_name]
                        user.sock.send("You are in {room_name}.".encode("utf-8"))

                        user.current_room.broadcast(f"{user.name} has joined!")
                        continue
                   
                           # seeing the users available
                   elif receive_message == '<users>':
                            # check if they are in a current room
                       if user.current_room == "None":
                           user.sock.send(f"cant list any room".encode("utf-8"))
                           continue
                            # if they are in a room show me
                       else:
                           users = user.current_room.show_users()
                           for name in user.keys():
                               user.sock.send(name.encode("utf-8"))
                               continue
                           
                           # leaving room
                   elif receive_message == '<leave>':
                       if user.current_room == "None":
                          user.sock.send(f"You cant be removed coz u are not in a current room".encode("utf-8"))
                          continue
                       
                       else:
                          user.current_room.broadcast(f"{user.name} has left".encode("utf-8"))
                          user.current_room.leave_room(user.name, user.sock.send)
                          current_room_name = "None"
                          user.current_room = "None"
                          continue
                       

                        # messagse to send then formatted with the name 
                   sent_message = f"<{user.name}> {receive_message}"
                   print(sent_message)
                          # check if the user in the room
                   if user.current_room == "None":
                       user.sock.send(f"Join a room first".encode('utf-8'))
                   else:
                       user.current_room.broadcast(sent_message)
          except Exception as error:
           print(f"Error")
     
          finally:
           user.sock.close() 
           break
          
def receive():
    while True:
        try:
             
               #waiting for a connection to come
             socket_communicate, address= server.accept()
             socket_communicate.setblocking(1)
             print(f"Connect to server")

                   # ask for name
             socket_communicate.send("What is ur name".encode("utf-8"))
             nickname =socket_communicate.recv(1024).decode("utf-8")

             new_user = User(nickname, socket_communicate, 'None', 'None')
             clients[nickname] = new_user

             socket_communicate.send(f"Welcome {nickname}".encode('utf-8'))


             thread= threading.Thread(target=handle, args=(new_user,))
             thread.start()
             
        except Exception as error:
              print(f"Error")
              break

if __name__ == "__main__":
    receive()  





     




   








            


          


     






