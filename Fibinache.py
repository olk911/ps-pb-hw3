fibinache = []       # Наша пустая Фибиначи
fibinache_1 = []     # Пустая - с четными элементами
fibinache_2 = []     # Пустая - с нечетными элементами   
i = 0                # Счетчик элементов для формирования заданной Фибиначи
j = 0                # Счетчик элементов для формирования четной/нечетной Фибиначи
f = True             # Ключ завершения (False) формирования заданной последовательности Фибиначи
sum_fibinache_1 = 0  # Сумарное значение четных элементов Фибиначи
sum_fibinache_2 = 0  # Сумарное значение не четных элементов Фибиначи
while f:
    if i < 2:
        fibinache.append(1)
        #i += 1
    elif (fibinache[i-1] + fibinache[i-2]) <= 10000000:
        fibinache.append(fibinache[i-1] + fibinache[i-2])
        #i += 1
    else:
        f = False    
    i += 1

while j < len(fibinache):
    if fibinache[j] % 2 == 0:
        fibinache_1.append(fibinache[j])
    else:
        fibinache_2.append(fibinache[j])
    j += 1

for k in fibinache_1:
    sum_fibinache_1 += k
for l in fibinache_2:
    sum_fibinache_2 += l

print(f'Все элементы заданной Фибиначи {fibinache}')  
print(f'Общее количество элементов заданной Фибиначи {len(fibinache)}') 
print(f'Предпоследний элемент заданной последовательности {fibinache[-2]}')
print(f'Четные элементы заданной Фибиначи: {fibinache_1}') 
print(f'Нечетные элементы заданной Фибиначи: {fibinache_2}')  
print(f'Сумма четных элементов заданной Фибиначи: {sum_fibinache_1}')    
print(f'Сумма нечетных элементов заданной Фибиначи: {sum_fibinache_2}')