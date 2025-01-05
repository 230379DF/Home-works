number_1 = input()
number_2 = input()
number_3 = input()
if number_1 == number_2 and number_1 == number_3 and number_2 == number_3:
    print('3')
elif number_1 == number_2 or number_1 == number_3:
    print('2')
elif number_2 == number_3 or number_2 == number_1:
    print('2')
elif number_3 == number_1 or number_3 == number_2:
    print('2')
else: print('0')
#elif number_1 != number_2 and number_1 != number_3 and number_2 != number_3:
#    print('0')
