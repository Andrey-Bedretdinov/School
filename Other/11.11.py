# Задача 1
print ('Задача 1')
print ('Введите число')
n = int(input())
n = print(int(str(int(n*3))*2)**2)

print('')

# Задача 2
print ('Задача 2')
print ('Введите число A')
a2a1a0 = int(input())
print ('Введите число B')
b2b1b0 = int(input())
a0 = str(a2a1a0 % 10)     #Распишем цифры числа A
a1 = str(a2a1a0 // 10 % 10)
a2 = str(a2a1a0 // 100)
b0 = str(b2b1b0 % 10)     #Распишем цифры числа B
b1 = str(b2b1b0 // 10 % 10)
b2 = str(b2b1b0 // 100)
print ('a2b1a0 =', a2+b1+a0)
print ('b2a1b0 = ', b2+a1+b0)