# ask user what type of list they want to create
# options are (People , Items , Cost , Business)
import scripts
outputFile = open('output.txt', 'w').close
outputFile = open('output.txt', 'w')
print("       ***** WELCOME TO NOAHS GENERATOR *****")
print("PLEASE INPUT WHAT TYPE OF LIST YOU WOULD LIKE TO CREATE")
print(" 'P' for PEOPLE 'I' for ITEMS 'C' for COST 'B' for BUSINESS 'E' for EMAILS")
userTypeChoice = input().capitalize()
print("how many items would you like")
numberOfListItems = input()
outputData = ""

# open user chosen file
if userTypeChoice == 'P':
    outputData = scripts.generateName(numberOfListItems)
    print(outputData)
elif userTypeChoice == 'I':
    outputData = scripts.generateProduct(numberOfListItems)
    print(outputData)
elif userTypeChoice == 'C':
    outputData = scripts.generateCost(numberOfListItems)
    print(outputData)
elif userTypeChoice == 'B':
    file = open('dataFiles\companyNames.txt', 'r')
elif userTypeChoice == 'E':
    outputData = scripts.generateEmail(numberOfListItems)
    print(outputData)
else:
    print("Incorrect input")
print(outputData)
# setting up the output file

counter = 0
print("would you like to print to output.txt")
printBool = input().capitalize()
if printBool == 'Y':
    outputFile.write(outputData)
    print("printing worked")
else:
    print("printing did not work")
