l = []

for i in range(1,51):
    l.append(i)

a= int(input())

a = int(a)

count = 0

for i in l:
    if(i%a==0 and i!=a):
        count+=1

print(count)