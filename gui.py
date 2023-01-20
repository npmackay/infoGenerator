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

# userEntry.pack

# entryValue = int(userEntry.get())
userValueLabel = Label(
    window, text="ENTER AMOUNT OF RECORDS YOU WOULD LIKE").place(x=400, y=170)
label = Label(window, text="INFOMATION GENERATOR by Noah Mackay ",
              background='#111111').pack()


def outputEmails(num):
    # outputFile = scripts.generateEmail(100)
    outputFile = scripts.generateEmail(num)
    file = open('output.txt', 'w')
    file.write(str(outputFile))


def outputNames(num):
    outputFile = scripts.generateName(num)
    file = open('output.txt', 'w')
    file.write(str(outputFile))


def outputCost(num):
    outputFile = scripts.generateCost(num)
    file = open('output.txt', 'w')
    file.write(str(outputFile))


def outputProduct(num):
    outputFile = scripts.generateProduct(num)
    file = open('output.txt', 'w')
    file.write(str(outputFile))


def outputPhoneNumber(num):
    outputFile = scripts.generatePhoneNumber(num)
    file = open('output.txt', 'w')
    file.write(str(outputFile))


emailButton = Button(window, text="PRESS ME FOR EMAILS",
                     command=outputEmails(10)).place(x=40, y=50)
nameButton = Button(
    window, text="PRESS ME FOR FIRST AND LAST NAMES", command=outputNames(30)).place(x=40, y=100)
costButton = Button(window, text="PRESS ME FOR PRICES",
                    command=outputCost(20)).place(x=40, y=150)
productButton = Button(window, text="PRESS ME FOR PRODUCTS",
                       command=outputProduct(50)).place(x=40, y=200)
phoneNumberButton = Button(
    window, text="PRESS ME FOR PHONE NUMBERS").place(x=40, y=250)

# printButton = Button(window, text='PRINT LIST' ()).place(x=483.5, y=300)


# validation of of userValue entry to insure that the user has entered a int

window.mainloop()
