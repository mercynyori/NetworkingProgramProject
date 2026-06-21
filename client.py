import socket # networking communications
import threading # sending and receiving at the same time


class ChatClient:
    """the chat clients can connect to thr server send messages and receive messages and do them simultaneously

    """
  
    def __init__(self, host='127.0.0.1', port=2707):
       # connect to socket the IPv4 and TCP 
       self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       # we now connect to server and if its not running we raise the expection part
       try:
        self.client.connect((host, port))
        print(f"Connected to server at {host}:{port}")
       except Exception as error:
        print(f"Failed to connect : {error}")
        #storage for nickname, we be there ones user sets it
        self.nickname = None 



    def send_message(self): 
      """here we gat messages and we send to server doesnt block receiving"""
      #infite while loop to keep accepting user input and msg they send untill they quit
      while True:

        #lets get their users input first and put in a data structure
        message = input()

      if  message.lower() == '/exit':
                print("Disconnecting...")
                self.client.close()  # Close connection

       # send message to server
      self.client.send(message.encode()) 
       
        
   whole_message = f"{self.nickname}: {message}"
    

    

   def receive_msg(self): 
      """ listens  continuosly for an any incoming messages to the user """ 
      #while loopp 
      while True:
        try: 
          message = self.client.recv(1024).decode()

        
        #  checking what type of message from the sever
          if message == "MERCY":  
             
            #  server will ask for the name
             self.client.send(self.nickname.encode())

          elif message == "NAME_TAKEN":
             print("Name has been taken choose another one")
             self.nickname = input("Your new nickname :")
             self.client.send(self.nickname.encode())

          
          elif message == "NAME_EMPTY":
             print("Your name cannot be empty")
             self.nickname= input("New nickname: ")
             self.client.send(self.nickname.encode())
          
      
          else:
            #  print the normal message of what the other users have
             print(message)

        except
        print("User disconnected from the server")

      break

def run_client(self):
       self.accept_clients()


      #  the start buttom
       if __name__== "__main__":
        client = ChatClient()
       client.run()







      



  
    self.socket = None
    self.Username = None
    self.current_room = "General"
    self.running = False
    self.received_thread = None

def Disconnect(self):
  self.running = False
  if self.socket:
    try:
      self.socket.close()
    except OSError as e:
        print(f"Error closing socket: {e}")
    else:
    print ("Disconnected from server")

#connecting and running
client = ChatClient()
if client.connect(host, port, username):
    client.run()
else:
print("Failed to connect to server")

#creating username
username = input("Username (2-20 characters): ").strip()
    if not username or len(username) < 2:
        print("Username must be at least 2 characters")
        return
    if len(username) > 20:
        print("Username must be at most 20 characters")
        return

