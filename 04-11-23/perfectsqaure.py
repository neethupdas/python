lis=[]
def square(a,b):




    for i in range(a,b+1):
        j=1
        while j*j<=i:
            if j*j==i:
               lis.append(str(i))
            j=j+1
        i=i+1
    return lis
print(square(1000,9999))
liste=[]
for i in lis:
    count=0
    for z in i:
        if int(z)%2==0:
            count=count+1
        else:
            break
    if count==4:
        liste.append(int(i))
print("even list is \n",liste)
