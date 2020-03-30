import glob
import cv2
  
image_counter = 1
#path="C:\Users\HASSAN\OneDrive\CompVision\Textmine\rotating"

images = glob.glob("./rotating/*.jpg")

for image in images:
        img=cv2.imread(image,1)

        x=1550
        y=688
        w=358
        h=4228
        

        crop_img = img[y:y+h, x:x+w]
        filename = "./Cropped/crop"+str(image_counter)+".jpg"
        #cv2.imshow('windo',crop_img)
        cv2.imwrite(filename,crop_img)
        image_counter = image_counter + 1

        cv2.waitKey(0)
        cv2.destroyAllWindows()
