import re
import sys

def matchMailbox(str):
    validMailboxPattern = re.compile(r'^[A-Z0-9]+([-_\.]?[A-Z0-9]+)*$', re.IGNORECASE)
    match = validMailboxPattern.match(str)

    return bool(match)


def matchAt(str):
    validAt = re.compile(r'(@|_at_)')
    match = validAt.search(str)

    return bool(match)


def findAtPos(str):

    nonSymbol = str.rfind('_at_')
    symbol = str.rfind('@')

    if symbol > nonSymbol:
        return symbol
    elif (symbol < nonSymbol):
        return nonSymbol
    else:
        return None


def matchDomain(str):
    validDomain = re.compile(r'^([A-Z0-9]+((\.)?[A-Z0-9]+)*)+(\.|_dot_)$', re.IGNORECASE)
    match = validDomain.match(str)

    return bool(match)


def isIPDomain(str):
    validIP = re.compile(r'\[(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]\.){2}25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]\]$')
    match = validIP.search(str)

    return bool(match)


def matchExt(str):
    validExt = re.compile(r'(co\.nz|com\.au|co\.uk|com|co\.us|co\.ca)$', re.IGNORECASE)
    match = validExt.search(str)

    return bool(match)


def matchDomainAndExt(str):
    validDomainAndExt = re.compile(r'^([A-Z0-9]+((\.)?[A-Z0-9]+)*)+(\.|_dot_)(co\.nz|com\.au|co\.uk|com|co\.us|co\.ca)$', re.IGNORECASE)
    match = validDomainAndExt.match(str)

    return bool(match)


def containsWhitespace(str):
    whitespace = re.compile(' ')
    match = whitespace.search(str)

    return bool(match)

#write case for if any spaces exist
#need a case for missing domain? when extension is valid but there's no domain?
#I think that the domain is what comes immediately after the @ symbol
# rsplit 1 time for the @ symbol

def fullMatch(str):
    error_message = ""

    #str.replace('_at_', '@').replace('_dot_', '.').lower()

    #fullValidEmailRegex = re.compile(r'^([A-Z0-9]+([-_\.]?[A-Z0-9]+)*)+(@|_at_)([A-Z0-9]+((\.)?[A-Z0-9]+)*)+(\.|_dot_)(co\.nz|com\.au|co\.uk|com|co\.us|co\.ca)$', re.IGNORECASE)
    #match = fullValidEmailRegex.match(str)

    print

    if containsWhitespace(str):
        print (str + " <- Address contains whitespace")
        return

    if matchExt(str):
        if (str[-3:] == "com"):
            if (str[-8:-3] == "_dot_"):
                #print "Uses _dot_ correctly"
                #print str
                str = str[:-8] + "." + str[-3:] #replace _dot_ with .
                #print str
        elif (str[-6:] == "com.au"):
            if (str[-11:-6] == "_dot_"):
                #print "Uses _dot_ correctly"
                #print str
                str = str[:-11] + "." + str[-6:] #replace _dot_ with .
                #print str
        else:
            if (str[-10:-5] == "_dot_"):
                #print "Uses _dot_ correctly"
                #print str
                str = str[:-10] + "." + str[-5:] #replace _dot_ with .
                #print str


    if not matchAt(str):
        print (str + " <- Missing @ symbol")
        return
    else:
        if str[findAtPos(str)] == "@":
            atIndex = findAtPos(str)
        elif str[findAtPos(str):findAtPos(str) + 4] == "_at_":
            str = str[:findAtPos(str)] + "@" + str[(findAtPos(str) + 4):]
            atIndex = findAtPos(str)

        splitAddress = re.split('(@)', str) #split at the @ symbol

        if len(splitAddress) > 3: #if there are more than 3 parts
            print (str + " <- Too many @ symbols")
            return

        #separate string into 3 parts
        mailbox = splitAddress[0] #mailbox is the part before the @ symbol
        atSymbol = splitAddress[1] #atSymbol is the @ symbol
        domainAndExt = splitAddress[2] #domainAndExt is the part after the @symbol

        #mailbox doesn't fit the regex
        if not matchMailbox(mailbox):
            consecutiveSeparators = re.compile(r'(\.|-|_)(\.|-|_)')
            if bool(consecutiveSeparators.search(mailbox)):
                print (str + " <- Mailbox contains consecutive separators") #cannot contain consecutive separators (mailbox)
                return
            elif len(mailbox) == 0:
                print (str + " <- Missing mailbox")
                return
            else:
                print (str + " <- Invalid mailbox")
                return

        if not matchDomainAndExt(domainAndExt): #if there is an error in the domain or extension
            consecutiveDots = re.compile(r'(\.|_dot_)(\.|_dot_)') #looks for two dots next to eachother
            if bool(consecutiveDots.search(domainAndExt)):
                print (str + " <- Domain contains consecutive separators") #cannot contain consecutive separators (domain)
                return

            #evaluate the extension first
            validExt = re.compile(r'(co\.nz|com\.au|co\.uk|com|co\.us|co\.ca)$', re.IGNORECASE)
            domainAndExtSplit = re.split(validExt, domainAndExt) #split at the extension

            #if there is an invalid extension (extension doesn't split)
            if len(domainAndExtSplit) < 2:
                dotSeparator = re.compile(r'[A-Z0-9]\.[A-Z0-9]', re.IGNORECASE)
                #says if there are no two characters separated by a dot, there must be a missing extension
                if not isIPDomain(domainAndExt) and not re.search(dotSeparator, domainAndExt):
                    print (str + " <- Missing extension")
                    return
                elif not isIPDomain(domainAndExt):
                    print (str + " <- Invalid extension")
                    return
            else:
                domain = domainAndExtSplit[0] #first part is the domain
                ext = domainAndExtSplit[1] #second part is the extension

                if not matchDomain(domain): #if the domain doesn't match the regex
                    if len(domain) == 0 or domain == ".": #if the domain is a dot or nothing
                        print (str + " <- Missing domain")

                    elif not isIPDomain(domainAndExt): #if the domain and extension is not an IP
                        print (str + " <- Invalid domain") #the domain is invalid
                        return

    # If the _dot_ couldn't be replaced anywhere else other than before the extension
    # this would need to change (remove replace dot and use the string indexing)
    # _dot_ can be anywhere that a . can be, but there can only be one _at_|@
    print (str.replace('_dot_', '.').lower()) #replace the _dot_s
    return


def main():

    # User Input
    for line in sys.stdin:
        line = line.strip()
        fullMatch(line)

if __name__ == "__main__":
    main()
