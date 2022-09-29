#Задача 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


def func1(x, y, z):
    a = not (x or y or z)
    b = not x and not y and not z
    return a == b 

for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
            print(func1(x , y, z))
