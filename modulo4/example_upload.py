#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
path = "/home/student-04-1d1855d09476/supplier-data/images/"
for file in os.listdir(path):
    if file.endswith(".jpeg"):
        with open(os.path.join(path,file), 'rb') as opened:
            r = requests.post(url, files={'file': opened})
