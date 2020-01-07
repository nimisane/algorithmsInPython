n=int(input("Enter length of the list:"))
a=[]
for i in range (0,n):
    n1=int(input("Enter Elemet:"))
    a.append(n1)

for i in range(1,n):
    key=a[i]
    hole=i
    while(hole>0 and a[hole-1]>key):
        a[hole]=a[hole-1]
        hole=hole-1
    a[hole]=key
        
print(a)
