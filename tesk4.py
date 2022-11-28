#4'. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.(для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
#-2 -1 0 1 2
#Позиции: 0,1 -> 2

print ('Введите число N:')
n = int(input())
a = []
with open('file4.txt', 'r') as f:
    a = f.read().split('\n')
index = [int(x) for x in a]
numbers = range(-n, n+1)
i = 0
product = 1
while i < len(index):
     product = product * numbers[index[i]]
     i += 1
print (product)