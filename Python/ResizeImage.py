from PIL import Image
import os

# This script requires you to install Pillow library, from here: https://pypi.python.org/pypi/Pillow/2.7.0.
# For a 32-bit Windows computer, download Pillow-2.7.0.win32-py2.7.exe (md5) from the list of options.
# Double click to install.


# This is where you specify the new dimensions for all your images. Change the values to any whole number, in the format 
# (width, height). 
# Since this script maintains the proportion of the images these numbers only serve as the upper bound. Therefore the 
# new image, if not square in shape, will have only one dimension equal to what you have specified while the other dimension
# will be smaller.
#
# For example, if an image's dimension is (400,200) and you type size = (200,200), the new image's dimension will be (200,100).

size = (300,300)


# Specify the location of your folder of images here. The folder should not contain any non-image files.
# Either use single forward slashes (/) or double backward slashes (\\) to denote going into a file (In Windows).

print "Enter location of folder of images"
filePath = raw_input()#"C:/Users/RayM/Desktop/compressjpeg/practice"
newFilePath = ""

if filePath.__contains__("/"):
    array = filePath.split("/")
else:
    array = filePath.split("\\")
    
if array[array.__len__()-1]=="":
    filePath = filePath[:filePath.__len__()-1]
    newFilePath = filePath[:filePath.__len__() - array[array.__len__() - 2].__len__()] + "ResizedImages"
    print newFilePath
else:
    print "Given file path: "+filePath
    newFilePath = filePath[:filePath.__len__() - array[array.__len__() - 1].__len__()] + "ResizedImages"
    print "Location of resized images: "+newFilePath


#The resized images are created in a new folder called "ResizedImages", in the same directory as your current folder of images.

os.makedirs(newFilePath)
for file in os.listdir(filePath):
    image = Image.open(filePath+"/"+file)
    image.thumbnail(size, Image.ANTIALIAS)
    image.save(newFilePath+"/"+file)
