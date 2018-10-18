import random
def fun():
    while True:
        print ("enter your choice \n 1.weak password \n 2.medium password \n 3.strong password \n type 'exit' to escape")
        c = raw_input()
        if c == 'exit':
            break
        elif c == '1':
            print 'abcdefgh'
        elif c == '2':
            print 'abcdABCD'
        elif c == '3':
            s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+_)(*&^%$#@!"
            a = random.sample(s,8)
            print ''.join(a)
        else:
            print "please type correct value"
            break
fun()
