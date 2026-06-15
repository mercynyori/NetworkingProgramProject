import socket # networking communications
import threading # sending and receiving at the same time


class ChatClient:
  def __init__(self) :
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

