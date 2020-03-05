import re
import sys

# Evaluate when IGNORECASE should be used
# Is it only for mailbox names, or can it be for ext/domain as well?

# Get correct format for IP domains

# working
def matchMailbox(str):
    validMailboxPattern = re.compile(r'^[A-Z0-9]+([-_\.]?[A-Z0-9]+)*$', re.IGNORECASE)
    match = validMailboxPattern.match(str)

    return bool(match)


# working
def matchAt(str):
    validAt = re.compile(r'(@|_at_)')
    match = validAt.search(str)

    return bool(match)

def findAt(str):

    nonSymbol = str.rfind('_at_')
    symbol = str.rfind('@')

    if symbol > nonSymbol:
        return symbol
    elif (symbol < nonSymbol):
        return nonSymbol
    else:
        return None


# working
# domains finish with a dot
def matchDomain(str):
    validDomain = re.compile(r'^([A-Z0-9]+((\.)?[A-Z0-9]+)*)+(\.|_dot_)$', re.IGNORECASE)
    match = validDomain.match(str)

    return bool(match)


#dot separated numbers of no limit
#should there be a cap on the amount of digits?
def isIPDomain(str):
    validIP = re.compile(r'\[([0-9]+((\.)?[0-9]+)*)\]$', re.IGNORECASE)
    match = validIP.search(str)

    return bool(match)


# Maybe return the extension if it's not valid
def matchExt(str):
    validExt = re.compile(r'(co\.nz|com\.au|co\.uk|com|co\.us|co\.ca)$', re.IGNORECASE)
    #maybe don't use IGNORECASE here
    match = validExt.search(str)

    return bool(match)


def matchDomainAndExt(str):
    validDomainAndExt = re.compile(r'^([A-Z0-9]+((\.)?[A-Z0-9]+)*)+(\.|_dot_)(co\.nz|com\.au|co\.uk|com|co\.us|co\.ca)$', re.IGNORECASE)
    match = validDomainAndExt.match(str)

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

    '''
    elif (str[-5:] == "co.nz" or str[-5:] == "co.uk" or str[-5:] == "co.ca" or str[-5:] == "co.us"):
        print("Other valid ext")
    '''

    print()

    if (matchExt(str)):
        if (str[-3:] == "com"):
            if (str[-8:-3] == "_dot_"):
                #print("Uses _dot_ correctly")
                #print(str)
                str = str[:-8] + "." + str[-3:] #replace _dot_ with .
                #print(str)
        elif (str[-6:] == "com.au"):
            if (str[-11:-6] == "_dot_"):
                #print("Uses _dot_ correctly")
                #print(str)
                str = str[:-11] + "." + str[-6:] #replace _dot_ with .
                #print(str)
        else:
            if (str[-10:-5] == "_dot_"):
                #print("Uses _dot_ correctly")
                #print(str)
                str = str[:-10] + "." + str[-5:] #replace _dot_ with .
                #print(str)
    elif not (isIPDomain(str)):
        print("Bad extension!!")

    if matchAt(str):
        if str[findAt(str)] == "@":
            atIndex = findAt(str)
        elif str[findAt(str):findAt(str) + 4] == "_at_":
            str = str[:findAt(str)] + "@" + str[(findAt(str) + 4):]
            atIndex = findAt(str)

        '''
        print("Formatted @ symbol")
        print(str)
        print("atIndex")
        print(atIndex)
        '''

    # Need to make it clear how the domain is identified relative to the @ symbol

    # then split at the valid @ symbol
    # then check the mailbox and domain(s)


    if matchAt(str):
        #yes @ symbol exists

        splitAddress = re.split('(@|_at_)', str) #split at the @ symbol
        #print splitAddress

        if len(splitAddress) > 3: #if there are more than 3 parts

            print(str + " <- Too many @ symbols")
            return
            #return str + error_message

        #separate string into 3 parts
        mailbox = splitAddress[0] #mailbox is the part before the @ symbol
        atSymbol = splitAddress[1] #atSymbol is the @ symbol
        domainAndExt = splitAddress[2] #domainAndExt is the part after the @symbol

        #need a case for missing mailbox
        if not matchMailbox(mailbox):
            consecutiveSeparators = re.compile(r'(\.|-|_)(\.|-|_)')
            if bool(consecutiveSeparators.search(mailbox)):
                print(str + " <- Mailbox contains consecutive separators") #cannot contain consecutive separators (mailbox)
                return
            else:
                print(str + " <- Invalid mailbox")
                return
                #return str + error_message

        if not matchDomainAndExt(domainAndExt): #if there is an error in the domain or extension
            consecutiveDots = re.compile(r'(\.|_dot_)(\.|_dot_)')
            #this block might fit better in an outer condition so it catches consecutive dots in a mailbox as well
            if bool(consecutiveDots.search(domainAndExt)):
                print(str + " <- Domain contains consecutive separators") #cannot contain consecutive separators (domain)
                return

            #if matchExt(domainAndExt): #if there is a valid extension
            validExt = re.compile(r'(co\.nz|com\.au|co\.uk|com|co\.us|co\.ca)$', re.IGNORECASE)
            domainAndExtSplit = re.split(validExt, domainAndExt) #split at the extension

            #says if there is an invalid extension (extension is not split)
            if len(domainAndExtSplit) < 2:
                dotSeparator = re.compile(r'[A-Z0-9]\.[A-Z0-9]', re.IGNORECASE)
                #says if there are no two characters separated by a dot, there must be a missing extension
                if not isIPDomain(domainAndExt) and not re.search(dotSeparator, domainAndExt):
                    print(str + " <- Missing extension")
                    return
                elif not isIPDomain(domainAndExt):
                    print(str + " <- Invalid extension")
                    return
            else:
                domain = domainAndExtSplit[0] #first part is the domain
                ext = domainAndExtSplit[1] #second part is the extension

                if not matchDomain(domain): #if the domain doesn't match the regex
                    if not isIPDomain(domainAndExt): #if the domain and extension is not an IP
                        print(str + " <- Invalid domain") #the domain is invalid
                        return
                        #return str + error_message

                #nested in the invlaid domain or extension
                #the domainAndExt isn't an IP

    #change to if not matchAt, else for better readability
    else:
        #no @ symbol
        print(str + " <- Missing @ symbol")
        return
        #return str + error_message

    # If the _dot_ couldn't be reaplaced anywhere else other thatn before the extension
    # this would need to change (remove replace dot and use the string indexing)
    # .replace('_at_', '@')
    print(str.replace('_dot_', '.').lower())
    return


