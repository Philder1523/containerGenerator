'''
Applicazione in grado di creare e scaricare un file yaml, che può essere utilizzato dall'utente per eseguire in un ambiente isolato la propria applicazione
'''

import yaml
import docker
import os
import io
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="pages")
client = docker.from_env()

@app.route("/", methods=["POST", "GET"])
def createContainer():
    if request.method == "POST":
      #nome del container
      name = request.form.get("cname")
      #immagine del container
      image = request.form.get("cimage")
      #porte del container
      ports = request.form.get("cports")
      #volumi persistenti del container
      volumes = request.form.get("cvolumes")
      #variabili di ambiente del container
      envVars = request.form.get("cenvironments")
      client.images.get_registry_data("nginx")

      '''while str(os.system(f"docker manifest inspect {image};")).find("architecture") == -1:
          print("l'immagine non esiste nel registro di docker")
          image = input("scegli un'altra immagine --> ")
      client.images.get_registry_data("nginx")'''
      
      print(f"l'immagine {image} sta per essere scaricata")
      os.system(f"docker --quiet pull {image};")
      
      data = {"version" : '3.8', 
              "services" : {
                "webapp" : {
                  "container_name" : name,
                  "image" : image,
                  "ports" : [str(ports)],
                  "volumes" : [str(volumes)],
                  "environment" : [envVars]
                  }
                }
              }

      #os.system("if which docker; then docker container create {0}; else sudo apt update && sudo apt-get install docker-ce docker fi", name)
      with io.open("container.yaml", "w", encoding="utf8") as output:
        yaml.dump(data, output, sort_keys=False, default_flow_style=False, allow_unicode=True)
      
      with io.open("container.yaml", "r") as stream:
        data_loaded = yaml.safe_load(stream)

    return render_template("containerGenerator.html")


if __name__ == "__main__":
  app.run()
