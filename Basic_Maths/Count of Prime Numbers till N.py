class Solution:
    # Function to find whether the
    # number is prime or not
    def isPrime(self, n):
        
        # Variable to store the 
        # count of divisors of n
        count = 0
        
        # Loop from 1 to n
        for i in range(1, n + 1):
            
            # Check if i is a divisor
            if n % i == 0:
                # Increment count
                count = count + 1
        
        # If count is 2, n is prime
        if count == 2:
            return True
        # Else not prime
        return False
    
    # Function to find count
    # of primes till n
    def primeUptoN(self, n):
        
        # Variable to store count
        count = 0
        
        # Iterate from 2 to n
        for i in range(2, n + 1):
            
            # Check if i is prime
            if self.isPrime(i):
                count += 1
        
        # Return the count
        return count

# Input number
n = 6

# Creating an instance of Solution class
sol = Solution()

# Function call to get count of all primes till n
ans = sol.primeUptoN(n)

print("The count of primes till", n, "is:", ans)


import math

class Solution:
    # Function to find whether 
    # the number is prime or not
    def isPrime(self, n):
        # Variable to store the count 
        # of divisors of n
        count = 0
        
        # Loop from 1 to square root of n
        for i in range(1, int(math.sqrt(n)) + 1):
            # Check if i is a divisor
            if n % i == 0:
                # Increment count
                count += 1
                
                # Check if counterpart divisor is 
                # different from original divisor
                if n // i != i:
                    # Increment count
                    count += 1
        
        # If count is 2, n is prime
        return count == 2
    
    # Function to find count of primes till n
    def primeUptoN(self, n):
        # Variable to store count
        count = 0
        
        # Iterate from 2 to n
        for i in range(2, n + 1):
            # Check if i is prime
            if self.isPrime(i):
                count += 1
        
        # Return the count
        return count

if __name__ == "__main__":
    n = 6
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to get count of all primes till n
    ans = sol.primeUptoN(n)
    
    print(f"The count of primes till {n} is: {ans}")
