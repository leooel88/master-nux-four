from . import BaseModule
from constants import apt as CONST
from services.errors import MyDeployerError

class Apt(BaseModule.BaseModule) :
    def __init__(self, params, logger) :
        self.name = "apt"
        BaseModule.BaseModule.__init__(self, params)
        self.mainLogger = logger

    def process(self, ssh_client) :
        self.mainLogger.info('host=' + ssh_client.get_transport().getpeername()[0] + ' op=' + self.name + ' ' + str(self.params))
        if self.params["state"] == "present" :
            stdin, stdout, stderr = ssh_client.exec_command(CONST.APT_UPDATE_COMMAND)
            result = stdout.channel.recv_exit_status()
            if result != 0 :
                raise MyDeployerError()
            stdin, stdout, stderr = ssh_client.exec_command(CONST.APT_INSTALL_COMMAND + " " + self.params["name"])
            stdout.channel.recv_exit_status()
            if result != 0 :
                raise MyDeployerError()
        elif self.params["state"] == "absent" :
            stdin, stdout, stderr = ssh_client.exec_command(CONST.APT_REMOVE_COMMAND + " " + self.params["name"])
            stdout.channel.recv_exit_status()
            if result != 0 :
                raise MyDeployerError()
    