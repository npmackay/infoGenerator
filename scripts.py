import random


def generateName(numberOfItemsNeed):
    lastNameFile = open('dataFiles\LastNamesData.txt', 'r')
    firstNameFile = open('dataFiles\FirstNamesData.txt', 'r')
    returnValue = ""
    counter = 0

    while counter < int(numberOfItemsNeed):
        returnValue += str(firstNameFile.readline(random.randrange(0, 1000)).strip("\n")
                           ) + " " + str(lastNameFile.readline(random.randrange(0, 1000))).strip("\n") + "\n"
        counter = counter + 1
    return (returnValue)


def generateEmail(numberOfItemsNeed):
    firstNameFile = open('dataFiles\dictonary.txt', 'r')
    counter = int(0)
    suffix = ['@gmail.com', '@gmail.ca', '@hotmail.com',
              '@hotmail.ca', '@mail.com ', '@mail.ca', '@gov.ca']
    returnValue = ""

    while counter < int(numberOfItemsNeed):
        returnValue += firstNameFile.readline(random.randrange(0,1000)).strip("\n") + \
            str((random.randrange(0, 100))) + \
            suffix[random.randrange(0, len(suffix))]+'\n'
        counter = counter + 1
    return (returnValue)


def generateCost(numberOfItemsNeed):
    counter = 0
    cost = ""
    while counter < int(numberOfItemsNeed):
        cost += str(random.randrange(0, 1000)) + \
            "." + str(random.randrange(0, 99)) + '$' + '\n'
        counter = counter+1
    return cost


def generateProduct(numberOfItemsNeed):
    counter = 0
    returnValue = ""
    productList = open('dataFiles\itemData.txt', 'r')
    while counter < int(numberOfItemsNeed):
        returnValue += str(productList.readline()).strip("\n") + str(generateCost(1))
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


print(generateEmail(1500))
