# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 17:27:26 2021

@author: prakhar.newatia
"""

a=r'''from PIL import Image
import ocrmypdf
import os
 
                                    
img=Image.open(r"C:\Users\satyam.tiwari01\Desktop\imgtabletest.jpg")
img1=img.convert('RGB')
 
# Pdf_outPath=Pdf_outPath[:-3]+"pdf"
img1.save(r"C:\Users\satyam.tiwari01\Desktop\imgtabletest.pdf")
 
ocrmypdf.ocr(input_file=r"C:\Users\satyam.tiwari01\Desktop\imgtabletest.pdf", 
            output_file=r"C:\Users\satyam.tiwari01\Desktop\imgtabletest_ocr.pdf", deskew=True, use_threads =True)
 
os.remove(r"C:\Users\satyam.tiwari01\Desktop\imgtabletest.pdf")
'''
#------------------------------------------------------------
import warnings
warnings.filterwarnings("ignore")
import ocrmypdf
import fitz # PyMuPDF
import io
import os
from PIL import Image
import camelot
# file path you want to extract images from
file = r"D:\test_img.pdf"
# open the file
pdf_file = fitz.open(file)
path=r"D:\\testindir1\\"
try:
    os.mkdir(path)
except:
    pass
# iterate over PDF pages
temp_list=["GMO","kraft","items"]
l=[]
for page_index in range(len(pdf_file)):
    # get the page itself
    page = pdf_file[page_index]
    image_list = page.getImageList()
    # printing number of images found in this page
    if image_list:
        print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
    else:
        print("[!] No images found on page", page_index)
    for image_index, img in enumerate(page.getImageList(), start=1):

        # get the XREF of the image
        xref = img[0]
        # extract the image bytes
        base_image = pdf_file.extractImage(xref)
        image_bytes = base_image["image"]
        # get the image extension
        image_ext = base_image["ext"]
        # load it to PIL
        image = Image.open(io.BytesIO(image_bytes))
        # save it to local disk
        final_dir=f"{path}\\image{page_index+1}_{image_index}.{image_ext}"
        image.save(open(final_dir, "wb"))
        img=Image.open(final_dir)
        img1=img.convert('RGB')
        final1=f"{path}\\image{page_index+1}_{image_index}.pdf"
        final2=f"{path}\\image{page_index+1}_{image_index}_ocr.pdf"
        img1.save(final1)
        ocrmypdf.ocr(input_file=final1,output_file=final2, deskew=True, use_threads=True)
        os.remove(final1)
        #final3=f"{path}\\image{page_index+1}_{image_index}_ocr.txt"
        with fitz.open(final2) as doc:
            text = ""
            for page in doc:
                text += page.getText()
            text_list=text.split("\n")
            for x in text_list:
                if temp_list[0] in x or temp_list[1] in x or temp_list[2] in x :
                    l.append(x)
        tables = camelot.read_pdf(final2)
        abc=tables[0].df
        abc.to_csv(f"{path}\\image{page_index+1}_{image_index}_ocr.csv")

print(os.listdir(path))
print("done")
print()
print(l)
