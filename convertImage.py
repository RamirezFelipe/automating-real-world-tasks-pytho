
import sys
import os
from PIL import Image

def convertImagesFromFolder(pathFolder= "\\", newPathFolder = "\\") -> None:
    # convert all images from this folder
    for file in os.listdir(pathFolder):
        if file.endswith("48dp"):
            print("Converting: " + file)
            im = Image.open(os.path.join(pathFolder,file)).convert('RGB')
            im = im.rotate(90).resize((128,128))
            im.save(os.path.join(newPathFolder,file) + ".jpg")
        
            
            
    


if __name__ == "__main__":
    convertImagesFromFolder(sys.argv[1], sys.argv[2])
    print("Done")
    