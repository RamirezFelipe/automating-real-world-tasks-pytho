#!/usr/bin/env python3
import sys
import os
from PIL import Image

def convertImagesFromFolder(pathFolder= "\\", newPathFolder = "\\") -> None:
    # convert all images from this folder
    for file in os.listdir(pathFolder):
        if file.endswith(".tiff"):
            print("Converting: " + file)
            im = Image.open(os.path.join(pathFolder,file)).convert('RGB')
            im = im.resize((600,400))
            im.save(os.path.join(newPathFolder,file.replace(".tiff",".jpeg")))






if __name__ == "__main__":
    # convertImagesFromFolder(sys.argv[1], sys.argv[2])
    #student-04-7a032a992120
    imagesFolder = "/home/student-04-7a032a992120/supplier-data/images/"
    newImagesFolder = "/home/student-04-7a032a992120/supplier-data/images/"
    convertImagesFromFolder(imagesFolder, newImagesFolder)
    print("Done")
