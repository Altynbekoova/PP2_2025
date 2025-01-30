def filter_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = list(map(int, input().split()))

prime_numbers = []

for num in numbers:
    if filter_prime(num):
        prime_numbers.append(num)
        
print(prime_numbers)