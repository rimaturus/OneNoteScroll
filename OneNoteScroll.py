from PIL import Image
import glob, os

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
                    outfile = file.replace("-001.png","_long.png")
                im = Image.open(file)    
                im1 = im.crop((left, top, right, bottom))
                new_im.paste(im1, (0, (bottom-top)*count))
                count += 1
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
            outfile = file.replace("-001.png","_long.png")
        im = Image.open(file)    
        im1 = im.crop((left, top, right, bottom))
        new_im.paste(im1, (0, (bottom-top)*count))
        count += 1
#new_im.show()
new_im.save(outfile, "PNG")
#-----------------------------------------

