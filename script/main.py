from flask import Flask, render_template, request
from methods import check_into_DockerHub
from Yaml import Yaml

app = Flask(__name__, template_folder="pages")

@app.route("/", methods=["POST", "GET"])
def createContainer():
    if request.method == "POST":
      name = request.form.get("cname")
      image = request.form.get("cimage")
      ports = request.form.get("cports")
      volumes = request.form.get("cvolumes")
      envVars = request.form.get("cenvironments")

      yml = Yaml()
      yml.containerName = name
      yml.containerImage = image
      yml.containerPorts = ports
      yml.containerVolume = volumes
      yml.containerEnv = envVars

      check_into_DockerHub(image)      
      
      yml.generateYaml(yml.containerName, yml.containerImage, yml.containerPorts, yml.containerVolume, yml.containerEnv)

    return render_template("containerGenerator.html")


if __name__ == "__main__":
  app.run()
