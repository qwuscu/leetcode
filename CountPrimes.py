class Solution:
    """
    @param n: a integer
    @return: return a integer
    """
    def countPrimes(self, n: int) -> int:
    	if n < 2:
    		return 0
    	not_prime = [False] * n
    	res = 0
    	for i in range(2,n):
    		if not_prime[i] == False:
    			res += 1
    			for j in range(2, n):
    				if j * i >= n:
    					break
    				not_prime[j*i] == True
    	return res



class Solution:
    def countPrimes(self, n: int) -> int:
        # assue all number are primes
        isPrime = [True] * (n)
        res = 0
        for i in range(2,n):
            if isPrime[i]:
                res += 1
                # prime's multiples cannot be prime
                for j in range(i*2,n,i):
                    isPrime[j] = False
        return res


