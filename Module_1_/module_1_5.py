immutable_var = (1,2,3,4,False,'Banana',33.5)
print(immutable_var)
#immutable_var[3] = 99
# 'tuple' object does not support item assignment - Кортеж относится к неизменяемым типам данных и
# не поддерживает операции замены своих элементов на инные объекты, о чем и сообщает выскочившая ошибка.
mutable_list = [1,2,3,4,False,'Banana',33.5]
print(mutable_list)
mutable_list[4] = 99
mutable_list.append(True)
mutable_list.extend('Groza')
mutable_list.remove('Banana')
print(mutable_list)


