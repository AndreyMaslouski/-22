# Напишите декоратор, который будет считать, сколько раз была вызвана декорируемая функция

import functools

def counter(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        wrapper.num +=1
        print(f'Вызов{func.__name__!r}: {wrapper.num}')
        val = func(*args,**kwargs)
        return val
    wrapper.num=0
    return wrapper

@counter
def say(name):
    return f'Привет {name}!'

print(say('Андрей'))
print(say('Михаил'))
print(say('Рита'))
print(say('Ира'))


