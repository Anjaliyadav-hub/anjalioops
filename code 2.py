def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def primes_upto_n(n):
    """Generate all prime numbers up to n."""
    prime_list = []
    for i in range(2, n+1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list


def first_n_primes(n):
    """Generate the first n prime numbers."""
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


# --- Main Program ---
n = int(input("Enter a number n: "))

# a. Check if n is prime
if is_prime(n):
    print(f"\n{n} is a prime number.")
else:
    print(f"\n{n} is not a prime number.")

# b. Generate all primes up to n
print(f"\nAll prime numbers up to {n}:")
print(primes_upto_n(n))

# c. Generate first n prime numbers
print(f"\nThe first {n} prime numbers are:")
print(first_n_primes(n))