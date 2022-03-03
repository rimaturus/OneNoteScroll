from PIL import Image
from pdf2image import convert_from_path
import os, glob

for file in glob.glob("*.pdf"):
    pages = convert_from_path(file, 144)
    file_name = file.split('.')[0]
    count = 0
    for page in pages:
        image_name = file_name + '-' + str(count) + ".png"
        page.save(image_name, 'PNG')
        count += 1
        
#input = "MES_20210303.pdf"
#output pdf2png =  "MES_20210303-1.png" "MES_20210303-2.png" ...

#---limiti crop---
# misurati su file convertito con DPI = 144
top = 38
left = 0
right = 1684 
bottom = 1108
#-----------------

lista = []
n_page = 0
count = 0

for file in glob.glob("*.png"):
    radice = file.split('-')[0]
    
    if(lista == []):
        lista.append(radice)
        
    if(radice in lista): #scorro pagine
        n_page += 1
        
    else: #cambio file
        #qui ho scorso tutti i file con la stessa radice
        # Inizio processo di restauro file onenote
        width = right - left
        height = n_page * (bottom - top)
            
        new_im = Image.new('RGB', (width, height))
        
        for file in glob.glob("*.png"):
            if(file.split('-')[0] in lista):
                if(count == 0):
                    outfile = file.replace("-0.png","_long.png")
                im = Image.open(file)    
                im1 = im.crop((left, top, right, bottom))
                new_im.paste(im1, (0, (bottom-top)*count))
                count += 1
                os.remove(file)
        #new_im.show()
        new_im.save(outfile, "PNG")
        #-----------------------------------------
        
        lista.clear()
        lista.append(radice)
        n_page = 1
        count = 0

#unisco pagine dell'ultimo file radice
width = right - left
height = n_page * (bottom - top)
    
new_im = Image.new('RGB', (width, height))

for file in glob.glob("*.png"):
    if(file.split('-')[0] in lista):
        if(count == 0):
            outfile = file.replace("-0.png","_long.png")
        im = Image.open(file)    
        im1 = im.crop((left, top, right, bottom))
        new_im.paste(im1, (0, (bottom-top)*count))
        count += 1
        os.remove(file)
#new_im.show()
new_im.save(outfile, "PNG")
#-----------------------------------------

for file in glob.glob("*.png"):
    image = Image.open(file)
    image2pdf = image.convert('RGB')
    image2pdf.save(file.replace(".png",".pdf"))
