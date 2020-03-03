import re
import sys

# Evaluate when IGNORECASE should be used
# Is it only for mailbox names, or can it be for ext/domain as well.


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

    #str.replace('_at_', '@').replace('_dot_', '.').lower()

    #fullValidEmailRegex = re.compile(r'^([A-Z0-9]+([-_\.]?[A-Z0-9]+)*)+(@|_at_)([A-Z0-9]+((\.)?[A-Z0-9]+)*)+(\.|_dot_)(co\.nz|com\.au|co\.uk|com|co\.us|co\.ca)$', re.IGNORECASE)
    #match = fullValidEmailRegex.match(str)

    print
    if matchAt(str):
        #yes @ symbol
        splitAddress = re.split('(@|_at_)', str) #split at the @ symbol
        #print splitAddress

        if len(splitAddress) > 3: #if there are more than 3 parts
            print str + " <- Too many @ symbols"
            return
            #return str + error_message

        mailbox = splitAddress[0]
        atSymbol = splitAddress[1]
        domainAndExt = splitAddress[2]

        if not matchMailbox(mailbox):
            str + " <- Invalid mailbox"
            return
            #return str + error_message

        if not matchDomainAndExt(domainAndExt): #if there is an error in the domain or extension

            #if matchExt(domainAndExt): #if there is a valid extension
            validExt = re.compile(r'(co\.nz|com\.au|co\.uk|com|co\.us|co\.ca)$', re.IGNORECASE)
            domainAndExtSplit = re.split(validExt, domainAndExt) #split at the extension


            #problem here
            if len(domainAndExtSplit) < 2:
                print "Domain and ext " + domainAndExt
                dotSeparator = re.compile(r'[A-Z0-9]\.', re.IGNORECASE)
                if not isIPDomain(domainAndExt) and not re.search(dotSeparator, domainAndExt):
                    print str + " <- Missing extension"
                    return
            else:
                print domainAndExtSplit
                domain = domainAndExtSplit[0] #first part is the domain
                ext = domainAndExtSplit[1] #second part is the extension
                print "Domain = " + domain
                print "Ext = " + ext

                if not matchDomain(domain): #if the domain doesn't match the regex
                    print "Split domains"
                    print domain.split(".")
                    if not isIPDomain(domainAndExt): #if the domain and extension is not an IP
                        print str + " <- Invalid domain" #the domain is invalid
                        return
                        #return str + error_message

                #nested in the invlaid domain or extension
                #the domainAndExt isn't an IP
                elif not isIPDomain(domainAndExt):
                    splitDomains = re.split('\.', domainAndExt)
                    #print splitDomains
                    if len(domainAndExt.split(".")) < 2:
                        print "This one"
                        print str + " <- Missing extension"
                        return
                        #return str + error_message
                    else:
                        print str + " <- Invalid extension"
                        return
                        #return str + error_message
    else:
        #no @ symbol
        print str + " <- Missing @ symbol"
        return
        #return str + error_message


    print str.replace('_at_', '@').replace('_dot_', '.').lower()
    return


def main():

    '''
    #TESTING

    if matchMailbox('darcy-_knox'):
        print "working mailbox function: mailbox is valid"

    if matchAt("darcyknox@outlook.com"):
        print "working @ function"

    if matchDomain("domain.domain.domain."):
        print "working domain function: domain is valid"

    if isIPDomain("[123.123.123.123]"):
        print "IP domain"
    '''
    print
    print "Valid email addresses"
    print
    fullMatch('darcy_knox@hotmail.co.nz')
    fullMatch('darcyknox_at_outlook_dot_com')
    fullMatch('CEO@InsuroCorp.com')

    #fullMatch('gerry_at_research.techies_dot_co.uk')
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

    print
    print "Invalid email addresses"
    print

    fullMatch('darcy_knox@hotmail.com.nz')

    fullMatch('maffu@cs.otago.ac.nz')





    fullMatch('bob@gmail..com')


    fullMatch('a-@gmail.com')
    fullMatch('BIG@@@')
    fullMatch('example.com')

    fullMatch('email@example..example.com')

    fullMatch('A@b@c@domain.com')
    fullMatch('.test@domain.com')
    fullMatch('test@domain..com')
    fullMatch(' darcyknox@outlook.com')
    fullMatch('darcyknox@outlook.com ')
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
    fullMatch('email@-example.com')




    fullMatch('a_$b@cs.com')
    fullMatch('a___b@lol.com')
    fullMatch('a--b@cs.com')


    fullMatch('ab_-l@a.com')

    fullMatch('la@l.com_')
    fullMatch('a_@l.com')

    fullMatch('a-$a@s.com')



if __name__ == "__main__":
    main()
