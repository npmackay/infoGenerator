# IMPORT tkinter for GUI creation and import scripts for functions
from tkinter import *
from tkinter.ttk import *
import scripts
import customtkinter

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("dark")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("customTkinterTheme.json")


def popupmsg(msg):
    popup = customtkinter.CTk()
    popup.title("!")
    label = customtkinter.CTkLabel(popup, text=msg,)
    label.pack(side="top", fill="x", pady=10)
    B1 = customtkinter.CTkButton(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()


# create main window
# window specs are 700 x 350 and window is not able to be resizeable
windowDim = str(750)+'x'+str(350)
window = customtkinter.CTk()
window.configure(background='#3b597d')
window.title("INFO GENERATOR")
window.geometry(windowDim)
window.resizable(False, False)
# CREATING USER CONTROLS
# each button will print a list of items (number of items will be come from the entry userValue)
userEntry = customtkinter.CTkEntry(window)
# userValue = int(userValue)

userValue = ""

userEntry.place(x=325, y=200)
userEntry.insert(0, userValue)

userValueLabel = customtkinter.CTkLabel(
    window, text="ENTER AMOUNT OF RECORDS YOU WOULD LIKE").place(x=275, y=170)
label = customtkinter.CTkLabel(window, text="INFOMATION GENERATOR by Noah Mackay "
                               ).pack()


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


emailButton = customtkinter.CTkButton(window, text="EMAILS",
                                      command=lambda: outputEmails(userValue)).place(x=5, y=40)


productButton = customtkinter.CTkButton(window, text="PRODUCTS",
                                        command=lambda: outputProduct(userValue)).place(x=150, y=40)
phoneNumberButton = customtkinter.CTkButton(
    window, text="PHONE NUMBERS").place(x=300, y=40)
costButton = customtkinter.CTkButton(window, text="PRICES",
                                     command=lambda: outputCost(userValue)).place(x=450, y=40)
nameButton = customtkinter.CTkButton(
    window, text="FIRST + LAST NAMES", command=lambda: outputNames(userValue)).place(x=600, y=40)


window.mainloop()