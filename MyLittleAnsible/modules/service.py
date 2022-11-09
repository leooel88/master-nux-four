from . import BaseModule
from constants import service as CONST
from constants import state
from services.logger import logModuleInfo,logModuleError, logModuleSuccess

class Service(BaseModule.BaseModule) :
  def __init__(self, params, logger) :
    self.name = "service"
    BaseModule.BaseModule.__init__(self, params)
    self.mainLogger = logger

  def process(self, ssh_client) :
    logModuleInfo(self.mainLogger, ssh_client.get_transport().getpeername()[0], self.name, self.params)
    print(self.params["name"])
    print(self.params["state"])
    ssh_client.exec_command(CONST.APT_UPDATE_COMMAND)
    ssh_client.exec_command(CONST.SERVICE_BASE_COMMAND + " " + state.State[self.params["state"]] + " " + self.params["name"])
    
    logModuleSuccess(self.mainLogger, ssh_client.get_transport().getpeername()[0], self.name)