i=-1
a=[]
b=[]
while i==-1:
    z=int(input("enter number to list1 or '0' to exit: \n"))
    if z==0:
        break;
    else:
        a.append(z)

#print(a)

while i==-1:
    z=int(input("\nenter number to list2 or '0' to exit: \n"))
    if z==0:
        break;
    else:
        b.append(z)

#print(b)

if len(a)==len(b):
    print("list are same length\n",len(a))
else:
    print("\n list1:",len(a),"\n list2:",len(b))

if sum(a)==sum(b):
    print("\nboth lists have the same sum",sum(a))
else:
    print("\nsum of list 1:",sum(a),"\nsum of list 2:",sum(b))
for n in a:
    for z in b:
        if n==z:
           print("\n",n,"is in both at list1 in position",a.index(n),"and list2 in position",b.index(n))
    
