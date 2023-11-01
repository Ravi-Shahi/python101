N = int(input ('Enter your Number'))

def isPrime(num):
    if num> 1:
        for i in range(2,int(num/2)+1): 
            if num%i == 0:
                return False
        else:
            return True
        
prime_numbers = []
 
for i in range(N):
    if isPrime(i):
        prime_numbers.append(i)
    
print(prime_numbers)