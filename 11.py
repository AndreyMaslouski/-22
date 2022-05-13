# 1. Если в функцию передаётся кортеж, то посчитать длину всех его слов.

# 2. Если список, то посчитать кол-во букв и чисел в нём.

# 3. Число – кол-во нечётных цифр.

# 4. Строка – количество букв.

# Сделать проверку со всеми этими случаями.

def func(p):
    if type(p) == tuple:
        print("Длина всех его слов= ",len(p))
    elif type(p) == list:
        print('Кол-во букв: ', len(list(filter(lambda x: type(x) == str, p))), 'Кол-во чисел:', len(list(filter(lambda x: type(x) in (int, float), p))))
    elif type(p) == int:
        even = 0
        odd = 0
        while p>0:
            if p%2 == 0:
                even +=1
            else:
                odd +=1
            p = p//10
        print("Количество нечетных цифр= ",odd)
    elif type(p) == str:
        print('Количество букв: ', len(p))


func(('hello','world','day','pay','money','box','football'))
func([10, 15, 16, 21, 'h', 's', 'e','k','g'])
func(5622445541222157885223)
func('dfggfdgdfgthrhdssfaAAQWDF')