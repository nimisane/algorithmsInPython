from random import randint,shuffle
def create_array(size=10,max=50):
    return [randint(0,max) for _ in range(size)]

def is_sorted(a):
    for i in range(1,len(a)):
        if a[i]<a[i-1]:
            return False
    return True

def bogo_sort(a):
    ctr=0
    while not is_sorted(a):
        shuffle(a)
        print(a)
        ctr+=1
    return ctr,a

a=create_array(5,5)
print("unsorted array:",a)
c,s=bogo_sort(a)
print("Sorted Array:",s)
print(c)
