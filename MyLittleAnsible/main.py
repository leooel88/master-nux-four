# from rich import print, pretty, inspect
# pretty.install()
from services import ReadYaml as Yaml
from services import sshClients
from services import commandLineArguments
from services import logger
import sys
import modules
from clients import ssh

args = commandLineArguments.getCommandLineArguments()

if not 'todo' in args or args['todo'] == None or args['todo'] == '' :
  print('ERROR : No todo file passed... Couldn\'t operate')
  exit()
elif not 'inventory' in args or args['inventory'] == None or args['inventory'] == '' :
  print('ERROR : No inventory file passed... Couldn\'t operate')
  exit()

todos = Yaml.ReadYaml(args['todo'])
inventory = Yaml.ReadYaml(args['inventory'])

mainLogger = logger.build_logger('main')

hostsAddresses = sshClients.getHostList(inventory)

mainLogger.info('processing [' + str(len(todos)) + '] tasks on hosts: ' + hostsAddresses)

moduleManager = modules.ModuleManager()

sshClients = sshClients.buildSshClientArray(inventory['hosts'])

# sshClient = ssh.SshClient()
# sshClient.connectWithPassword('10.0.0.4', 22, 'mla', 'MyLittleAnsible2018!')

i = 0
for todo in todos:
  for sshClient in sshClients :
    moduleManager.process(todo["module"], todo["params"], sshClient.client, mainLogger)
    i += 1

sshClient.close()