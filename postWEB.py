import os
import requests
import json

# recorrer carpetas
# folder = "/data/feedback"
folder = r"C:\Users\Laptop72\Desktop\DesarolloGit\automating-real-world-tasks-pytho\data"
ip = "http://34.67.143.243/feedback/"
for file in os.listdir(folder):
    # abrir archivos txt
    if file.endswith(".txt"):
        with open(os.path.join(folder,file), "r") as f:
            lineas = f.readlines()
            message = {}
            message["title"] = lineas[0].replace("\n", "")
            message["name"] = lineas[1].replace("\n", "")
            message["date"] = lineas[2].replace("\n", "")
            message["feedback"] = lineas[3].replace("\n", "")
        # enviar datos al servidor with requests post
        r = requests.post(ip, data = message)
        print(r.status_code)
