def is_prime(n):
    if n % 2 == 0:  # if the number is even, then it is not prime
        return False
    for i in range(2, int(pow(n, 0.5))+1):
        # the square root of number needs less calculation time
        if n % i == 0:
            return False
    return True


for i in range(1, 100):
    if is_prime(i):
        print(i)
