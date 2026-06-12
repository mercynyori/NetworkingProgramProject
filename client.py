import socket
import sys
import time
import threading
import select

class ChatClient:
  def __init__(Self) :
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

