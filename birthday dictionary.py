'birth day dictinaries'
import json
def bday():
    dic_bday = {
        "naveen": "06/12/2016",
        "akash": "26/12/2004",
        "abi": "20/08/2010"
        }
    while True:
        print "we know these person's bday dates  "
        for j in dic_bday:
            print j
        i = raw_input("Who's birthday do you want to look up? ")
        if i in dic_bday:
            print ' '
            print i+"'s birthday is ",dic_bday[i]
            print ' '
        else:
            print "Error! Enter correct name"
bday()
