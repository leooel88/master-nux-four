from . import apt
from . import copy
from . import template
from . import service
from . import sysctl
from . import command

class ModuleManager:
  def __init__(self):
    pass

  def process(self, module_name, params, ssh_client, logger):
    if module_name == 'apt':
      module = apt.Apt(params, logger)
    elif module_name == 'copy':
      module = copy.Copy(params, logger)
    elif module_name == 'template':
      module = template.Template(params, logger)
    elif module_name == 'service':
      module = service.Service(params, logger)
    elif module_name == 'sysctl':
      module = sysctl.Sysctl(params, logger)
    elif module_name == 'command':
      module = command.Command(params, logger)
    module.process(ssh_client)