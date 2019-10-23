# Primes.py
# This is a simple module which generates prime numbers.

def prime_gen(n):
    """ This generates prime numbers using the sieve of Eratososthenes.
    Input: n: upper bound for prime numbers.
    """
    prime_list = []
    return_primes = []
    for i in range(2, n+1):
        if i not in prime_list:
            return_primes.append(i)
            for j in range(i*i, n+1, i):
                prime_list.append(j)
    return return_primes
