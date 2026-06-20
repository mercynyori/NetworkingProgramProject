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
    
    

