
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 17:45:18 2021

@author: prakhar.newatia
"""


import win32com.client as client
import os
#this fuction convert each doc/docx to pdf inside a particular folder 
def convertingpdf(filepath,val):
    try:
        word=client.DispatchEx("Word.Application")#DispatchEx opens a new instance (an entirely new .exe)
        in_file=os.path.abspath(filepath)
        output=filepath.replace(val,r".pdf")
        out_file = os.path.abspath(output)
        doc = word.Documents.Open(in_file)
        print ('Exporting', out_file)
        doc.SaveAs(out_file, FileFormat=17)#fileformat is the format for the pdf conversion 
        doc.Close()
        word.Quit()
    except e:
        print("some error is coming",e)
    print("doonnneee")
import os

directory = r'C:\Users\prakhar.newatia\Downloads\Translated\Shanghai'
for filename in os.listdir(directory):
    if filename.endswith("doc") :
        print(filename)
        convertingpdf(directory+"\\"+filename,".doc")
    elif filename.endswith("docx"):
    	print(filename)
    	convertingpdf(directory+"\\"+filename,".docx")