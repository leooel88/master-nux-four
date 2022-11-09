from . import BaseModule
from services.logger import logModuleInfo,logModuleError, logModuleSuccess
from constants import apt as CONST
from services.errors import MyDeployerError

class Apt(BaseModule.BaseModule) :
    def __init__(self, params, logger) :
        self.name = "apt"
        BaseModule.BaseModule.__init__(self, params)
        self.mainLogger = logger

    def process(self, ssh_client) :
        logModuleInfo(self.mainLogger, ssh_client.get_transport().getpeername()[0], self.name, self.params)
        if self.params["state"] == "present" :
            stdin, stdout, stderr = ssh_client.exec_command(CONST.APT_UPDATE_COMMAND)
            stderr = stderr.read().decode('ascii')
            result = stdout.channel.recv_exit_status()
            if result != 0 or stderr.startswith('E:') :
                logModuleError(self.mainLogger, ssh_client.get_transport().getpeername()[0], self.name, stderr)
                return

            stdin, stdout, stderr = ssh_client.exec_command(CONST.APT_INSTALL_COMMAND + " " + self.params["name"])
            stderr = stderr.read().decode('ascii')
            stdout.channel.recv_exit_status()
            if result != 0 or stderr.startswith('E:') :
                logModuleError(self.mainLogger, ssh_client.get_transport().getpeername()[0], self.name, stderr)
                return
        elif self.params["state"] == "absent" :
            stdin, stdout, stderr = ssh_client.exec_command(CONST.APT_REMOVE_COMMAND + " " + self.params["name"])
            stdout.channel.recv_exit_status()
            if result != 0 or stderr.startswith('E:') :
                logModuleError(self.mainLogger, ssh_client.get_transport().getpeername()[0], self.name, stderr)
                return

        logModuleSuccess(self.mainLogger, ssh_client.get_transport().getpeername()[0], self.name)
