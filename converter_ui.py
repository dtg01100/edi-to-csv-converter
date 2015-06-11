import converter
import os
from Tkinter import *
from tkFileDialog import askopenfilename
from tkFileDialog import askdirectory
import tkMessageBox
from PIL import Image, ImageTk

logo_io_error = False
image = None
logo_label = None
try:
    image = Image.open("logo.jpg")  # Replace with company logo (110px * 110px)
except IOError:
    logo_io_error = True  # if it fails, set this
filename = ''  # initialize filename Variable
root = Tk()  # initialize UI Window component
root.title("EDI to CSV converter 1.1")  # Set Window Title
var = StringVar()  # Status bar Variable
var.set('Select File')  # Set initial Status bar status
frame = Frame(root)  # Set placement frame
frame2 = Frame(root)  # Set placement fram2

upc_var_check = IntVar()  # define  "UPC calculation" checkbox state variable
a_rec_var_check = IntVar()  # define "A record checkbox state variable
c_rec_var_check = IntVar()  # define "C record" checkbox state variable
c_headers_check = IntVar()  # define "Column Headers" checkbox state variable
ampersand_check = IntVar()  # define "Filter Ampersand" checkbox state variable


#  initial file selection dialog, passes initial generated output file path to write error checker
def select_file():
    global filename
    global var
    global output
    filename = askopenfilename()  # open file select Dialog
    if filename != '':  # check for cancel/close of file open dialog, and do nothing if that's the case
        print (filename)  # print input file to stdout
        output = (filename + ".csv")  # create initial output file path
        check_write_error(output)  # send output file path to error checker


#  the following checks for write errors, passes any to the write error handler
def check_write_error(write_error_name):
    global filename
    global output
    io_error = False  # define io_error variable
    try:
        open(os.path.abspath(write_error_name), "w")  # try to write output file
    except IOError:
        io_error = True  # if it fails, set this
    if repr(os.path.dirname(output)) == "u'/'" or io_error is True or output == '' or output == "''" or \
            os.access(output, os.W_OK) is not True or output is None:  # check for invalid output path
        file_io_error_handler()  # call io error handler in event of invalid output
        if output is None or output is '' or output is "''":  # if user closes or cancels folder selection
            var.set("Origin Write Error. Directory Change Cancelled. Please Select Another File.")
            # set status bar text to this
        else:  # update interface if new output is acceptable
            # print repr(output) #  print raw value of output directory value
            print ("Now exporting to " + output)  # write directory to stdout
            var.set("Write Error In Input Directory, Exporting To " + output)  # display new file path in statusbar
            go_button.configure(state=ACTIVE)
    else:  # if all is well, update interface
        var.set(filename + " Ready To Convert")  # set file as status contents
        print filename + " ready to convert"  # status to stdout
        go_button.configure(state=ACTIVE)


#  the following prompts a new directory, then calls the function to check for write errors
def new_folder_selection():
    global output
    global filename
    output = askdirectory() + "/" + os.path.basename(filename) + ".csv"  # select new output directory
    check_write_error(output)  # check to see if new output directory is valid


#  the following prompts for directory change in the event of write error
def file_io_error_handler():
    global filename
    global output
    conflict_result = tkMessageBox.askyesno(title="Error", message="Write Error In Output Directory.\n \
    Would you like to change output directory?")  # show error if unable to write to directory
    if conflict_result is True:
        # prompt for new write directory
        new_folder_selection()
    else:
        # if user says no, reset status and notify user
        var.set("Origin Write Error. Directory Change Cancelled. Please Select Another File.")
        filename = ''  # set filename to null
        output = ''  # set output to null


def go_convert():
    global filename
    global upc_var_check
    global a_rec_var_check
    global c_rec_var_check
    global ampersand_check
    global output
    if filename != '':  # if there is a file then
        converter.edi_convert(filename, output, upc_var_check.get(), a_rec_var_check.get(),
                              c_rec_var_check.get(), c_headers_check.get(), ampersand_check.get())  # do conversion
        print output + " converted"  # print CLI debug string
        var.set(output + " Converted. Select next file.")  # Set status window String
        go_button.configure(state=DISABLED)
    else:  # if user gets ahead of themselves, and clicks this with no file selected.
        tkMessageBox.showerror(title="Error", message="No File Selected")  # show error
    filename = ''  # set file back to Null


upc_calc_checkbutton = Checkbutton(frame,
                                   text="Calculate UPC Check Digit", variable=upc_var_check, onvalue='1',
                                   offvalue='0')  # check and set variable of checkbox state
keep_a_records = Checkbutton(frame,
                             text="Keep \"A\" Records", variable=a_rec_var_check, onvalue='1',
                             offvalue='0')  # check and set variable of checkbox state
keep_c_records = Checkbutton(frame,
                             text="Keep \"C\" Records", variable=c_rec_var_check, onvalue='1',
                             offvalue='0')  # check and set variable of checkbox state
column_headers = Checkbutton(frame,
                             text="Column Headers", variable=c_headers_check, onvalue='1',
                             offvalue='0')  # check and set variable of checkbox state
filter_ampersand = Checkbutton(frame,
                               text="Replace Ampersand", variable=ampersand_check, onvalue='1',
                               offvalue='0')


# the following defines the UI
if logo_io_error is False:
    photo = ImageTk.PhotoImage(image)
    logo_label = Label(frame2, image=photo, relief="sunken",  padx=10, pady=10)
# logo_label.image = photo
# logo_label.config(relief = "sunken")

open_file_button = Button(frame, text="Select File", command=select_file)  # when button pressed execute select_file

# open_file_button.bind('<Button-1>', select_file)
go_button = Button(frame, text="Convert", command=go_convert, state=DISABLED)  # when button pressed execute go_convert
# go_button.bind('<Button-1>', go_convert)

file_feedback = Label(root, textvariable=var, relief="sunken")
how_to = Label(frame2, text="1) Select File \n2) Choose options \n3) Click convert", justify=LEFT)

# packed into "frame" order defines placement
open_file_button.pack(side=LEFT)  # file selector
upc_calc_checkbutton.pack(side=LEFT)
keep_a_records.pack(side=LEFT)
keep_c_records.pack(side=LEFT)
column_headers.pack(side=LEFT)
filter_ampersand.pack(side=LEFT)
go_button.pack(side=RIGHT)
center_pad = Label(frame2, text="To use:", padx=100, justify=RIGHT)

# packed into "frame2" order defines placement
if logo_io_error is False:
    logo_label.pack(side=LEFT)
center_pad.pack(side=LEFT)
how_to.pack(side=LEFT)

# main pack for overall look
frame.pack(fill="x", side=TOP)
file_feedback.pack(fill="x", side=BOTTOM)
frame2.pack(fill="x", side=LEFT)

# set window minimum size to prevent user making it ugly
root.update()  # update window geometry
root.minsize(root.winfo_width(),root.winfo_height())  # don't allow window to be resized smaller than current dimensions

# execute program
root.mainloop()
