from . import BaseModule
from services.logger import logModuleInfo,logModuleError, logModuleSuccess

class Copy(BaseModule.BaseModule) :
    def __init__(self, params, logger) :
      self.name = "copy"
      BaseModule.BaseModule.__init__(self, params)
      self.mainLogger = logger

    def process(self, ssh_client) :
      logModuleInfo(self.mainLogger, ssh_client.get_transport().getpeername()[0], self.name, self.params)
      print(self.params)
      ftp_client = ssh_client.open_sftp()
      ftp_client.put(self.params["src"],self.params["dest"])
      ftp_client.close()
      
      logModuleSuccess(self.mainLogger, ssh_client.get_transport().getpeername()[0], self.name)