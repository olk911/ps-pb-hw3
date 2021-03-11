# Ввод начала начала и конца для диапазона чисел FizzBuzz:
fizzbuzz1 = input('Введите целое число начала диапазона FizzBuzz: ')
fizzbuzz2 = input('Введите целое число конца диапазона FizzBuzz: ')

# Определение ключей для Fizz (x) и Buzz (y):
x = ''
y = ''

if fizzbuzz1.isdigit() and fizzbuzz2.isdigit():  # Проверка на число
    k = int(fizzbuzz1)                           # Счетчик чисел
    #sum = int(fizzbuzz1)                         # Сумма чисел FizzBuzz
    sum = 0
    while k <= int(fizzbuzz2):
        if k % 3 == 0:
            x = 'Fizz'
        if k % 5 == 0:
            y = 'Buzz'
        if x or y :
            sum += k           
            x = ''
            y = ''
        k += 1 
    print(f'Сумму чисел из диапазона от {fizzbuzz1} до {fizzbuzz2} включительно, которые делятся и на 3 и на 5 = {str(sum)}')    
    print(k)
else:
    print('Вы ввели не число!')         
