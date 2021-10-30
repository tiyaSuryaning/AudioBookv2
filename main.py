from tkinter import *
from tkinter.filedialog import askopenfile
import PyPDF2
import pyttsx3

speak = pyttsx3.init()

window = Tk()
window.title('Book Reader')
window.geometry("600x600")
window.configure(bg = "#cacac8")

def open_file():
    open_file.file = askopenfile(parent=window, mode='rb', title="Choose file", filetype=[("pdf file", "*.pdf")])

def start_reading():
    if open_file.file:
        text_pdf = PyPDF2.PdfFileReader(open_file.file)
        pages = text_pdf.numPages
        for num in range(0, pages):
            page = text_pdf.getPage(0)
            page_content = page.extractText()
            speak.say(page_content)
            speak.runAndWait()

def stop_reading():
    speak.stop()

canvas = Canvas(
    window,
    bg = "#cacac8",
    height = 600,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    300.0, 339.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    345.0, 142.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#c5c4c2",
    highlightthickness = 0,
    )

entry0.place(
    x = 203.0, y = 127,
    width = 284.0,
    height = 28)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = open_file,
    relief = "flat")

b0.place(
    x = 89, y = 127,
    width = 100,
    height = 30)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    419.0, 249.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#f1eeee",
    highlightthickness = 0)

entry1.place(
    x = 269, y = 234,
    width = 300,
    height = 28)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = start_reading,
    relief = "flat")

b1.place(
    x = 257, y = 173,
    width = 85,
    height = 23)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = stop_reading,
    relief = "flat")

b2.place(
    x = 251, y = 300,
    width = 99,
    height = 33)

window.resizable(False, False)
window.mainloop()