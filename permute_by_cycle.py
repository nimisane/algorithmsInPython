import math
def cyclic(N):
    num = N
    n = len(str(N))
    while (True):
        print(int(num))
        rem = num % 10
        div = (num // 10)
        #num = ((math.pow(10, n - 1)) *rem + div);
        num= (10**(n-1))*rem+div
        if (num == N):
            break
N = 12345
cyclic(N)