from PIL import Image
import glob

image_counter = 1
#path="C:\Users\HASSAN\OneDrive\CompVision\Textmine\rotating"
images = glob.glob("./Retrieve/*.jpg")
image_counter = 1
for image in images:
        img = Image.open(image)
        rotated= img.rotate(0.87)
        filename = "./rotating/rotate"+str(image_counter)+".jpg"
        #save_dir = './Rotate-images
    # Save the image of the page in system 
        rotated.save(filename,'JPEG') 
        #rotated.show()
  
    # Increment the counter to update filename 
        image_counter = image_counter + 1
        

 
