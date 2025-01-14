ch=int(input("enter a number :"))
for i in range(1,ch+1):
    for k in range(ch,i,-1):
      print(end=" ")
    for j in range(1,i+1,1):
       print(j,end=" ")
    print()
    f=ch
for i in range(1,ch):
    for k in range(1,i+1):
      print(end=" ")
    for j in range(1,f):
       print(j,end=" ")
    print()
    f=1