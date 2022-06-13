#!/usr/bin/env python3
import os
import json
import requests

# descriptionsFolder  = r"C:\Users\Laptop72\Desktop\DesarolloGit\automating-real-world-tasks-pytho\modulo4\descripciones_test"
descriptionsFolder  = "/home/student-04-7a032a992120/supplier-data/descriptions/"
url = "http://localhost/fruits/"
for file in os.listdir(descriptionsFolder):
    if file.endswith(".txt"):
        # crear variable tipo json para almacenar con la estructura name, weight (in lbs), description
        data = {}
        with open(os.path.join(descriptionsFolder,file), 'r') as texto:
            lineas = texto.readlines()
            data['name'] = lineas[0].strip()
            data['weight'] = int(lineas[1].replace(" lbs",""))
            data['description'] = lineas[2]
            data['image_name'] = file.replace(".txt",".jpeg")
            # print(data)
            # convert data to json variable
            # json_data = json.dumps(data)
            # send data to server
            r = requests.post(url, data=data)
            print(r.status_code)
