d1={}
d2={}
n=input()
m=input()
for i in n:
    if i in d1:
         d1[i] += 1
    else:
         d1[i] = 1
for i in m:
    if i in d2:
         d2[i] += 1
    else:
         d2[i] = 1
if d1==d2:
    print(1)
else:
    print(0)