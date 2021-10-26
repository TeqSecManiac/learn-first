
a = input("enter the head")
a=int(a)
b = input("enter 0 for left and 1 for right")
print("enter the sequence")
b=int(b)
c=[]
for i in range(0,7):
    d=input()
    c.append(d)
d=0
e=200
print("seek sequence")


list1=[]
list2=[]
for x in c:
    if int(x) < int(a):
        list2.append(int(x))


    if int(x) > int(a):
        list1.append(int(x))

if b==0:
    while(len(list2)!=1):
        f=min(list2)
        print("SE",f)
        list2.remove(f)
    print("SE{0}\nSE{1}\nSE{2}".format(list2[0],d,e))
    while(len(list1) != 1):
        f=min(list1)
        print("SE",f)
        list1.remove(f)
    print("SE",list1[0])    

elif b==1:
    print ("head is ",a)
    while(len(list1) != 1):
        f=min(list1)
        print("SE",f)
        list1.remove(f)
    print("SE{0}\nSE{1}\nSE{2}".format(list1[0],e,d))


    while(len(list2)!=1):
        f=min(list2)
        print("SE",f)
        list2.remove(f)
    print("SE",list2[0])


else:
    print("invalid option")
