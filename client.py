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
        self.client.connect(("127.0.0.1", 2707))
        print(f"Connected to server at {host}:{port}")
       except Exception as error:
        print(f"Failed to connect : {error}")
        #storage for nickname, we be there ones user sets it
        self.nickname = None 
        self.running = True



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

        except:
         print("User disconnected from the server")

         break

def run_client(self):
       print("=" * 50)
       print("CHAT CLIENT")
       print("=" * 50)
       
       self.nickname = input(("Choose your nickname:"))
       print(f"Welcome {nickname}")
       print("Commands: /create, /join, /rooms, /users")
       print("=" * 50)

          # the receiving thread the ears listening
       receive_thread = threading.Thread(target=self.receive_messages) 
       receive_thread.daemon = True
       receive_thread.start()

           # the mouth to send 
       send_thread = threading.Thread(target=self.send_messages)
       send_thread.daemon = True
       send_thread.start() 

       send_thread.join()
                             
       self.accept_clients()


      #  the start buttom
       if __name__== "__main__":
           client = ChatClient()
           client.run()







      



  
   