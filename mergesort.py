a=[13,0,4,65,3,2]
print("Unsoerted list",a)
def merge(a):
    if len(a)>1:
        mid=len(a)//2
        n=len(a)
        l=[]
        r=[]
        i=0
        while(i<=mid-1):
            l.append(a[i])
            i=i+1
        i=mid
        while(i<=n-1):
            r.append(a[i])
            i=i+1
        merge(l)
        merge(r)
        i=0
        j=0
        k=0
        while(i<len(l) and j<len(r)):
            if (l[i]<=r[j]):
                a[k]=l[i]
                i=i+1
            else:
                a[k]=r[j]
                j=j+1
            k=k+1
        while(i<len(l)):
            a[k]=l[i]
            i=i+1
            k=k+1
        while(j<len(r)):
            a[k]=r[j]
            j=j+1
            k=k+1
merge(a)
print("Soerted list",a)
        
