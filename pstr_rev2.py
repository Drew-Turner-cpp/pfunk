# Constants
NULL = ''

# Internal note: i cant believe this works. you can store functions in a dict or array and call them later
OPERDICT = {'integer': int,'float': float,
            'string': str, 'boolean': bool}


def findReturn(test):
    """
    Takes one argument; returns the data type of the arg fed

    :return: Data type as a string
    """
    if test == True or test == False:
        return 'boolean'

    integer = isinstance(test, int)
    string = isinstance(test, str)
    floaT = isinstance(test, float)

    if integer:
        return 'integer'
    elif string:
        return 'string'
    elif floaT:
        return 'float'


def split(thing):
    """
    Takes one argument; splits a string into a list of characters

    :return: List of characters and the original type (tuple)
    """
    tp = findReturn(thing)
    return [char for char in str(thing)], tp


def replace(oldS, newS, visual=False):
    """
    Takes two arguments; replaces the items fed

    :return: New item (keeping data type of new)
    """

    # Split
    oldL, ot = split(oldS)
    newL, nt = split(newS)

    index = 0

    modelList = []

    # Strings fed are the same
    if oldS == newS:
        if visual:
            print(split(oldS))
        return oldS

    # Length of old str is greater
    if len(oldL) > len(newL):

        # Appends modelList by the difference of the two lengths of the lists
        for x in range(len(oldL) - len(newL)):
            modelList.append(NULL)

            # Appends corresponding list
            for x in modelList:
                newL.append(NULL)


    # Length of new str is greater
    else:

        # Appends modelList by the difference of the two lengths of the lists
        for x in range(len(newL) - len(oldL)):
            modelList.append(NULL)

        # Appends corresponding list
        for x in modelList:
            oldL.append(NULL)

    # Replace items in list left to right
    for char in oldL:

        # If char is the same then skip a space
        if oldL[index] == newL[index]:
            index += 1

        else:
            oldL[index] = newL[index]
            index += 1
            if visual:
                print(oldL)

    index = 0

    # Map to string and return
    repStr = ''.join(map(str, oldL))

    return OPERDICT[nt](repStr)


def wSplit(line):
    """
    Takes one argument; returns a list of words

    :return: List of words in given string
    """

    index = 0
    srch = split(line)
    condenser = []
    finList = []

    for char in srch:
        if srch[index] == ' ':

            # Map condenser to string
            strItem = ''.join(map(str, condenser))

            # Remove space
            rev = strItem.replace(' ', '')

            # Append final list and reset condenser
            finList.append(rev)
            condenser = []
            index += 1

        else:
            condenser.append(srch[index])
            index += 1

    # Condenses last word in line
    strItem = ''.join(map(str, condenser))

    # Remove space
    rev = strItem.replace(' ', '')

    # Append final list and reset condenser
    finList.append(rev)
    condenser = []
    index += 1

    return finList


def sReplace(line, query, rep):
    """
    Takes three arguments; returns revised string

    :return: Revised string
    """

    # Split line, and define vars
    index = 0
    scan = wSplit(line)
    inl = False

    # Stops an infinite loop problem
    if query == rep:
        raise Exception('Cannot replace item')

    # Replaces query with replacement
    for word in scan:
        if query == scan[index]:
            repQ = replace(scan[index], rep)
            scan[index] = repQ
            inl = True
        else:
            index += 1

    # If the item is not in the list
    if not inl:
        raise Exception('String is not in line')

    # Reset index
    index = 0

    # Adds a space to the string to return it to its original state
    for item in scan:

        # If it is the last item in the list, break loop
        if index == len(scan) - 1:
            break
        scan[index] += ' '
        index += 1

    # Condense list and return string
    final = ''.join(map(str, scan))

    return final


def reverse(thing):
    """
    Takes one argument, reverses the input

    :return: reversed thing (keeps data type)
    """
    z, nt = split(thing)
    ret = []

    index = len(z) - 1

    for i in z:
        ret.append(z[index])
        index -= 1

    returned = ''.join(map(str, ret))

    return OPERDICT[nt](returned)
