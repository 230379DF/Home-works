numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []
for i in  numbers[1:]:
    for j in numbers[1:]:
        if i / j > 1 and i / j == int(i / j):
            not_prime.append(i)
            break
        if i / j == 1:
            prime.append(i)
            break
print(prime)
print(not_prime)