# Я сразу же покаюсь, решение не является полностью моим собственным. При поиске возможностей и методов работы
# с функцией isinstance(), я наткнулся на уже готовую конструкцию с ее использованием. В сравнении с тем, что я изначально
# хотел написать она в разы более компактна и менее громоздка, поэтому использовал именно её с небольшими правками.

def calculate_structure_sum(*data_str):
    summ = 0
    data_str = data_str[0]
    if isinstance(data_str, int):
        summ += data_str
    if isinstance(data_str, str):
        summ += len(data_str)
    if isinstance(data_str, (list, tuple, set)):
        for x in data_str:
            summ += calculate_structure_sum(x)
    if isinstance(data_str, dict):
        for key, value in data_str.items():
            summ += calculate_structure_sum(key)
            summ += calculate_structure_sum(value)

    return summ

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)