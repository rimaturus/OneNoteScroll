from PIL import Image
from pdf2image import convert_from_path
import glob
     
#---limiti crop---
# misurati su file convertito con DPI = 144
top = 38
left = 0
right = 1684 
bottom = 1108
#-----------------

for file in glob.glob("*.pdf"):
    pages = convert_from_path(file, 144)
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
    new_im.save(outfile, "PNG")

    image2pdf = new_im.convert('RGB')
    image2pdf.save(outfile.replace(".png",".pdf"))