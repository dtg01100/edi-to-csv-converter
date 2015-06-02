import converter
import os
from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox
from PIL import Image, ImageTk

image = Image.open("logo.jpg") # Replace with company logo (110px * 110px)
filename = '' #initialize filename Variable
root = Tk() # initialize UI Window component
root.title("EDI to CSV converter") # Set Window Title
root.geometry("650x170") # Set initial window size
root.minsize(width=650, height=170) # Set window minimal Size
var = StringVar() # Status bar Variable
var.set('Select File') # Set initial Status bar status
frame = Frame(root) # IDK
frame.pack() #IDK


def select_file(event):
    global filename
    global var
    filename = askopenfilename() #open file select Dialog
    print (filename)
    if filename != '':
        var.set(filename) #set file as status contents
        print (filename) + " ready to convert"


def go_convert(event):
    global filename
    global upcvarcheck
    global arecvarcheck
    global crecvarcheck
    output = os.path.abspath(filename) + ".csv" 
    if filename != '':
        converter.edi_convert(filename, output, upcvarcheck.get(), arecvarcheck.get(), crecvarcheck.get()) # do conversion
        print (filename) + " converted"
        var.set(filename + " Converted. Select next file.")
    else:
        tkMessageBox.showerror(title="Error",message="No File Selected")
    filename = ''


upcvarcheck = IntVar()
upc_calc_checkbutton = Checkbutton(frame, text="Calculate UPC Check Digit", variable=upcvarcheck, onvalue = '1', offvalue = '0') 
arecvarcheck = IntVar()
keep_arecords = Checkbutton(frame, text="Keep \"A\" Records", variable=arecvarcheck, onvalue = '1', offvalue = '0')
crecvarcheck = IntVar()
keep_crecords = Checkbutton(frame, text="Keep \"C\" Records", variable=crecvarcheck, onvalue = '1', offvalue = '0')


# the following defines the UI
photo = ImageTk.PhotoImage(image)
logo_label = Label(image=photo)
logo_label.image = photo
logo_label.config(relief = "sunken")
logo_label.pack( side = LEFT, padx=10, pady=10)
keep_crecords.pack(side = RIGHT)
keep_arecords.pack(side = RIGHT)
upc_calc_checkbutton.pack( side = RIGHT)
open_file_button = Button(frame, text="Select File")
open_file_button.pack( side = LEFT)
open_file_button.bind('<Button-1>', select_file)
go_button = Button(frame, text="Convert")
go_button.pack( side = LEFT)
go_button.bind('<Button-1>', go_convert)
filefeedback = Label(root, textvariable = var)
filefeedback.config(relief = "sunken")
filefeedback.pack(fill = "x", side = BOTTOM)

# execute program
root.mainloop()
