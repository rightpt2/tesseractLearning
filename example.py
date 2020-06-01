## Lets see if we cant create an example file to see how we might use this
import pdf2image
from PIL import Image
import pytesseract


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

dst = print_pages('Test_Images/oteAnalyst.pdf')
print(dst)