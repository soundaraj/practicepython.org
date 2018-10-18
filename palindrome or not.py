'''
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
'''


string = raw_input("enter the string\t")
if string == string[::-1]:
    print "this string is palindrome"
else:
    print "this string is not palindrome"
