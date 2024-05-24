import os
from docx2pdf import convert as ct
from urllib.parse import unquote_plus
from tkinter import filedialog

def createPDF(wordPath, pdfPath):
    """
    Convert Word document into PDF.
    
    :param wordPath: Path of the Word document.
    :param pdfPath: Path of the output PDF.
    """
    wordPath = os.path.abspath(wordPath)

    pdf_Path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        initialfile=pdfPath,
        filetypes=[("PDF 文件", "*.pdf"), ("所有文件", "*.*")]
    )
    pdf_Path = pdf_Path.replace("/", "\\\\")

    ct(wordPath, pdf_Path)

'''
if __name__ == "__main__":
    createPDF("test1.docx", "test2.pdf")
'''