from . import BaseModule
from services.logger import logModuleInfo,logModuleError, logModuleSuccess

class Command(BaseModule.BaseModule) :
  def __init__(self, params, logger) :
    self.name = "command"
    BaseModule.BaseModule.__init__(self, params)
    self.mainLogger = logger

  def process(self, ssh_client) :
    logModuleInfo(self.mainLogger, ssh_client.get_transport().getpeername()[0], self.name, self.params)
    command = '#! '

    if 'shell' in self.params :
      command += self.params['shell']
    else :
      command += '/bin/bash'

    command += '\n'
    command += self.params['command']

    ssh_client.exec_command('echo \'' + command + '\' > /tmp/myLittleAnsibleTmpFile.sh')
    ssh_client.exec_command('sudo chmod +x /tmp/myLittleAnsibleTmpFile.sh')
    ssh_client.exec_command('sudo /tmp/myLittleAnsibleTmpFile.sh')

    stdin, stdout, stderr = ssh_client.exec_command('sudo rm /tmp/myLittleAnsibleTmpFile.sh')
    stderr = stderr.read().decode('ascii')
    result = stdout.channel.recv_exit_status()
    if result != 0 or stderr :
      logModuleError(self.mainLogger, ssh_client.get_transport().getpeername()[0], self.name, stderr)
      return

    logModuleSuccess(self.mainLogger, ssh_client.get_transport().getpeername()[0], self.name)
    