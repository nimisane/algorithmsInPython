def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		gcd, x, y = egcd(b % a, a)
		return (gcd, y - (b//a) * x, x)
a=30
b=50
gcd, x, y = egcd(a, b)
print("gcd(",a,",",b,")=",gcd)
print("Extended version:- gcd(a,b) = ax+by")
print(gcd,"=",a,"(",x,")","+",b,"(",y,")")
print("x=",x,"y=",y)