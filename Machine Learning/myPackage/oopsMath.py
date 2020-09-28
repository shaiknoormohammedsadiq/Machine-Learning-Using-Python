class Math:
    """
     in this Math class i created few mathmatical functions,
     those are isEven() and isOdd()
    """
    def isPrime(n):
        for i in range(2,n):
            if n%i==0:
                return False
        return True