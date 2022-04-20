import mammoth
import os
filepath=r"C:\Users\prakhar.newatia\Downloads\tosend\Data Ingestion\Geo.docx"
in_file=os.path.abspath(filepath)
f = open(in_file, 'rb')
output=filepath.replace(".docx",r".html")
out_file = os.path.abspath(output)
b = open(out_file, 'wb')
document = mammoth.convert_to_html(f)
b.write(document.value.encode('utf8'))
f.close()
b.close()
print("done")


#------ converting pdf to image

from pdf2image import convert_from_path 
  
  
# Store Pdf with convert_from_path function 
images = convert_from_path('example.pdf')
images[0].save('output.jpg', 'JPEG')#first page will be saved as this
