# a="abcedfg"
# b="bacg"
a=""
b=""

def lcs(xstr, ystr):
    if not xstr or not ystr:
        return ""
    x, xs, y, ys = xstr[0], xstr[1:], ystr[0], ystr[1:]
    if x == y:
        return x + lcs(xs, ys)
    else:
        return max(lcs(xstr, ys), lcs(xs, ystr), key=len)

print("Longest Common Subsequence is",lcs(a,b)+" and its length is ",len(lcs(a,b)))