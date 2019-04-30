try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os

def ocr_core(filename):
    """
    This funcion will handle the core OCR processing of images
    """
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open(filename))

    return text

print(  ocr_core('images/ocr_example_1.png'))    
print(  ocr_core('images/teste_net.jpg'))    