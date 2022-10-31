import yaml
#expliquer module

def ReadYaml(YamlFile):
    with open(YamlFile) as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        file = yaml.load(file, Loader=yaml.FullLoader)
        return file