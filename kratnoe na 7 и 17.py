x = int(input())

if x>=1000 and x<10000:
    if x%7==0 or x%17==0:
        print("YES")
    else:
        print("NO")
if x<1000 or x>10000:
    print("NO")
