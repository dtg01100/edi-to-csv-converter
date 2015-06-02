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
frame = Frame(root) # Set placement frame
frame2 = Frame(root) # Set placement fram2

upcvarcheck = IntVar() # define  "UPC calculation" checkbox state variable
arecvarcheck = IntVar() # define "A record checkbox state variable
crecvarcheck = IntVar() # define "C record" checkbox state variable
cheaderscheck = IntVar() # define "Column Headers" checkbox state variable


def select_file():
    global filename
    global var
    filename = askopenfilename() #open file select Dialog
    print (filename)
    if os.access(filename,os.W_OK) != True and filename != '':
        tkMessageBox.showerror(title="Error",message="No Write Permissions For Directory") #show error if unable to write to directory
        filename = '' #set filename to null
    if filename != '':
        var.set(filename) #set file as status contents
        print (filename) + " ready to convert"



def go_convert():
    global filename
    global upcvarcheck
    global arecvarcheck
    global crecvarcheck
    output = os.path.abspath(filename) + ".csv"
    if filename != '': # if there is a file then
        converter.edi_convert(filename, output, upcvarcheck.get(), arecvarcheck.get(), crecvarcheck.get(), cheaderscheck.get()) # do conversion
        print (filename) + " converted" # print CLI debig string
        var.set(filename + " Converted. Select next file.") # Set status window String
    else:
        tkMessageBox.showerror(title="Error",message="No File Selected")  # show error
    filename = '' # set file back to Null



upc_calc_checkbutton = Checkbutton(frame, text="Calculate UPC Check Digit", variable=upcvarcheck, onvalue = '1', offvalue = '0') #check and set variable of checkbox state
keep_arecords = Checkbutton(frame, text="Keep \"A\" Records", variable=arecvarcheck, onvalue = '1', offvalue = '0') #check and set variable of checkbox state
keep_crecords = Checkbutton(frame, text="Keep \"C\" Records", variable=crecvarcheck, onvalue = '1', offvalue = '0') #check and set variable of checkbox state
column_headers = Checkbutton(frame, text="Column Headers", variable=cheaderscheck, onvalue = '1', offvalue = '0') #check and set variable of checkbox state


# the following defines the UI
photo = ImageTk.PhotoImage(image)
logo_label = Label(frame2, image=photo, relief = "sunken",  padx=10, pady=10 )
#logo_label.image = photo
#logo_label.config(relief = "sunken")

open_file_button = Button(frame, text="Select File", command=select_file) # when button pressed execute select_file

#open_file_button.bind('<Button-1>', select_file)
go_button = Button(frame, text="Convert", command=go_convert) # when button pressed execute go_convert
#go_button.bind('<Button-1>', go_convert)

filefeedback = Label(root, textvariable = var, relief = "sunken")
#filefeedback.config()
howto = Label(frame2, text="1) Select File \n2) Choose options \n3) Click convert", justify = LEFT)

# packed into "frame" order defines placement
open_file_button.pack( side = LEFT) # file selector
upc_calc_checkbutton.pack( side = LEFT)
keep_arecords.pack(side = LEFT)
keep_crecords.pack(side = LEFT)
column_headers.pack(side = LEFT)
go_button.pack( side = LEFT)
centerpad = Label(frame2, text="To use:", padx=100, justify = RIGHT)

# packed into "frame2" order defines placement
logo_label.pack(side = LEFT )
centerpad.pack(side=LEFT)
howto.pack(side=LEFT)

#main pack for overall look
frame.pack(fill= "x", side = TOP)
filefeedback.pack(fill = "x", side = BOTTOM)
frame2.pack(fill = "x", side = LEFT)
# execute program

root.mainloop()
