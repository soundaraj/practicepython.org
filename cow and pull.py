import random
def fun(number,user):
    cb = [0,0]
    for i in range(len(number)):
        if number[i] == user[i]:
            cb[1] += 1
        else:
            cb[0] += 1
    return cb
if __name__ == "__main__":
    number = str(random.randint(0,9999))
    #print number
    guesses =0
    while True:
        user = raw_input("enter the number")
        cowbull = fun(number,user)
        print "cow",cowbull[0],"bull",cowbull[1]
        if user == "exit":
            break
        guesses += 1
        if cowbull[1] == 4:
            print "game over"
            
            print guesses
            break
