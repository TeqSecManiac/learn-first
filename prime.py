

num = 29

num = int(input("Enter a number: "))

flag = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
           
            flag = True
          
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")