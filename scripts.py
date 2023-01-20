import random


def generateName(numberOfItemsNeed):
    # opens 2 files. One containing first names and the other containing last names
    firstNameFile = open('dataFiles\FirstNamesData.txt', 'r')
    lastNameFile = open('dataFiles\LastNamesData.txt', 'r')
    # builds values for the while statement and the return string
    returnValue = ""
    counter = 0

# builds the return string using a while loop and removing the newline character
# after each line from both files when being read
    while counter < int(numberOfItemsNeed):
        returnValue += str(firstNameFile.readline().strip("\n")
                           ) + " " + str(lastNameFile.readline().strip("\n")) + "\n"
        counter = counter + 1
# returns a list of "human" names in a single string divided by a newline character
    return (returnValue)


def generateEmail(numberOfItemsNeed):
    # opens a file containing a records of first names
    firstNameFile = open('dataFiles\dictonary.txt', 'r')
    counter = 0
    # A list of commonly used email address suffixs
    suffix = ['@gmail.com', '@gmail.ca', '@hotmail.com',
              '@hotmail.ca', '@mail.com ', '@mail.ca', '@gov.ca']
    returnValue = ""

    while counter < int(numberOfItemsNeed):
        returnValue += firstNameFile.readline().strip("\n") + \
            str((random.randrange(0, 100))) + \
            suffix[random.randrange(0, len(suffix))]+'\n'
        counter = counter + 1
    return (returnValue)


def generateCost(numberOfItemsNeed):
    # generates a random item price in the inclusive range of 0.00$ to 1000.99$
    counter = 0
    cost = ""
    while counter < int(numberOfItemsNeed):
        cost += '$' + str(random.randrange(0, 1000)) + \
            "." + str(random.randrange(0, 99)) + '\n'
        counter = counter+1
    return cost


def generateProduct(numberOfItemsNeed):
    counter = 0
    returnValue = ""
    productList = open('dataFiles\itemData.txt', 'r')
    while counter < int(numberOfItemsNeed):
        returnValue += str(productList.readline()
                           ).strip("\n") + str(generateCost(1))
        counter = counter + 1
    return (returnValue)


def generatePhoneNumber(numberOfItemsNeed):
    counter = 0
    returnValue = ""
    while counter < int(numberOfItemsNeed):

        firstNumber = str(random.randrange(100, 999))
        secondNumber = str(random.randrange(1000, 9999))
        thirdNumber = str(random.randrange(100, 999))

        returnValue += firstNumber + "-" + secondNumber + "-" + thirdNumber + '\n'
        counter = counter + 1
    return (returnValue)


def shuffleFile(filePath):
    lines = open(filePath).readlines()
    random.shuffle(lines)
    open(filePath, 'w').writelines(lines)
        
# shuffleFile('dataFiles\dictonary.txt')
