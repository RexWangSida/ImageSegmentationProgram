from tkinter import *
import tkinter.font as tkFont
from tkinter import filedialog
from PIL import Image, ImageTk
from algorithms import segmentation
import os
SAVEPATH = ""
READPATH = ""
image1, image2 =None, None
def start(newWin = False):

    def setSaving():
        global SAVEPATH
        SAVEPATH =  filedialog.askdirectory()
        dirLabel = Label( text="  Location to save image:   " + SAVEPATH)
        dirLabel.grid(row = 5, column = 2)

    def loadImg():
        global READPATH, image1
        READPATH =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        filenameLabel = Label( text="  Image to be segmented:   " + READPATH)
        filenameLabel.grid(row = 1, column = 2)
        image = Image.open(READPATH)
        displayImage = image
        while displayImage.size[0] > 400 or displayImage.size[1] > 400:
            displayImage = displayImage.resize((int(displayImage.size[0]//2),int(displayImage.size[1]//2)))
        displayPic = ImageTk.PhotoImage(displayImage)
        image1 = Label(image=displayPic)
        image1.image = displayPic
        image1.place(relx=0.3, rely=0.6, anchor=CENTER)

    def process():
        global image2
        segmentation(READPATH, int(kEntry.get()), os.path.join(SAVEPATH,"SEG" + os.path.basename(READPATH)))
        image = Image.open(os.path.join(SAVEPATH,"SEG" + os.path.basename(READPATH)))
        displayImage = image
        while displayImage.size[0] > 400 or displayImage.size[1] > 400:
            displayImage = displayImage.resize((int(displayImage.size[0]//2),int(displayImage.size[1]//2)))
        displayPic = ImageTk.PhotoImage(displayImage)
        image2 = Label(image=displayPic)
        image2.image = displayPic
        image2.place(relx=0.7, rely=0.6, anchor=CENTER)

    spacer1 = Label( text="          ")
    spacer1.grid(row = 0, column = 0)
    imageButton = Button( text="Select Input Image", command=loadImg)
    imageButton.grid(row = 1, column = 1)
    kText = Label( text="Number of Clusters(k): ")
    spacer2 = Label(text="          ")
    spacer2.grid(row = 2, column = 0)
    kText.grid(row = 3, column = 1)
    kEntry = Entry()
    kEntry.grid(row = 3, column = 2)
    spacer3 = Label(text="          ")
    spacer3.grid(row = 4, column = 0)
    saveButton = Button( text="Select Output location", command=setSaving)
    saveButton.grid(row = 5, column = 1)
    spacer4 = Label( text="          ")
    spacer4.grid(row = 6, column = 0)
    submit = Button( text="Submit", command=process)
    submit.grid(row = 7, column = 2)
    clear = Button( text="Clear Images", command=lambda:[image1.destroy(), image2.destroy()])
    clear.grid(row = 7, column = 3)


def destroyall():
    global startLabel1, startLabel2, creator, startButton, rvpImage

    startLabel1.place_forget()
    startLabel2.place_forget()
    creator.place_forget()
    startButton.place_forget()
    rvpImage.place_forget()

window = Tk()
window.title("Image Segmentation Processor")
window.geometry("800x800")
startLabel1 = Label(text="Image Segmentation Processor",font=tkFont.Font(family='Impact', size=20))
startLabel2 = Label(text="based on K-Means Clustering Algorithm",font=tkFont.Font(family="Lucida Grande", size=10))
startLabel1.place(relx=0.5, rely=0.2, anchor=CENTER)
startLabel2.place(relx=0.5, rely=0.3, anchor=CENTER)
creator = Label(text="Creator: Sida Wang",font=tkFont.Font(family="Lucida Grande", size=10))
creator .place(relx=0.5, rely=0.4, anchor=CENTER)
startButton = Button(window, text="START", command=lambda:[start(), destroyall()])
startButton.place(relx=0.5, rely=0.5, anchor=CENTER)
image = Image.open("rvp.png")
image=image.resize((628,200))
pic = ImageTk.PhotoImage(image)
rvpImage = Label(image=pic)
rvpImage.image = pic
rvpImage.place(relx=0.52, rely=0.7, anchor=CENTER)
window.mainloop()
