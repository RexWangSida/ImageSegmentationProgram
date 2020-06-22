from tkinter import *
import tkinter.font as tkFont
from tkinter import filedialog
from PIL import Image, ImageTk
from algorithms import segmentation
import os
SAVEPATH = ""
READPATH = ""
def start():
    def setSaving():
        global SAVEFILE
        SAVEPATH =  filedialog.askdirectory()
        dirLabel = Label(panel, text="  Location to save image:   " + SAVEPATH)
        dirLabel.grid(row = 5, column = 2)

    def loadImg():
        global READPATH
        READPATH =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        filenameLabel = Label(panel, text="  Image to be segmented:   " + READPATH)
        filenameLabel.grid(row = 1, column = 2)
        image = Image.open(READPATH)
        displayImage = image
        while displayImage.size[0] > 400 or displayImage.size[1] > 400:
            displayImage = displayImage.resize((int(displayImage.size[0]//2),int(displayImage.size[1]//2)))
        displayPic = ImageTk.PhotoImage(displayImage)
        image1 = Label(panel, image=displayPic)
        image1.image = displayPic
        image1.place(relx=0.3, rely=0.6, anchor=CENTER)

    def process():
        segmentation(READPATH, int(kEntry.get()), os.path.join(SAVEPATH,os.path.basename(READPATH)))

    def again():
        panel.destroy()
        start()

    panel = Tk()
    panel.title("Image Segmentation Processor")
    panel.geometry("800x800")
    spacer1 = Label(panel, text="          ")
    spacer1.grid(row = 0, column = 0)
    imageButton = Button(panel, text="Select Input Image", command=loadImg)
    imageButton.grid(row = 1, column = 1)
    kText = Label(panel, text="Number of Clusters(k): ")
    spacer2 = Label(panel, text="          ")
    spacer2.grid(row = 2, column = 0)
    kText.grid(row = 3, column = 1)
    kEntry = Entry(panel,)
    kEntry.grid(row = 3, column = 2)
    spacer3 = Label(panel,text="          ")
    spacer3.grid(row = 4, column = 0)
    saveButton = Button(panel, text="Select Output location", command=setSaving)
    saveButton.grid(row = 5, column = 1)
    spacer4 = Label(panel, text="          ")
    spacer4.grid(row = 6, column = 0)
    submit = Button(panel, text="Submit", command=process)
    submit.grid(row = 7, column = 2)
    submit = Button(panel, text="Process Another Image", command=again)
    submit.grid(row = 7, column = 3)

def destroyall():
    global window
    window.destroy()

window = Tk()
window.title("Image Segmentation Processor")
window.geometry("600x600")
startLabel1 = Label(text="Image Segmentation Processor",font=tkFont.Font(family='Impact', size=20))
startLabel2 = Label(text="based on K-Means Clustering Algorithm",font=tkFont.Font(family="Lucida Grande", size=10))
startLabel1.place(relx=0.5, rely=0.2, anchor=CENTER)
startLabel2.place(relx=0.5, rely=0.3, anchor=CENTER)
creator = Label(text="Creator: Sida Wang",font=tkFont.Font(family="Lucida Grande", size=10))
creator .place(relx=0.5, rely=0.4, anchor=CENTER)
startButton = Button(window, text="START", command=lambda:[start(), destroyall()])
startButton.place(relx=0.5, rely=0.5, anchor=CENTER)
image = Image.open("rvp.png")
image=image.resize((471,150))
pic = ImageTk.PhotoImage(image)
rvpImage = Label(image=pic)
rvpImage.image = pic
rvpImage .place(relx=0.52, rely=0.7, anchor=CENTER)
window.mainloop()
