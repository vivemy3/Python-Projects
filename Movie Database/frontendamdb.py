from tkinter import *
from PIL import ImageTk, Image
from backendamdb import *

#Window setup
window = Tk()
window.geometry('500x550')
window.resizable(0,0)
window.iconbitmap(default = "favicon.ico")
window.title('Aarons\'s Movie Database')
window.config(bg = 'purple')
       


# Clears the entry fields
def clearinputs():
    inputvalue.delete(0,"end")
    inputkey.delete(0,"end")
    dictlist.delete(0,"end")

# Adds or updates data based on a barcode or set of charactors
def addinfo():  
    if len(inputkey.get()) != 0 and len(inputvalue.get()) != 0:
        writejson(inputkey.get(),inputvalue.get().upper())
        clearinputs()
        inputvalue.focus_set()
        dictlist.insert("end", *sorted(populateListbox()))
        canvas.itemconfigure(count,text = counter())
    
# Deletes data from the list, based on the barcode scanned
def deleteinfo():
    if len(inputkey.get()) != 0:
        deletejsoninfo(inputkey.get())
        clearinputs()
        inputvalue.focus_set()
        dictlist.insert("end", *sorted(populateListbox()))
        canvas.itemconfigure(count,text = counter())

# Event manager for buttons
def deletedata(event):
    deleteinfo()
    
def adddata(event):
    addinfo()
    
# Reads the values from the listbox when dbl clicked or enter was pressed, and populates the input fields
def updateinfo(event):
    inputvalue.delete(0,"end")
    inputkey.delete(0,"end")
    inputkey.insert(0, list(readjson().keys())[list(readjson().values()).index(dictlist.get(ACTIVE))])
    inputvalue.insert(0,dictlist.get(ACTIVE))

#Title label
titlelabel = Label(window, text = "Aaron's Movie Database",bg="purple",font=("Arial Black",26,"bold"))
titlelabel.pack(pady = 10)

# Frame to format the image and entryfields
box1 = Frame(bg="purple")
box1.pack(padx = 20)

# Frame to format the entryfields and labels
box2 = Frame(box1, bg = "purple")
box2.grid(row = 0, column = 0, padx = 20)

# Frame to format the image/canvas
box3 = Frame(box1, bg = "purple")
box3.grid(row = 0, column = 1)

# Frame to store the buttons
box4 = Frame(box1, bg = "purple")
box4.grid(pady=5)

# Creates a canvas to load an image into
canvas = Canvas(box3,width = 200, height = 175, bg = "purple", highlightthickness=0)
canvas.grid(padx = 20)

# Loads the image into the canvas
img = ImageTk.PhotoImage(Image.open("movie.png"))
canvas.create_image(0,0, anchor=NW, image=img)
canvas.create_text(100,75, text="Movie Count", font = ("Arial MT",14,"bold"))
count = canvas.create_text(100,110, font=("Arial MT",30,"bold"))
canvas.itemconfigure(count,text = counter())

# Movie Title Entryfield
label1 = Label(box2,text ="Movie Title",font=("Hevlitica", 16, "bold"),bg = "purple")
label1.pack()
inputvalue = Entry(box2,font=("Helvitica",12))
inputvalue.pack()

# Barcode Entryfield
label2 = Label(box2, text ="Barcode",font=("Hevlitica", 16, "bold"),bg = "purple")
label2.pack()
inputkey = Entry(box2, font=("Helvitica",12))
inputkey.pack()

box4 = Frame(box2,bg="purple")
box4.pack(pady=15)

# Button to delete the content
button1 = Button(box4, text = "Delete Content", command = deleteinfo)
button1.bind("<Return>",deletedata)
button1.grid(column=0,row=0)

# Button to add the content
button2 = Button(box4, text = "Add Content", command = addinfo)
button2.bind("<Return>", adddata)
button2.grid(column=1,row=0)

# List box to display all the movies
dictlist = Listbox(window, width = 40, height = 20, font = ("Arial MT",16))
dictlist.bind("<Double-Button>", updateinfo)
dictlist.bind("<Return>", updateinfo)
dictlist.pack(pady = 10)

# Sets the cursor to the Movie Title entryfield
inputvalue.focus_set()


#starts the program with the filled list box
dictlist.insert("end", *sorted(populateListbox()))

#Program mainloop
window.mainloop()