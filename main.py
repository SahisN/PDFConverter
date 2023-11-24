from tkinter import *
import customtkinter
from tabs.imageToPdf import imageToPdf
from tabs.pdfToPdf import pdfToPdfs

# window
window = customtkinter.CTk()

# app screen size
width, height = 700, 600

# get screen width and height
x = (window.winfo_screenwidth() / 2) - (width / 2)
y = (window.winfo_screenheight() / 2) - (height / 2)

# screen apperance
# window.geometry(f"{width}x{height}")  # window size
window.geometry("%dx%d+%d+%d" % (width, height, x + 200, y))  # window size & position
window.title("PDF Converter")  # set title
window.resizable(False, False)
customtkinter.set_appearance_mode("dark")  # app theme
customtkinter.set_widget_scaling(1.1)  # set widget scaling size

# tabview - contains tab
tabview = customtkinter.CTkTabview(master=window, width=width, height=height)

# tabs
tab1_label, tab2_label = "Image To PDF", "PDF to PDFS"
tabview.add(tab1_label)
tabview.add(tab2_label)
tab1, tab2 = tabview.tab(tab1_label), tabview.tab(tab2_label)

# tab 1 - content
tab1_content = imageToPdf(tab=tab1, height=height, width=width)

# tab 2 - content
tab2_content = pdfToPdfs(tab=tab2, height=height, width=width)
tabview.pack()

window.mainloop()
