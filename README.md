# OneNoteScroll
Create one scrollable pdf file from a pdf-printed OneNote endless file

# How to use it:
1) Create a folder with all the .pdf files 
2) Launch the program in the same folder as the files
3) It will output 1 file for each input: ***"<input_file_name>_long.pdf"***

Extra:
4) Uncomment ***row 36*** to output also ***"<input_file_name>_long.png"*** 

# Dependencies:
It uses:
  1) pdf2image
  2) Image from PIL (Pillow)
  3) Poppler (for Windows): (https://pypi.org/project/python-poppler/)
