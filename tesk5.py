#Реализуйте алгоритм перемешивания списка.

a = []
with open('file5.txt', 'r') as f:  #Решила попробовать применить метод 
    a = f.read().split('\n')       #с txt файлом и в этой задаче :)
print ('Исходный список:')
print (a)
import random
random.shuffle(a)
print ('Перемешанный список:')
print(a)