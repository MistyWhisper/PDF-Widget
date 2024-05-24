import random
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import simpledialog
import WordToPDF as wp
import EncryptPDF as ep
import os

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.on_close)  # 绑定窗口关闭事件
        self.__win()
        self.tk_label_lwkd39qq = self.__tk_label_lwkd39qq(self)
        self.tk_button_lwkd69mj = self.__tk_button_lwkd69mj(self)
        self.tk_button_lwkd6hjn = self.__tk_button_lwkd6hjn(self)
    
    def __win(self):
        self.title("PDF Master")
        # 设置窗口大小、居中
        width = 621
        height = 281
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)
    
    # 添加窗口关闭事件处理方法
    def on_close(self):
        self.destroy()
        
    def scrollbar_autohide(self,vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    
    def __tk_label_lwkd39qq(self,parent):
        label = Label(parent,text="点击按钮进行选择",anchor="center", )
        label.place(x=60, y=20, width=499, height=30)
        return label
    
    def __tk_button_lwkd69mj(self,parent):
        btn = Button(parent, text="Word转PDF", takefocus=False,)
        btn.place(x=240, y=100, width=139, height=38)
        return btn
    
    def __tk_button_lwkd6hjn(self,parent):
        btn = Button(parent, text="PDF加密", takefocus=False,)
        btn.place(x=241, y=160, width=137, height=39)
        return btn

class Win(WinGUI):
    def __init__(self, controller=None):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        if self.ctl:
            self.ctl.init(self)
    
    def __event_bind(self):
        self.tk_button_lwkd69mj.bind('<Button-1>',self.wordPath)
        self.tk_button_lwkd6hjn.bind('<Button-1>',self.pdfPATH)
    
    def __style_config(self):
        pass
    
    def wordPath(self, event):
        word_path = filedialog.askopenfilename(
            title="选择 Word 文件",
            filetypes=[("Word 文件", "*.docx"), ("所有文件", "*.*")]
        )

        word_path = word_path.replace("\\", "\\\\")
        word_filename = os.path.basename(word_path)
        # 找到word文件名中最后一个点的位置
        last_dot_index = word_filename.rfind(".")

        # 构建pdf文件的文件名
        pdf_filename = word_filename[:last_dot_index] + ".pdf"
        wp.createPDF(word_path, pdf_filename)
    
    def pdfPATH(self, event):
        pdf_path = filedialog.askopenfilename(
            title="选择 PDF 文件",
            filetypes=[("PDF 文件", "*.pdf"), ("所有文件", "*.*")]
        )
        pwd = simpledialog.askstring("输入密码", "请输入将要设置的密码：", show='*')
        pdf_path = pdf_path.replace("\\", "\\\\")
        ep.encrypt(pdf_path, pwd)

class Controller:
    def init(self, view):
        self.view = view

def start():
    controller = Controller()
    win = Win(controller)
    win.mainloop()

if __name__ == "__main__":
    start()
  