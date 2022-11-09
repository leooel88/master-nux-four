from . import BaseModule
from services import ReadYaml
import jinja2
import os
from services.logger import logModuleInfo,logModuleError, logModuleSuccess

class Template(BaseModule.BaseModule) :
  def __init__(self, params, logger) :
    self.name = "template"
    BaseModule.BaseModule.__init__(self, params)
    self.mainLogger = logger

  def process(self, ssh_client) :
    logModuleInfo(self.mainLogger, ssh_client.get_transport().getpeername()[0], self.name, self.params)
    print(self.params)
    with open(self.params['src']) as file :
      environment = jinja2.Environment()
      template = environment.from_string(file.read())
      finalFile = template.render(self.params['vars'])
      ssh_client.exec_command('echo \'' + finalFile + '\' > ' + self.params['dest'])
      
      logModuleSuccess(self.mainLogger, ssh_client.get_transport().getpeername()[0], self.name)