import socket # networking communications
import threading # sending and receiving at the same time
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 2120))

nickname = input("Choose nicknames:")



def receive(): 
      """ listens  continuosly for an any incoming messages to the user """ 
      #while loopp 
      while True:
        try: 
          message = client.recv(1024).decode()
        
        #  checking what type of message from the sever
          if message == "NICK":  
             
            #  server will ask for the name
             client.send(nickname.encode())

          elif message == "NAME_TAKEN":
             print("Name has been taken choose another one")
             nickname = input("Your new nickname :")
             client.send(nickname.encode())

          
          elif message == "NAME_EMPTY":
             print("Your name cannot be empty")
             nickname= input("New nickname: ")
             client.send(nickname.encode())
          
      
          else:
            #  print the normal message of what the other users have
                print(message)

        except:
         print("User disconnected from the server")

         break


    

def send():
       """here we gat messages and we send to server doesnt block receiving"""
      #infite while loop to keep accepting user input and msg they send untill they quit
       while True:
         try:
               message = f"{nickname}: {input("")}"

               #exiting there
               if  message.lower() == '/exit':
                    print("Disconnecting...")
                    client.close()  # Close connection
                    break
               client.send(message.encode()) 
 
         except:
                 print("Connection lost")
                 client.close()
                 break


def run():
     
     """  here the client stsrts running"""
     print(f"{nickname} welcome")
     print("Commands: /create, /join, /rooms, /users")

     receive_thread = threading.Thread(target=receive)
     receive_thread.start()

     send_thread = threading.Thread(target=send)
     send_thread.start()

if __name__ == "__main__":
    run()

      







      



  
   
