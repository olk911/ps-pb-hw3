def plural_form(number, form1, form2, form3):
    f =''                # правильная форма для числа number
    date = str(number)   # преобразование в строку и следовательно в список []

    if int(date[-1]) == 1 and int(date[-2:]) != 11:
        f = form1
    if int(date[-1]) > 1 and int(date[-1]) < 5:
        f = form2
    if int(date[-1]) == 0 or (int(date[-1]) > 4 and int(date[-1]) <= 9):
        f = form3
    return date + ' ' + f

print(plural_form(1, 'form1', 'form2', 'form3'))  
print(plural_form(105, 'студент', 'студента', 'студентов'))  
print(plural_form(39, 'яблоко', 'яблока', 'яблок'))              