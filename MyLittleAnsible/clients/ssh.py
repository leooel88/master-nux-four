from paramiko import SSHClient, AutoAddPolicy

class SshClient :
  def __init__(self) :
    self.client = SSHClient()
    self.client.load_host_keys('/home/ansible/.ssh/known_hosts')
    self.client.load_system_host_keys()
    self.client.set_missing_host_key_policy(AutoAddPolicy())
  
  def connectDefault(self, hostname, port) :
    self.client.connect(hostname, port=port)

  def connectWithPassword(self, hostname, port, username, password) :
    self.client.connect(hostname, port=port, username=username, password=password)

  def connectWithSshKey(self, hostname, port, ssh_key_file) :
    self.client.connect(hostname, port=port, key_filename=ssh_key_file)

  def close(self) :
    self.client.close()
