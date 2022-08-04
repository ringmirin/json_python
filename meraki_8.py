# ["neelam""programer","24","2400",]
# ["komal","trainer","24","20000"]
# ["anuradha","HR","25","40000"]
# ["Abhishek","manager","29","63000"]


# ab aapko 4 dictionaries create karni hai jaise ki emp1 emp2 emp3 and emp4.
# har ek employee ka dictionary main name,designation,age and salary honi chahiye.
# aur ye sab dictionary ki keys hai jismai maine list main value di hai. Iska use kar 
# ke aapko ek json file create karni hai? Jaise ki niche diya hai.

import json
a=["neelam","programer","24","2400"]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"]
e=["name","designation","age","salary"]

dict={}
dict1={}
dict2={}
dict3={}
dict4={}

i=1
while i<len(a):
   dict1[e[i]]=a[i]
   dict2[e[i]]=b[i]
   dict3[e[i]]=c[i]
   dict4[e[i]]=d[i]
   i+=1
dict["emp1"]=dict1
dict["emp2"]=dict2
dict["emp3"]=dict3
dict["emp4"]=dict4
print(dict)

with open("meraki8.json","a") as fh:
   j=json.dump(dict,fh,indent=4)