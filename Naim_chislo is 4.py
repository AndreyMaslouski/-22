a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a<=b and a<=c and a<=d:
    print(a)
if b<a and b<=c and b<=d:
    print(b)
if c<a and c<b and c<=d:
    print(c)
if d<a and d<b and d<c:
    print(d)