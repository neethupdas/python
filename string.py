n=input("enter a string with repeated words")
k="$"
res=n[0]+n[1:].replace(n[0],k)
print(res)
