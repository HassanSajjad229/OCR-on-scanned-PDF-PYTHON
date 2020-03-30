from pdf2image import convert_from_path
 
PDF_file = 'sample.pdf'
pages = convert_from_path(PDF_file, 500) 

image_counter = 1

for page in pages: 
   
    filename = "Retrieve/page_"+str(image_counter)+".jpg"
      
    # Save the image of the page in system 
    page.save(filename, 'JPEG') 
  
    # Increment the counter to update filename 
    image_counter = image_counter + 1
 

