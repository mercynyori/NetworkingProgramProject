
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

# rooms created a dictionary is created when u enter u enter directly
       self.rooms = {"Home": []} 
    # track the rooms that they are in
       self.user_rooms = {}  

       print("=" * 50 )
       print(f"Server is listening on 27.0.0.1, 2707")
       print("=" * 50 )
  


     def broadcasting(self, message,sender=None):
      """ here we send messages to every client """
     #loop through all the clients that we got
      for client in self.client:
           try:
          #sending message if fails client disconnected
                client.send(message)
           except Exception as error:
               print(f"No able to send to client:{error}")

    
     def broadcast_to_a_specific_room(self, message, room,sender=None):
       """Broadcasting to a specific roomdepending on what the user used"""
       if room  in self.room:
            for client in self.room[room_name]:
                if client != sender:
                    try:
                        client.send(message)
                    except:
                        self.remove(client)

     def nickname_getting(self, client):
          if client in self.clients:
             return self.nicknames[self.clients.index(client)]
          return None

     def remove_client(self,client):
      # here we remove the client once they disconnect
      """here we clear the client when they disconnect so that we dont have memory leaks"""
      if client in self.clients:
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
      while True:
          try: # infite loop on and on of receiving thr clients message
               message = client.recv(1024).decode()
                 # once u get the msg u send to everyone
               if message: 
                  self.broadcast(message, sender_client=client)
               else:
                  self.remove(client)


                   # the user is able to create a chat room
               if message.startswith(" /create"):
                   parts= message.split(" ")
                   if len(parts) > 1:
                         room_name = parts[1]

                         if room_name in self.rooms:
                             client.send(f"Room name taken choose another one!".encode())

                         else:
                            self.rooms[room_name] = []
                            client.send(f"Room has been created".encode())

                            self.rooms[room_name].append(client)
                            self.user_rooms[client] = room_name
                            client.send(f"You have joined '{room_name} welcome!".encode())


                   else:
                        client.send("This is a wrong usage of /create <roomname>".encode())

                    # joining a new chatroom
               if message.startswith("/join"):
                  parts=message.split(" ")
                  if len(parts) > 1:
                     room_name = parts[1]

                       # removing from anyother room
                     if room_name in self.room: # check if the room is in the server
                          if client in self.user_room: # check if the clinet is in the room
                              old = self.ser_room[client] #  safe check 
                              self.room(old).remove(client) #  if they are there we remoeve them
  
                              # then now they join their new chat room
                          self.rooms[room_name].append(client)   #adds the user to the new room
                          self.user_room[client]= room_name  #stores the user in the new room
                          client.send(f"You have now joined {room_name}".encode())

                            # get the users in the room
                          users=[] 
                          for i in self.rooms(room_name):
                              name = self.get_nickname(c)

                              if name:
                                 user.append(name)
                          if users:
                               client.send(f"Users are : {', '.join(users)}".encode())
                     else:
                          client.send(f"Room is nonexistent").encode()

                  else:
                      client.send(f"This is the wrong usage of : /join <room_name>".encode())


               if message.startswith("/rooms"):
                   client.send(f"Rooms: {', '.join(self.rooms)}".encode())

          except:  # if client has left the room
            self.remove_client(client)
            break
                    

     def accept_client(self):
      """ Here the server is constantly waiting for someone to come forever, asks for their name  then accepts"""
      while True:
         # wait for the client to come
       client, address = self.server.accept()
            #  ask for there name 
       client.send("NICK".encode())
       while True:
            # ask for the name and if in nicknane tell its gone
          if nickname in self.nicknames:
           nickname = client.recv(1024).decode().strip() 
           client.send("NAME_GONE".encode())
             # ask again 
           client.send("NICK".encode())
          continue
       else:
          break 


# add client to the chat
      self.client.append(client)
      self.nickname.append(nickname) #  unique names
      self.broadcast(f"{nickname} welcome!" . encode())


         # added to the default room once accepted
      self.rooms[DEFAULT_ROOM].append(client)

        # always remember that the client is there in the room
      self.user_rooms[client] = "DEFAULT_ROOM"

      client.send(f"{nickname} is in {DEFAULT_ROOM} welcome !".encode())
      client.send(f"Commands: /create, /join, /users, /rooms".encode())


       # create the thread to listen which allows other users to join
      thread = threading.Thread(target=self.handle_client, args=(client,))
      thread.start

     def run(self):
        self.accept_clients()

    
    # start button for the server program
        if __name__ == "__main__":
              server = ChatServer()
              server.run()




   








            


          


     






