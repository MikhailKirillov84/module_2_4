numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes =[]
not_primes = []

for num in numbers:
    is_prime = True
    if num / 1 - 1:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
        if is_prime:
            primes.append(num)
        else:
            not_primes.append(num)
print('Primes:', primes)
print('Not_Primes:', not_primes)

#Primes: [2, 3, 5, 7, 11, 13]
#Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]