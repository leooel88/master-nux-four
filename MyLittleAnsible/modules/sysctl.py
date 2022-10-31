from . import BaseModule

class Sysctl(BaseModule.BaseModule) :
  def __init__(self, params, logger) :
    self.name = "sysctl"
    BaseModule.BaseModule.__init__(self, params)
    self.mainLogger = logger

  def process(self, ssh_client) :
    pass