def print_pararms (a = 1, b = 'string', c = True):
    print(a,b,c)

values_list = ['Vova', False, 32]
values_dict = {'a' : 2435, 'b' : 'Forgoten_Name', 'c' : False}
print_pararms(*values_list)
print_pararms(**values_dict)
values_list_2 = [21, '13 chests']
print_pararms(*values_list_2, 49)