import re
import sys

# Evaluate when IGNORECASE should be used
# Is it only for mailbox names, or can it be for ext/domain as well.

fullValidEmailRegex = re.compile(r'^([A-Z0-9]+([-_\.]?[A-Z0-9]+)*)+(@|_at_)([A-Z0-9]+((\.)?[A-Z0-9]+)*)+(\.|_dot_)(co\.nz|com\.au|co\.uk|com|co\.us|co\.ca)$', re.IGNORECASE)


# working
def matchMailbox(str):
    validMailboxPattern = re.compile(r'^[A-Z0-9]+([-_\.]?[A-Z0-9]+)*$', re.IGNORECASE)
    match = validMailboxPattern.match(str)
    '''
    if match is not None:
        return True
    else:
        return False # Invalid mailbox
    '''
    return bool(match)


# working
def matchAt(str):
    validAt = re.compile(r'(@|_at_)')
    match = validAt.search(str)

    return bool(match)


# working
# domains finish with a period
def matchDomain(str):
    validDomain = re.compile(r'^([A-Z0-9]+((\.)?[A-Z0-9]+)*)+(\.|_dot_)$', re.IGNORECASE)
    match = validDomain.match(str)

    return bool(match)


def isIPDomain(str):
    validIP = re.compile(r'^\[([0-9]+((\.)?[0-9]+)*)\]$', re.IGNORECASE)
    match = validIP.match(str)

    return bool(match)


def matchExt(str):
    validExt = re.compile(r'(co\.nz|com\.au|co\.uk|com|co\.us|co\.ca)$', re.IGNORECASE)
    #maybe don't use IGNORECASE here
    match = validExt.match(str)

    return bool(match)


def matchDomainAndExt(str):
    validDomainAndExt = re.compile(r'^([A-Z0-9]+((\.)?[A-Z0-9]+)*)+(\.|_dot_)(co\.nz|com\.au|co\.uk|com|co\.us|co\.ca)$', re.IGNORECASE)
    match = validDomainAndExt.match(str)

    return bool(match)


def fullMatch(str):
    error_message = ""
    match = fullValidEmailRegex.match(str)

    if bool(match):
        print str.replace('_at_', '@').replace('_dot_', '.').lower() #working
    else:

        if not matchAt(str):
            #no @ symbol
            error_message += " <- Missing @ symbol"
        else:
            #yes @ symbol
            splitAddress = re.split('(@|_at_)', str) #split at the @ symbol
            print splitAddress

            if len(splitAddress) > 3: #if there are more than 3 parts
                error_message += " <- Too many @ symbols"

            mailbox = splitAddress[0]
            atSymbol = splitAddress[1]
            domainAndExt = splitAddress[2]

            if not matchMailbox(mailbox):
                error_message += " <- Invalid mailbox"

            if not matchDomainAndExt(domainAndExt):
                domainAndExtSplit = re.split('(co\.nz|com\.au|co\.uk|com|co\.us|co\.ca)', domainAndExt)
                domain = domainAndExtSplit[0]
                ext = domainAndExtSplit[1]
                print "Domain = " + domain
                print "Ext = " + ext

                if not matchDomain(domain):
                    if not isIPDomain(domainAndExt):
                        error_message += " <- Invalid domain"
                else:
                    if not matchExt(str) and not isIPDomain(domainAndExt):
                        error_message += " <- Invalid extension"


        print(str + error_message)


def main():

    if matchMailbox('darcy-_knox'):
        print "working mailbox function: mailbox is valid"

    if matchAt("darcyknox@outlook.com"):
        print "working @ function"

    if matchDomain("domain.domain.domain."):
        print "working domain function: domain is valid"

    if isIPDomain("[123.123.123.123]"):
        print "IP domain"

    fullMatch("darcyknox@outlook_dot_company")


if __name__ == "__main__":
    main()
