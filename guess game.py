import random
while True:
    a = random.choice(range(1,10))
    b = 0
    b = input("enter the guessing number")
    c = 0
    if b == "exit":
        break
    b = int(b)
    c +=1
    if a > b:
        print "you guess too low"
        continue
    if a < b:
        print "you guess too high"
        continue
    if a == b:
        print "you guess exactly correct"
        continue
print(c)
