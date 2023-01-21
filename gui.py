# IMPORT tkinter for GUI creation and import scripts for functions
from tkinter import *
from tkinter.ttk import *
import scripts
import customtkinter
# creates main window with 750 x 600 window size
windowDim = str(750)+'x'+str(600)
window = customtkinter.CTk()
window.title("INFO GENERATOR")
window.geometry(windowDim)
window.resizable(True, True)

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("dark")
# set up custom customTkitnter theme
customtkinter.set_default_color_theme("customTkinterTheme.json")

outputToScreen = customtkinter.CTkTextbox(window, width=400, height=200)
outputToScreen.place(x=200, y=300)

# function to create a pop up box
# used to alert user that printing was successful


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

# CREATING USER CONTROLS
# each button will print a list of items (number of items will be come from the entry userValue)
userEntry = customtkinter.CTkEntry(window)

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
    outputToScreen.delete("1.0", END)
    outputToScreen.insert("1.0", outputFile)
    popupmsg("PRINTING COMPLETED")


def outputNames(userValue):
    # function receives the amount of records the user wants to print
    # function will be called when name button is clicked
    # this function will clear the output file and then read open it
    # will call the generateName function from scripts.py file
    # outputs the amount of records based on the user input in the entry text box
    userValue = int(userEntry.get())
    outputFile = scripts.generateName(userValue)
    file = open('output.txt', 'w').close()
    file = open('output.txt', 'w')
    file.write(str(outputFile))
    outputToScreen.delete("1.0", END)
    outputToScreen.insert("1.0", outputFile)
    popupmsg("PRINTING COMPLETED")


def outputCost(userValue):
    # function receives the amount of records the user wants to print
    # function will be called when price button is clicked
    # this function will clear the output file and then read open it
    # will call the generateCost function from scripts.py file
    # outputs the amount of records based on the user input in the entry text box
    userValue = int(userEntry.get())
    outputFile = scripts.generateCost(userValue)
    file = open('output.txt', 'w').close()
    file = open('output.txt', 'w')
    file.write(str(outputFile))
    outputToScreen.delete("1.0", END)
    outputToScreen.insert("1.0", outputFile)
    popupmsg("PRINTING COMPLETED")


def outputProduct(userValue):
    # function receives the amount of records the user wants to print
    # function will be called when name button is clicked
    # this function will clear the output file and then read open it
    # will call the generateProduct function from scripts.py file
    # outputs the amount of records based on the user input in the entry text box
    userValue = int(userEntry.get())
    outputFile = scripts.generateProduct(userValue)
    file = open('output.txt', 'w').close()
    file = open('output.txt', 'w')
    file.write(str(outputFile))
    outputToScreen.delete("1.0", END)
    outputToScreen.insert("1.0", outputFile)
    popupmsg("PRINTING COMPLETED")


def outputPhoneNumber(userValue):
    # function receives the amount of records the user wants to print
    # function will be called when phoneNumber button is clicked
    # this function will clear the output file and then read open it
    # will call the generatePhoneNumber function from scripts.py file
    # outputs the amount of records based on the user input in the entry text box
    userValue = int(userEntry.get())
    outputFile = scripts.generatePhoneNumber(userValue)
    file = open('output.txt', 'w').close()
    file = open('output.txt', 'w')
    file.write(str(outputFile))
    outputToScreen.delete("1.0", END)
    outputToScreen.insert("1.0", outputFile)
    popupmsg("PRINTING COMPLETED")

# creates 5 buttons each have their respective output function attached using command=


emailButton = customtkinter.CTkButton(window, text="EMAILS",
                                      command=lambda: outputEmails(userValue)).place(x=5, y=40)


productButton = customtkinter.CTkButton(window, text="PRODUCTS",
                                        command=lambda: outputProduct(userValue)).place(x=150, y=40)
phoneNumberButton = customtkinter.CTkButton(
    window, text="PHONE NUMBERS", command=lambda: outputPhoneNumber(userValue)).place(x=300, y=40)
costButton = customtkinter.CTkButton(window, text="PRICES",
                                     command=lambda: outputCost(userValue)).place(x=450, y=40)
nameButton = customtkinter.CTkButton(
    window, text="FIRST + LAST NAMES", command=lambda: outputNames(userValue)).place(x=600, y=40)

# renderr window
window.mainloop()
