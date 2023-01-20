# IMPORT tkinter for GUI creation and import scripts for functions
from tkinter import *
from tkinter.ttk import *
import scripts


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


userEntry.place(x=450, y=200)
userEntry.insert(0, 2)
updateButton = Button(window, text="UPDATE",
                      ).place(x=475, y=225)

outputValue = int(userEntry.get())

userValueLabel = Label(
    window, text="ENTER AMOUNT OF RECORDS YOU WOULD LIKE").place(x=400, y=170)
label = Label(window, text="INFOMATION GENERATOR by Noah Mackay ",
              background='#9999ff').pack()


def outputEmails():
    # function will be called when email button is clicked
    # this function will clear the output file and then read open it
    # will call the generateEmail function from scripts.py file
    # outputs the amount of records based on the user input in the entry text box

    outputFile = scripts.generateEmail(outputValue)
    file = open('output.txt', 'w').close()
    file = open('output.txt', 'w')
    file.write(str(outputFile))


def outputNames():

    outputFile = scripts.generateName(outputValue)
    file = open('output.txt', 'w').close()
    file = open('output.txt', 'w')
    file.write(str(outputFile))


def outputCost():

    outputFile = scripts.generateCost(outputValue)
    file = open('output.txt', 'w').close()
    file = open('output.txt', 'w')
    file.write(str(outputFile))


def outputProduct():

    outputFile = scripts.generateProduct(outputValue)
    file = open('output.txt', 'w').close()
    file = open('output.txt', 'w')
    file.write(str(outputFile))


def outputPhoneNumber():

    outputFile = scripts.generatePhoneNumber(outputValue)
    file = open('output.txt', 'w').close()
    file = open('output.txt', 'w')
    file.write(str(outputFile))

# creates 5 buttons each have their respective output function attached using command=


emailButton = Button(window, text="EMAILS",
                     command=outputEmails()).place(x=40, y=50)
nameButton = Button(
    window, text="FIRST AND LAST NAMES", command=outputNames()).place(x=40, y=100)
costButton = Button(window, text="PRICES",
                    command=outputCost()).place(x=40, y=150)
productButton = Button(window, text="PRODUCTS",
                       command=outputProduct()).place(x=40, y=200)
phoneNumberButton = Button(
    window, text="PHONE NUMBERS").place(x=40, y=250)


window.mainloop()
