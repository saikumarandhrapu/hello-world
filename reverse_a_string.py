x=input("enter the string")
l=x.strip()
l1=[]
i=len(l)-1
while i>=0:
    l1.append(l[i])
    i-=1
output="".join(l1)
print(output)
