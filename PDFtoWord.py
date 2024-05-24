import os
from pdf2docx import Converter
from tkinter import filedialog

def createWord(pdfPath, wordPath):
    """
    Convert Word document into PDF.
    
    :param wordPath: Path of the Word document.
    :param pdfPath: Path of the output PDF.
    """
    pdfPath = os.path.abspath(pdfPath)

    word_Path = filedialog.asksaveasfilename(
        defaultextension=".docx",
        initialfile=wordPath,
        filetypes=[("Word 文件", "*.docx"), ("所有文件", "*.*")]
    )
    word_Path = word_Path.replace("/", "\\\\")

    # Create Converter object
    converter = Converter(pdfPath)

    # Convert PDF to Word
    converter.convert(word_Path, start=0, end=None)

    # Close Converter object
    converter.close()

'''
if __name__ == "__main__":
    createPDF("test1.pdf", "test2.docx")
'''