from PIL import Image
import os


#Change the below values to any whole number, in the format (width, height). Since this script maintains the proportion
# of the images these numbers only serve as the upper bound. Therefore, the new image, if not square in shape,
# will have only one dimension as you have specified while the other dimension will be smaller.
# For example,
# If an image's dimension is (400,200) and you specify size = (200,200), the new image's dimension will be (200,100)

size = (300,300)

# Specify the location of your folder of images here. The folder should contain only images.
# either use single forward slashes (/) or double backward slashes (\\) to denote going into a file (In Windows).

filePath = "C:/Users/RayM/Desktop/compressjpeg/practice"
newFilePath = ""

array = filePath.split("/")
if array[array.__len__()-1]=="":
    print "meow"
    filePath = filePath[:filePath.__len__()-1]
    newFilePath = filePath[:filePath.__len__() - array[array.__len__() - 2].__len__()] + "ResizedImages"
    print newFilePath
else:
    print filePath
    newFilePath = filePath[:filePath.__len__() - array[array.__len__() - 1].__len__()] + "ResizedImages"
    print newFilePath

#The resized images are created in a new folder called "ResizedImages", in the same directory as your current folder of images.

os.makedirs(newFilePath)
for file in os.listdir(filePath):
    image = Image.open(filePath+"/"+file)
    image.thumbnail(size, Image.ANTIALIAS)
    image.save(newFilePath+"/"+file)
