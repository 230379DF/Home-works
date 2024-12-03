calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    list_ = []
    list_.append(len(string))
    a = string.upper()
    list_.append(a)
    b = string.lower()
    list_.append(b)
    tuple_ = tuple(list_)
    return tuple_

def is_contains(string, list_to_search):
    count_calls()
    a = string.lower()
    b = str(list_to_search).lower()
    if a in b:
        print(True)
    else:
        print(False)

print(string_info('Авокадо'))
print(string_info('Экзаменатор'))
is_contains('око', ['ЯбЛоНя', 'оКНо', 'ЯБЛОКО'])
is_contains('ГраД', ['ГаРдА', 'гРоЗа', 'ДУЭЛЬ'])
print(calls)

