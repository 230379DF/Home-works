my_dict = {'Vodyanchicus' : 'Gvr-msEN95', 'Masha' : 1967, 'Оранжевое яблоко' : False}
print(my_dict)
print(my_dict.get('Оранжевое яблоко'))
print(my_dict.get('Sasha'))
my_dict.update({'Vasya' : '9Q-YuuHIOt', 'Lana' : 2003})
password_ = my_dict.pop('Vodyanchicus')
print(password_)
print(my_dict)

my_set = {2,2,3,3,4,4,'false','false',True,True,}
print(my_set)
my_set.add((5, False, 5.17))
my_set.remove(1)
print(my_set)
