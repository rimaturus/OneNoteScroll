from PIL import Image
from pdf2image import convert_from_path
import glob
     
#---limiti crop---
#in orizzontale ho un foglio a4 dalle dimensioni: 
page_width = 11.69 #inch == 297 mm
page_height = 8.27 #inch == 210 mm
DPI = 144

left = 0
right = int(page_width * DPI)

top = int(0.265 * DPI)
bottom = int(7.696 * DPI)
#-----------------------------------------------

for file in glob.glob("*.pdf"):
    print("Working on... ",file)

    pages = convert_from_path(file, DPI)
    file_name = file.split('.')[0]
    
    width = right - left
    height = len(pages) * (bottom - top)
            
    new_im = Image.new('RGB', (width, height))
    
    count = 0
    for page in pages:
        im1 = page.crop((left, top, right, bottom))
        new_im.paste(im1, (0, (bottom-top)*count))
        count += 1

    outfile = file_name + "_long.png"
    #new_im.save(outfile, "PNG")

    image2pdf = new_im.convert('RGB')
    image2pdf.save(outfile.replace(".png",".pdf"))