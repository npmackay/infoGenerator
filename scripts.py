# ask user what type of list they want to create
# options are (People , Items , Cost , Business)

outputFile = open('output.txt').close
outputFile = open('output.txt', 'w')
print("       ***** WELCOME TO NOAHS GENERATOR *****")
print("PLEASE INPUT WHAT TYPE OF LIST YOU WOULD LIKE TO CREATE")
print(" 'P' for PEOPLE 'I' for ITEMS 'C' for COST 'B' for BUSINESS 'E' for EMAILS")
userTypeChoice = input()
userTypeChoice = userTypeChoice.capitalize()
print("how many items would you like")
numberOfListItems = input()




# open user chosen file
if userTypeChoice == 'P':
    file = open('dataFiles\personData.txt', 'r')
elif userTypeChoice == 'I':
    file = open('dataFiles\itemData.txt', 'r')
elif userTypeChoice == 'C':
    file = open('dataFiles\costData.txt', 'r')
elif userTypeChoice == 'B':
    file = open('companyNames.txt', 'r')
elif userTypeChoice == 'E':
    file = open('dataFiles\emailData.txt', 'r')
else:
    print("Incorrect input")

# setting up the output file
outputData = ""
counter = 0

while counter < int(numberOfListItems):
    outputData += file.readline()
    counter = counter + 1
print(outputData)
outputFile.write(outputData)
