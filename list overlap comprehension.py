import random
random_list1 = random.sample(range(100),10)
random_list2 = random.sample(range(100),15)
print(random_list1)
print(random_list2)
d = list(set([w for w in random_list1 for q in random_list2 if w==q]))
print(d)
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = list(set([x for x in a for y in b if x==y]))
print(c)
