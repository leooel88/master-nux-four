import argparse

def getCommandLineArguments() :
  parser = argparse.ArgumentParser()
  #-db DATABSE -u USERNAME -p PASSWORD -size 20
  parser.add_argument("-f", "--todo", help="Todos file")
  parser.add_argument("-i", "--inventory", help="Inventory file")

  parsedArguments = parser.parse_args()

  return { 'todo': parsedArguments.todo, 'inventory': parsedArguments.inventory }