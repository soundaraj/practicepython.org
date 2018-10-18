file1 = open("happynumbers.txt",'r')
file2 = open("primenumbers.txt",'r')
a = []
b = []
c = []
f1 = file1.readline()
f2 = file2.readline()
while f1:
    a.append(int(f1))
    f1 = file1.readline()
while f2:
    b.append(int(f2))
    f2 = file2.readline()
for i in a:
    if i in b:
        c.append(i)
print(c)
        
