# protocol and commands design
MERCY = "MERCY"
USERNAME_TAKEN = "USERNAME TAKEN"

#USER COMMANDS 
CMD_CREATE= "CREATE"
CMD_JOIN= "JOIN"
CMD_INVITE="INVITE"
CMD_USERS="USERS"
CMD_ROOMS="ROOMS"
CMD_ACCEPT="ACCEPT"
CMD_LEFT="LEFT"

#THE CONFIG SETTINGS
HOST = 127.0.0.1
PORT = 2707
DEFAULT_ROOM = "Home"
BUFFER_SIZE = 1024

class ChatRoom:
  def __init__(self, name: str, creator: str):
    self.name = name
    self.creator = creator
    self.members: Set[str] = {creater}
    self.created_at = datetime.now()

def add_member(self, username: str) -> bool:
  if username not in self.members:
    self.members.add(username)
    return True
  return False
  
  def remove_member( self, username: str) -> bool:
    if username in self.members:
      self.members.remove(username)
      return True
    return False
  def add_message(self, sender: str, content: str):
    msg = {
      "sender": sender,
      "content": content,
      "timestamp": datetime.now().isoformat()
    }
    self.meassage_history.append(msg)
    if len(self.
    
    

