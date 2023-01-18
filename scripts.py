import random


def generateName(numberOfItemsNeed):
    lastNameFile = open('dataFiles\LastNamesData.txt', 'r')
    firstNameFile = open('dataFiles\FirstNamesData.txt', 'r')
    returnValue = ""
    numberOfNamesNeed = int(numberOfItemsNeed)
    counter = 0
    while counter < numberOfItemsNeed:
        returnValue += str(firstNameFile.readline()
                           ) + str(lastNameFile.readline()) + '\n'
        counter = counter + 1
    return(returnValue)


def generateEmail(numberOfItemsNeed):
    firstNameFile = open('dataFiles\FirstNamesData.txt', 'r')
    counter = int(0)
    suffix = ['@gmail.com', '@gmail.ca', '@hotmail.com',
              '@hotmail.ca', '@mail.com ', '@mail.ca', '@gov.ca']
    returnValue = ""

    while counter < numberOfItemsNeed:
        returnValue += firstNameFile.readline() + \
            str((random.randrange(0, 100))) + \
            suffix[random.randrange(0, len(suffix))]+'\n'
        counter = counter + 1
    return(returnValue)


def generateCost(numberOfItemsNeed):
    counter = 0
    cost = ""
    while counter < numberOfItemsNeed:
        cost += str(random.randrange(0, 1000)) + \
            "." + str(random.randrange(0, 99)) + '$' + '\n'
        counter = counter+1
    return cost


def generateProduct(numberOfItemsNeed):
    counter = 0
    returnValue = ""
    productList = open('dataFiles\itemData.txt', 'r')
    while counter < numberOfItemsNeed:
        returnValue += str(productList.readline()) + str(generateCost(1))
        counter = counter + 1
    return(returnValue)


print(generateEmail(10))
