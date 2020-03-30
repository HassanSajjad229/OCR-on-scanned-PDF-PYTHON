# OCR-on-scanned-PDF-PYTHON
Text is extracted from scanned PDF document using OCR in python.The pytesseract,opencv and pdf2image libraries are used.
Following steps need to be followed to extract text
1# Convert the pdf file to the images.
2# Images are rotated at a designated angle so text extraction would be feasible.
3# Use width,height,top,right cordinates to crop the designated part of image need for extraction.
4# Peform OCR on the images to extract the text.
5# Save the extracted text to a file.
