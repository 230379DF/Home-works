calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    a = string.upper()
    b = string.lower()
    tuple_ = (len(string), a, b)
    return tuple_

def is_contains(string, list_to_search):
    count_calls()
    for x in list_to_search:
        list_to_search.remove(x)
        list_to_search.insert(0, x.lower())
        if string.lower() in list_to_search:
            print(string.lower() in list_to_search)
            break
    else: print(False)

print(string_info('Авокадо'))
print(string_info('Экзаменатор'))
is_contains('окно', ['ЯбЛоНя', 'оКНо', 'ЯБЛОКО'])
is_contains('ГраД', ['ГаРдА', 'гРоЗа', 'ДУЭЛЬ'])
print(calls)
