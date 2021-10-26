# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def signup():
   n=input("Enter the username:")
   m=input("Enter the password:")
   d[n]=m

def login():
   i=1
   while(i<=3):
       n=input("Enter the username:")
       m=input("Enter the password:")
       s=d[n]
       if(s==m and n==d.key('s')):
           print("Successfully Login")
           break;
       else:
           print(" try again")
           i=i+1
   if i==4:
       print("Your chances are over. Please try after sometime")
 
d={}
for i in range(ord('A'),ord('Z')):
    d[chr(i)]=chr(i)
print("Welcome to this application",end="")
h=int(input("Enter either 1 for Signup or 0 for Login:"))
if(h==1):
    signup()
    login()
elif(h==2):
    login()
else:
    print("Input not recognised")