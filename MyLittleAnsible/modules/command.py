from . import BaseModule

class Command(BaseModule.BaseModule) :
  def __init__(self, params, logger) :
    self.name = "command"
    BaseModule.BaseModule.__init__(self, params)
    self.mainLogger = logger

  def process(self, ssh_client) :
    command = '#!'

    if 'shell' in self.params :
      command += self.params['shell']
    else :
      command += '/bin/bash'

    command += '\n'
    command += self.params['command']
    ssh_client.exec_command('echo \'' + command + '\' > /tmp/myLittleAnsibleTmpFile.sh')
    ssh_client.exec_command('sudo chmod +x /tmp/myLittleAnsibleTmpFile.sh')
    ssh_client.exec_command('sudo /tmp/myLittleAnsibleTmpFile.sh')
    ssh_client.exec_command('sudo rm /tmp/myLittleAnsibleTmpFile.sh')
    