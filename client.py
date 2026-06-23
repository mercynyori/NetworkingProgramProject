import socket # networking communications
import threading # sending and receiving at the same time
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 2902))

nickname = input("Choose nicknames:")


def receive():
    while True:
        try:
            #waiting for servers message
            message = client.recv(1024).decode()
            #check for nick
            if message == "NICK":
              #send nickname
                client.send(nickname.encode()) 
            else:
                print(message)
        except:
                print(f"An error has occured")
                client.close()
                break
        
def send():
     while True:
               message = f"{nickname}: {input("")}"

               #exiting there
               if  message.lower() == '/exit':
                print("Disconnecting...")
                client.close()  # Close connection
                break


def run():
     receive_thread = threading.Thread(target=receive)
     receive_thread.start()
     write_thread = threading.Thread(target=run, args=(client,))
     write_thread.start()

if __name__ == "__main__":
    run()

      







      



  
   
