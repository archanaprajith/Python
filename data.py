data = {
    "john":{
         "Math":[85,90,95],
         "Science":[88,92,89],
         "Language":{"English":[78,80],"spanish":[85]}
    },
    "Alice":{
         "Math":[78,80,82],
         "Science":[90,85,88],
         "Language":{"English":[85,87],"french":[82,88]}
     },
    "bob":{
         "Math":[90,85],
         "Science":[85,87],
         "Language":{"English":[80],"french":[78,83]}
    },
}

#average of maths score
list1=[]
list1=(data["john"]["Math"])+(data["Alice"]["Math"])+(data["bob"]["Math"])
print(list1) 
avg=sum(list1)/len(list1)
print(avg)

#average of science score
list2=[]
list2=((data["john"]["Science"])+(data["Alice"]["Science"])+(data["bob"]["Science"]))
print(list2) 
avg1=sum(list2)/len(list2)
print(avg1)

#unique series
s = set(list2)
print(s)

#hscore
hscore=[80,82,85]
for i in data:
    data[i]["history"]=hscore
    print(data[i])

#sort
 
st =(data["john"]["Math"])+(data["john"]["Science"])+(data["john"]["Language"]["English"])+(data["john"]["Language"]["spanish"])
st1 =(data["Alice"]["Math"])+(data["Alice"]["Science"])+(data["Alice"]["Language"]["English"])+(data["Alice"]["Language"]["french"])
st2 =(data["bob"]["Math"])+(data["bob"]["Science"])+(data["bob"]["Language"]["English"])+(data["bob"]["Language"]["germen"])+

avg2=sum(st)/len(st)
avg3=sum(st1)/len(st1)
avg4=sum(st2)/len(st)2





