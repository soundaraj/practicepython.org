import random
while True:
    dic = {1:'rock',
       2:'scissor',
       3:'paper'}
    print("enter the key to play",dic)
    a = input()
    b = random.choice(dic.keys())
    


    if a == dic.keys()[0]:
        if b == dic.keys()[1]:
            print "you win"
        else:
            print "you loss"
            if raw_input("Do u want to continue type 'yes'")=='yes':
                continue
            else:
                break
    if a == dic.keys()[1]:
        if b == dic.keys()[2]:
            print "you win"
        else:
            print "you loss"
            if raw_input("Do u want to continue type 'yes'") == 'yes':
                continue
            else:
                break
    if a == dic.keys()[2]:
        if b == dic.keys()[0]:
            print "you win"
        else:
            print "you loss"
            if raw_input("Do u want to continue type 'yes'")=='yes':
                continue
            else:
                break
    if a == b:
        print "match was tie"
        continue
            
        
