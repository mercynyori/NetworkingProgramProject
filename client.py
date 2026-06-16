import socket # networking communications
import threading # sending and receiving at the same time


class ChatClient:
    """the chat clients can connect to thr server send messages and receive messages and do them simultaneously

    """
  
    def __init__(self, host='127.0.0.1', port=5555):
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



    def send_msg(self): 
      """here we gat messages and we send to server doesnt block receiving"""
      #infite while loop to keep accepting user input and msg they send untill they quit
      while True:
        #lets get their users input first and put in a data structure
        message = input()
      if message.lower() == '/quit' or message.lower() == '/exit':
                print("Disconnecting...")
                self.client.close()  # Close connection
               break 
    

    whole_message = f"{self.nickname}: {message}"
    





    
    def receive_msg(self): 
      """ listens to messages incoming """ 
      #while loopp 
      while True:
        try: 
          message = self.client.recv



      



  
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
      except:
      pass
    print ("Disconnected from server")

#connecting and running
client = ChatClient()
if client.connect(host, port, username):
    client.run()
else:
print("Failed to connect to server")

