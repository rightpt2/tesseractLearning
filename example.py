## Lets see if we cant create an example file to see how we might use this
import pdf2image
from PIL import Image
import pytesseract
import re


def pdf_to_img(pdf_file):
    return pdf2image.convert_from_path(pdf_file)


def ocr_core(file):
    text = pytesseract.image_to_string(file)
    return text


def print_pages(pdf_file):
    images = pdf_to_img(pdf_file)
    lst = []
    
    for pg, img in enumerate(images):
        lst.append(ocr_core(img))
    
    return lst


def removeBlankLines(lst):
    lstSplit = lst.split('\n')
    if isinstance(lstSplit, list):
        no_blanks=[x for x in lstSplit if x not in  [' ', '']]
        return '\n'.join(no_blanks)
    else:
        return [lstSplit]

def returnDict(full_lst):
    dct = {}
    for i, item in enumerate(full_lst):
        dct[i] = removeBlankLines(item)
    
    return dct


dst = print_pages('Test_Images/oteAnalyst2.pdf')
dct = returnDict(dst)


print(dst)

with open('mynewfile.txt', 'w+') as myfile:
    for i,item in enumerate(dst):
        if i == 0:
            myfile.write(str("----Page num " + str(i)) + "----\n")
        else:
            myfile.write(str("\n----Page num " + str(i)) + "----\n")
        myfile.write(removeBlankLines(item))
