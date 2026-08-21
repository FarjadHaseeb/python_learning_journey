limit = int(input("Find primes up to: "))

for n in range(2, limit + 1):
    is_prime = True
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(n, end=" ")
print()
