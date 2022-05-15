#   x = 10
#  def my_func(a,b):
#    print(x)
#    print(z)

# my_func(1,2)

# def my_func(a,b):
#    global c
#    b,a=a,b
#    d='Mike'
#    print(a,b,c,d)

# a,b,c,d = 1,2,'c is global',4
# my_func(1,2)
# print(a,b,c,d)

def counter():
    num=0
    def incrementer():
        nonlocal num
        num +=1
        return num
    return incrementer
c = counter()
print(c)
c()
