x=int(input("enter first number"))
temp=x
sum = 0
while x > 0:
    y = x%10
    sum += y**3
    print(sum)
    x = int(x/10)

if (temp==sum):
     print("is a armstrong number")
else:    
     print("is not a armstrong number")









