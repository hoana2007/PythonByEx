def range_prime(n):
    numbers = [True] * n
    numbers[0] = False
    numbers[1] = False
    for i in range(2, int(n**(1/2))):
        k = i * 2 # Đánh dấu bội số của i
        while k < n:
            numbers[k] = False
            k = k + i

    primes = [i for i in range(2, n) if numbers[i]]
    return primes

n = 19
print(range_prime(n))