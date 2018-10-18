def fun():
    a = raw_input("enter the string\t")
    b = a.split(' ')
    c = b[::-1]
    print(' '.join(c))
fun()
