# IMPORT tkinter for GUI creation and import scripts for functions
from tkinter import *
from tkinter.ttk import *
import scripts


def popupmsg(msg):
    popup = Tk()
    popup.wm_title("!")
    label = Label(popup, text=msg,)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()


# create main window
# window specs are 700 x 350 and window is not able to be resizeable
windowDim = str(700)+'x'+str(350)
window = Tk()
window.title("INFO GENERATOR")
window.geometry(windowDim)
window.resizable(False, False)
# CREATING USER CONTROLS
# each button will print a list of items (number of items will be come from the entry userValue)
userEntry = Entry(window)
# userValue = int(userValue)

userValue = ""

userEntry.place(x=450, y=200)
userEntry.insert(0, userValue)

userValueLabel = Label(
    window, text="ENTER AMOUNT OF RECORDS YOU WOULD LIKE").place(x=400, y=170)
label = Label(window, text="INFOMATION GENERATOR by Noah Mackay ",
              background='#9999ff').pack()


def outputEmails(userValue):
    # function receives the amount of records the user wants to print
    # function will be called when email button is clicked
    # this function will clear the output file and then read open it
    # will call the generateEmail function from scripts.py file
    # outputs the amount of records based on the user input in the entry text box
    userValue = int(userEntry.get())
    outputFile = scripts.generateEmail(userValue)
    file = open('output.txt', 'w').close()
    file = open('output.txt', 'w')
    file.write(str(outputFile))
    popupmsg("PRINTING WO")


def outputNames(userValue):
    # function receives the amount of records the user wants to print
    # function will be called when email button is clicked
    # this function will clear the output file and then read open it
    # will call the generateEmail function from scripts.py file
    # outputs the amount of records based on the user input in the entry text box
    userValue = int(userEntry.get())
    outputFile = scripts.generateName(userValue)
    file = open('output.txt', 'w').close()
    file = open('output.txt', 'w')
    file.write(str(outputFile))
    popupmsg("PRINTING COMPLETED")


def outputCost(userValue):
    userValue = int(userEntry.get())
    outputFile = scripts.generateCost(userValue)
    file = open('output.txt', 'w').close()
    file = open('output.txt', 'w')
    file.write(str(outputFile))
    popupmsg("PRINTING COMPLETED")


def outputProduct(userValue):
    userValue = int(userEntry.get())
    outputFile = scripts.generateProduct(userValue)
    file = open('output.txt', 'w').close()
    file = open('output.txt', 'w')
    file.write(str(outputFile))
    popupmsg("PRINTING COMPLETED")


def outputPhoneNumber(userValue):
    userValue = int(userEntry.get())
    outputFile = scripts.generatePhoneNumber(userValue)
    file = open('output.txt', 'w').close()
    file = open('output.txt', 'w')
    file.write(str(outputFile))
    popupmsg("PRINTING COMPLETED")
# creates 5 buttons each have their respective output function attached using command=


emailButton = Button(window, text="EMAILS",
                     command=lambda: outputEmails(userValue)).place(x=40, y=50)


productButton = Button(window, text="PRODUCTS",
                       command=lambda: outputProduct(userValue)).place(x=40, y=200)
phoneNumberButton = Button(
    window, text="PHONE NUMBERS").place(x=40, y=250)
costButton = Button(window, text="PRICES",
                    command=lambda: outputCost(userValue)).place(x=40, y=150)
nameButton = Button(
    window, text="FIRST AND LAST NAMES", command=lambda: outputNames(userValue)).place(x=40, y=100)


window.mainloop()
