from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image

global imageFile
root = Tk()
root.geometry("300x150")

def main():
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Upload an image").grid(column=0, row=0)
    ttk.Button(frm, text="Upload photo for analysis", command=openfile).grid(column=1, row=0)

    root.mainloop()



def openfile():
    imageFile = filedialog.askopenfilename(title="Select a Picture", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    filename = "image.png"
    with Image.open(imageFile) as image:
        width, height = image.size
    close_window()

def close_window():
    root.quit()

if __name__ == "__main__":
    main()