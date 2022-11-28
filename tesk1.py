#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:

#- 6782 -> 23
#- 0,56 -> 11
print ('Введите любое вещественное число')
a = float(input())
c = 1
count = 0
n = 1
i = 2
j = 0
sum = 0
while a > 1:
    if a < 10*c:
        while count < n:
            a = a/10
            count +=1
    else:
        c *= 10
        n +=1
a = f'{a:g}'
b = str(a)
list = [0] * (len(b)-2)
while j < len(b)-2:
    list[j] = int(b[i])
    i +=1
    j +=1
i = 0
while i < len(list):
    sum = sum + list[i]
    i +=1
print ('Сумма цифр числа равна:')
print (sum)