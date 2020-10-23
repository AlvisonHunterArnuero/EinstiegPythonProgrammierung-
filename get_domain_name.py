#Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
# #For example: domain_name("https://github.com/AlvisonHunterArnuero") == "github"
# Made with ❤️ in Python 3 by Alvison Hunter - October 22th, 2020
def domain_name(url):
    #list with the most common protocols to start cleaning the url
    lst_protocols =['http://','www.','https://','ftp','http://www.']
    #This is the part that we will extract, typically goes between the
    # protocol and domain, for example alvisonhunter in www.alvisonhunter.com
    subdomain = ''
    #the initial prefix of any Uniform Resource Locator we know of.
    protocol_type = url
    #the second or top level domain or this URL, example .com, .org, .edu, .net
    domain_suffix = ''
    #First, let's iterate the list to find any of its element on the current URL
    for el in lst_protocols:
        #If found, let us extract that part from this string
        if(url.find(el) != -1):
            protocol_type= url[len(el):]

        #now that we remove the protocol, let's find the domain
        domain_suffix = protocol_type.find('.')
        #if domain is found, let's remove it from the string and add it to subdomain
        if(domain_suffix != -1):
            subdomain = protocol_type[:domain_suffix]
        #If there is no dot, then let's simply return the string that was passed as URL
        else:
            subdomain = url

    #Having all the elements ready, the time has come for us to return it to the user
    print('We have successfully extracted {} from the given URL.'.format(subdomain))
    return subdomain

#Time to test these URLs out, my dear Pythonistas and pythoneers!
domain_name('http://google.com')
domain_name('http://google.co.jp')
domain_name('www.xakep.ru')
domain_name('https://youtube.com')
domain_name('cornisland')
domain_name('icann.org')
domain_name('https://github.com/AlvisonHunterArnuero')