def main():

    print()
    print()
    print("VALID EMAIL ADDRESSES")
    print()

    fullMatch('a.b_c-d@domain.com')
    fullMatch('first_last@hotmail.co.nz')
    fullMatch('firstlast_at_outlook_dot_com')
    fullMatch('CEO@InsuroCorp.com')
    fullMatch('gerry_at_research.techies_dot_co.uk')
    fullMatch('cath@[139.80.91.50]')
    fullMatch('b_at_g_dot_com')
    fullMatch('brad@lol.com')
    fullMatch('adsad.sdadsa@lol.com')
    fullMatch('123_123@lolc.com')
    fullMatch('a_l@[123.123.123.123]')
    fullMatch('la.a@l.co.co.co.nz')
    fullMatch('mailbox@a.co.nz')
    fullMatch('mailbox@cs.co.uk')
    fullMatch('mailbox@l.co.uk')
    fullMatch('mail_box@domain.com')
    fullMatch('email_l@ex.l.com')
    fullMatch('a-b-c@l.com')

    print()
    print()
    print("INVALID EMAIL ADDRESSES")
    print()

    fullMatch('name@[123.12.12.12].com')
    fullMatch('first_last@hotmail.com.nz')
    fullMatch('maffu@cs.otago.ac.nz')
    fullMatch('bob@gmail..com')
    fullMatch('a-@gmail.com')
    fullMatch('BIG@@@')
    fullMatch('example.com')
    fullMatch('email@example..example.com')
    fullMatch('A@b@c@domain.com')
    fullMatch('.test@domain.com')
    fullMatch('test@domain..com')
    fullMatch(' firstlast@outlook.com')
    fullMatch('firstlast@outlook.com ')
    fullMatch('plainaddress')
    fullMatch('#@%^%#$@#$@#.com')
    fullMatch('@example.com')
    fullMatch('Joe Smith <email@example.com>')
    fullMatch('email.example.com')
    fullMatch('email@example@example.com')
    fullMatch('.email@example.com')
    fullMatch('email.@example.com')
    fullMatch('email..email@example.com')
    fullMatch('email@example.com (Joe Smith)')
    fullMatch('email@example')
    fullMatch('email@example.')
    fullMatch('email@-example.com')
    fullMatch('a_$b@cs.com')
    fullMatch('a___b@lol.com')
    fullMatch('a--b@cs.com')
    fullMatch('ab_-l@a.com')
    fullMatch('la@l.com_')
    fullMatch('a_@l.com')
    fullMatch('a-$a@s.com')
    fullMatch('at_at_at_at_dot_com')

    print()
    print()

    findAt("email@example.com")
    findAt("darcyknox_at_outlook.com")


if __name__ == "__main__":
    main()
