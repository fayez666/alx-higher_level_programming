#!/usr/bin/python3
def no_c(my_string):
    listOfChars = list(my_string)
    for char in listOfChars:
        if char == 'c' or char == 'C':
            listOfChars.remove(char)
    return("".join(listOfChars))
