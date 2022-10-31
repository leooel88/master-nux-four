class BaseModule :
  name: str = "anonymous"

  def __init__(self, params) :
    self.params = params

  def process(self, ssh_client) :
    pass
