# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).

while True:
    d = float(input("Введите первое число: "))
    e = float(input("Введите второе число: "))
    choice = input("Какая операция Вас интересует(+,-,*,/): ")
    if choice =='+':
        def summa(a,b):
            c = (a+b)
            return a+b
        print(summa(d,e),"Сумма чисел")

    if choice =='-':
        def summa(a,b):
            c = (a-b)
            return a-b
        print(summa(d,e),"Разность чисел")

    if choice == '*':
        def summa(a,b):
            c = a*b
            return a*b
        print(summa(d,e),"Умножение чисел")

    if choice == '/':
        def summa(a,b):
            if b!=0:
                c = a/b
                return a/b
            if b ==0:
                print("Деление невозможно")
        print(summa(d, e), "Деление чисел")

        if e ==0:
            print("Программа завершена")
            break



