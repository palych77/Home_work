#Задача 4 HARD Напишите простой калькулятор, который считывает с пользовательского ввода три строки: 
#первое число, второе число и операцию, после чего применяет операцию к введённым числам 
#("первое число" "операция" "второе число") 
#и выводит результат на экран.

#Поддерживаемые операции: +, -, /, *, mod, pow, div, где
#mod — это взятие остатка от деления,
#pow — возведение в степень,
#div — целочисленное деление.

#Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
#Обратите внимание, что на вход программе приходят вещественные числа.

def simpleCalculator(msg):
    if mathOpertaion == '+': msg = (number1+number2)
    elif mathOpertaion == '-': msg = (number1-number2)
    elif mathOpertaion == '*': msg = (number1*number2)
    elif mathOpertaion == 'pow': msg = (number1**number2)
    elif mathOpertaion == '/': msg = (number1/number2)
    elif mathOpertaion == 'mod': msg = (number1%number2)
    elif mathOpertaion == 'div': msg = (number1//number2)
    return msg
msg ='Деление на 0!'
try:
    number1 = float(input('Введите первое число: '))
    number2 = float(input('Введите второе число: '))
    mathOpertaion = input('Введите математическу операцию: ')
    msg = simpleCalculator(msg)
except ZeroDivisionError:
    pass
except:
    msg = 'Некорректный ввод'
finally:
    print(msg)