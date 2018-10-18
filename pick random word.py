import random
def fun():
    with open("sowpods.txt",'r') as f:
        f1 = f.readlines()
        f2 = random.choice(f1)
        print(f2)
