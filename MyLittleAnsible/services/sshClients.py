from clients import ssh

def buildSshClientArray(hosts) :
  result = []
  keys = hosts.keys()
  i = 0

  for key in keys :
    result.append(ssh.SshClient())
    if 'ssh_user' in hosts[key] and 'ssh_password' in hosts[key] and not 'ssh_key_file' in hosts[key]:
      result[i].connectWithPassword(hosts[key]['ssh_address'], hosts[key]['ssh_port'], hosts[key]['ssh_user'], hosts[key]['ssh_password'])
    elif 'ssh_key_file' in hosts[key] and not 'ssh_user' in hosts[key] and not 'ssh_password' in hosts[key] :
      result[i].connectWithSshKey(hosts[key]['ssh_address'], hosts[key]['ssh_port'], hosts[key]['ssh_key_file'])
    else :
      result[i].connectDefault(hosts[key]['ssh_address'], hosts[key]['ssh_port'])
    i =+ 1
      
  return result

def getHostList(inventory) :
  hostsAdresses = ''

  keys = inventory['hosts'].keys()
  for key in keys :
    hostsAdresses += inventory['hosts'][key]['ssh_address'] + ', '

  hostsAdresses = hostsAdresses[:len(hostsAdresses) - 2]

  return hostsAdresses