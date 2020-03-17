import re
import sys

# Etude-1 Email Addresses
# Author: Darcy Knox
# Date: March 2020

# The program takes string input(s) from the user, and determines whether the
# string is a valid email address according to the specifications outlined in
# the Etude 1 Problem Description

# Function to match the mailbox part of the address
def matchMailbox(str):
    validMailboxPattern = re.compile(r'^[A-Z0-9]+([-_\.]?[A-Z0-9]+)*$', re.IGNORECASE)
    match = validMailboxPattern.match(str)

    return bool(match)


# Function to find an @ symbol in a string
def matchAt(str):
    validAt = re.compile(r'(@|_at_)')
    match = validAt.search(str)

    return bool(match)


# Function to find the right-most @ symbol in a string
def findAtPos(str):

    nonSymbol = str.rfind('_at_')
    symbol = str.rfind('@')

    if symbol > nonSymbol:
        return symbol
    elif (symbol < nonSymbol):
        return nonSymbol
    else:
        return None


# Function to match the domain part of the address
def matchDomain(str):
    validDomain = re.compile(r'^([A-Z0-9]+((\.)?[A-Z0-9]+)*)+(\.|_dot_)$', re.IGNORECASE)
    match = validDomain.match(str)

    return bool(match)


# Function to search for whether a string attempts to use an IP address
def hasIPDomain(str):
    validIP = re.compile(r'\[.+\]$')
    match = validIP.search(str)

    return bool(match)


# Function to match a valid IP address
def matchIPDomain(str):
    validIP = re.compile(r'^\[((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\]$')
    match = validIP.match(str)

    return bool(match)


# Function to find a valid extension at the end of a string
def matchExt(str):
    validExt = re.compile(r'(co\.nz|com\.au|co\.uk|com|co\.us|co\.ca)$', re.IGNORECASE)
    match = validExt.search(str)

    return bool(match)


# Function to match a fully valid domain and extension
def matchDomainAndExt(str):
    validDomainAndExt = re.compile(r'^([A-Z0-9]+((\.)?[A-Z0-9]+)*)+(\.|_dot_)(co\.nz|com\.au|co\.uk|com|co\.us|co\.ca)$', re.IGNORECASE)
    match = validDomainAndExt.match(str)

    return bool(match)


# Function to check for any whitespace within a string
def containsWhitespace(str):
    whitespace = re.compile(' ')
    match = whitespace.search(str)

    return bool(match)


# Function to check for any invalidities
def fullMatch(str):

    if containsWhitespace(str):
        print (str + " <- Address contains whitespace")
        return

    # if a valid extension is used
    # replace the _dot_ preceding the extension first
    if matchExt(str):
        # If extension is preceded with _dot_ it is changed to a . immediately
        # Position of dot may be different depending on the extension
        if (str[-3:] == "com"):
            if (str[-8:-3] == "_dot_"):
                str = str[:-8] + "." + str[-3:] #replace _dot_ with .
        elif (str[-6:] == "com.au"):
            if (str[-11:-6] == "_dot_"):
                str = str[:-11] + "." + str[-6:] #replace _dot_ with .
        else:
            if (str[-10:-5] == "_dot_"):
                str = str[:-10] + "." + str[-5:] #replace _dot_ with .

    #str = str.replace('_dot_', '.')


    # if there's no @ symbol
    if not matchAt(str):
        print (str + " <- Missing @ symbol")
        return
    else:
        # replace the furthest right instance of _at_ with @
        # all other _at_ instances are considered literal _at_
        # note: _at_ is 4 chars long
        if str[findAtPos(str):findAtPos(str) + 4] == "_at_":
            str = str[:findAtPos(str)] + "@" + str[(findAtPos(str) + 4):]

        str = str.replace('_dot_', '.')

        splitAddress = re.split('(@)', str) # split at the @ symbol


        # if there are more than 3 parts to the address
        if len(splitAddress) > 3:
            print (str + " <- Too many @ symbols")
            return

        # separate string into 3 parts
        mailbox = splitAddress[0] # mailbox is the part before the @ symbol
        atSymbol = splitAddress[1] # atSymbol is the @ symbol
        domainAndExt = splitAddress[2] # domainAndExt is the part after the @symbol

        # mailbox doesn't fit the regex
        if not matchMailbox(mailbox):
            consecutiveSeparators = re.compile(r'(\.|-|_)(\.|-|_)')
            if bool(consecutiveSeparators.search(mailbox)):
                print (str + " <- Mailbox contains consecutive separators") # cannot contain consecutive separators (mailbox)
                return
            elif len(mailbox) == 0:
                print (str + " <- Missing mailbox")
                return
            else:
                print (str + " <- Invalid mailbox")
                return

        if not matchDomainAndExt(domainAndExt): # if there is an error in the domain or extension
            consecutiveDots = re.compile(r'(\.|_dot_)(\.|_dot_)') # looks for two dots next to eachother
            if bool(consecutiveDots.search(domainAndExt)):
                print (str + " <- Domain contains consecutive separators") # cannot contain consecutive separators (domain)
                return

            # evaluate the extension first
            validExt = re.compile(r'(co\.nz|com\.au|co\.uk|com|co\.us|co\.ca)$', re.IGNORECASE)
            domainAndExtSplit = re.split(validExt, domainAndExt) # split at the extension
            domain = domainAndExtSplit[0] # first part is the domain

            # if there is an invalid extension (extension doesn't split)
            if len(domainAndExtSplit) < 2:
                dotSeparator = re.compile(r'[A-Z0-9]\.[A-Z0-9]', re.IGNORECASE)
                # says if there are no two characters separated by a dot, there must be a missing extension
                if not hasIPDomain(domainAndExt) and not re.search(dotSeparator, domainAndExt):
                    print (str + " <- Missing extension")
                    return
                elif not hasIPDomain(domainAndExt):
                    print (str + " <- Invalid extension")
                    return
                elif hasIPDomain(domainAndExt) and len(domainAndExt.split('[')[0]) > 0:
                    print(str + " <- IP address cannot have preceeding domain")
                    return
                elif not matchIPDomain(domain):
                    print (str + " <- Invalid IP address")
                    return
            else:
                ext = domainAndExtSplit[1] # second part is the extension
                if domain[-1] != ".":
                    print (str + " <- Missing extension")
                    return

                if not matchDomain(domain): # if the domain doesn't match the regex
                    if len(domain) == 0 or domain == ".": # if the domain is a dot or nothing
                        print (str + " <- Missing domain")
                        return
                    elif not hasIPDomain(domainAndExt): # if the domain and extension is not an IP
                        print (str + " <- Invalid domain") # the domain is invalid
                        return

    # Valid email
    print (str.replace('_dot_', '.').lower()) #replace the _dot_s
    return


def main():

    # User Input
    for line in sys.stdin:
        line = line.strip()
        fullMatch(line)

if __name__ == "__main__":
    main()
