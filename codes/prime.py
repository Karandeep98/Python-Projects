def isPrime(n):
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            print('Not Prime')
            return
    print('Prime')


isPrime(int(input()))



