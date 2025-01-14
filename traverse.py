str1=input("enter the string")
list1 = []
list2 = []
for i in str1:
    list1.append(i)
for j in range(len(list1)-1,-1,-1):
    list2.append(list1[j])

for i in range(len(list2)):
    print(list2[i],end=" ")
   

   

