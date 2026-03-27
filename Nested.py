
a=int(input("enter the upper range: "))
b=int(input("enter the lower range: "))

for num in range(a,b+1):
    if num>1:
        for i in range(2,num):
            if(num%i) == 0:
                print("the number is not a prime number",num)
                break
        else:
            print("the number is prime",num)