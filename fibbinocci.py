def fibb(num):
    if num > 1:
        a = range(2,num)
        b = []
        c = [1,2]
        for i in a:
            i = c[i-2] + c[i-1]
            c.append(i)
        print(c)
f = int(input("enter the number"))
fibb(f)
