import random
a = input("enter comma seperated name: ")
b = a.split(",")
print(b)
c = len(b)
print(c)
num = random.randint(0,c-1)
d = b[num]
print(d + " pay bill")
r = random.choice(b)
print(r + " pay")