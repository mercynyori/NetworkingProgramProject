import socket # networking communications
import threading # sending and receiving at the same time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 2120))

nickname = input("Choose nickname: ")

def receive(): 
      """ listens  continuosly for an any incoming messages to the user """ 
      #while loopp 
      while True:
        try: 
          message = sock.recv(1024).decode("utf-8")
        
        #  checking what type of message from the sever
          if message == "What is ur name":
                sock.send(nickname.encode("utf-8"))

        except Exception as error:
         print("User disconnected from the server")
         sock.close()

         break


    

def send():
       """here we gat messages and we send to server doesnt block receiving"""
      #infite while loop to keep accepting user input and msg they send untill they quit
       while True:
         try:
               message = input("")

               #exiting there
               if  message.lower() == '/exit':
                    print("Disconnecting...")
                    sock.close()  # Close connection
                    break
               sock.send(message.encode("utf-8")) 
 
         except Exception as error:
                 print("Connection lost")
                 sock.close()
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

      







      



  
   
