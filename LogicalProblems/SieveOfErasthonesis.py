def findAllPrimes(n):
    primes = [True for i in range(n+1)]
    primes[0],primes[1] = False, False
    p = 2
    while p*p<=n:
        if primes[p]==True:
            for i in range(p*p, n+1,p):
                primes[i] = False
        p+=1
    trueprimes = []
    for i in range(n+1):
        if primes[i]:
            trueprimes.append(i)
    return trueprimes

print((findAllPrimes(1000000)[0]))