
import pytesseract
import cv2
import csv
from PIL import Image

image_path = 'table_image.png'


image = Image.open(image_path) # Load image and perform OCR
extracted_text = pytesseract.image_to_string(image)


extracted_text = extracted_text.strip().replace('\n\n', '\n') # Clean up text


rows = extracted_text.split('\n')  # Split text into rows


table_data = [] # Split rows into columns
for row in rows:
    table_data.append(row.split('\t'))


csv_path = 'output.csv' # Save table data to CSV
with open(csv_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(table_data)

print('Saved table data to CSV file:', csv_path)