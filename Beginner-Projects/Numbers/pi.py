import math
a = str(math.pi).split('.')[1]
print(a)
inp = int(input('input for upto which decimal place: '))
l = []
str = '3.'
for x in range(inp):
    l.append(a[x])
z = ''.join(l)
str += z
print(str)