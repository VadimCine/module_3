
#Задача № 1
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(2)
print_params(5, 'Новая строка', False)
print_params(b = 25)
print_params(c = [1,2,3])

#Задача № 2
values_list = [1, 'Месяц', True]
values_dict = {'a': 1, 'b':'строка', 'c': True}

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(*values_list)
print_params(**values_dict)


#Задача № 3
values_list_2 = [54.32, 'Строка' ]

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(*values_list_2)