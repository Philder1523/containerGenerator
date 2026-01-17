import yaml
import io  

class Yaml():
    def __init__(self, containerName: str, containerImage: str, containerPorts: str, containerVolume: str, containerEnv: str):
        self.containerName = containerName
        self.containerImage = containerImage
        self.containerPorts = containerPorts
        self.containerVolume = containerVolume
        self.containerEnv = containerEnv

    def generateYaml(self, name, image, ports, volume, env):
        yml = Yaml()
        yml.containerName = name
        yml.containerImage = image
        yml.containerPorts = ports
        yml.containerVolume = volume
        yml.containerEnv = env

        data = {"version" : '3.8', 
            "services" : {
            "webapp" : {
                "container_name" : name,
                "image" : image,
                "ports" : [ports],
                "volumes" : [".:/%s", volume],
                "environment" : [env],
                "restart": "unless-stopped"
                }
            }
        }
        try:
            with io.open("compose.yaml", "w", encoding="utf8") as output:
                yaml.dump(data, output, sort_keys=False, default_flow_style=False, allow_unicode=True)
        except Exception as error:
            print(error)
            return data