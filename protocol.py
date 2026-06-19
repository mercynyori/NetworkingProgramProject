class ChatRoom:
  def __init__(self, name: str, creator: str):
    self.name = name
    self.creator = creator
    self.members: Set[str] = {creater}
