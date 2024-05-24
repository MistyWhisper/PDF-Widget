import os
from PyPDF2 import PdfWriter as pfw
from PyPDF2 import PdfReader as pfr
from tkinter import filedialog
from urllib.parse import unquote_plus

def encrypt(pdfPath, pwd):
    # :param pdfPath -> path of PDF

    pdfPath = os.path.abspath(pdfPath)

    pdf = pfr(open(pdfPath, 'rb'))
    write = pfw()
    write.encrypt(pwd)
    for page in pdf.pages:
        write.add_page(page)

    # 将加密后的内容写入到新的 PDF 文件中
    pdf_Path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        initialfile="encrypted_" + os.path.basename(pdfPath),
        filetypes=[("PDF 文件", "*.pdf"), ("所有文件", "*.*")]
    )
    pdf_Path = pdf_Path.replace("/", "\\\\")

    with open(pdf_Path, 'wb') as f:
        write.write(f)

'''
if "__name__" == "__main__":
    encrypt("test3.pdf")
'''