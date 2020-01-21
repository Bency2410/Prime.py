a=int(input("Enter a number: "))
flag=0
for i in range(2,(a//2+1)):
        if(a%i==0):
            flag=1
        else:
            flag=0
if(flag==0):
    print(a ,"is prime")
else:
    print(a ,"is not prime")