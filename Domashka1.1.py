#Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день 
# выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет
def isHoliday(msg): 
        if nDay >= 0 and nDay <= 5:
            msg = 'нет'
        elif nDay == 6 or nDay == 7:
            msg = 'да'
        return msg

msg = 'Некорректный ввод \n Введите число от 1 до 7'
try:
    nDay=int(input('Введите число: '))
    msg = isHoliday(msg)
except:
    pass
finally: 
    print(msg)