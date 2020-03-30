import glob
from PIL import Image
import pytesseract

images = glob.glob("./Cropped/*.jpg")
for image in images:
    img = Image.open(image)
    data = pytesseract.image_to_string(img, lang='eng', config='--psm 6')
    print(data,file=open('extract-text.txt',"a"))
