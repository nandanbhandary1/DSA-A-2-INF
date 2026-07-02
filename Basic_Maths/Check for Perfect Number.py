class Solution:
    # Function to find whether the
    # number is perfect or not
    def isPerfect(self, n):
        
        # Variable to store the sum
        # of all proper divisors
        sum = 0
        
        # Loop from 1 to n
        for i in range(1, n):
            
            # Check if i is a proper divisor
            if n % i == 0:
                # Update sum
                sum = sum + i
        
        # Compare sum and n
        return sum == n

# Input number
n = 6

# Creating an instance of Solution class
sol = Solution()

# Function call to find whether the given number is perfect or not
ans = sol.isPerfect(n)

if ans:
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")



import math

class Solution:
    # Function to find whether the 
    # number is perfect or not
    def isPerfect(self, n):
        # Edge case
        if n == 1: 
            return False
        # Variable to store the sum of all proper divisors
        sum = 0
        
        # Loop from 1 to square root of n
        for i in range(1, int(math.sqrt(n)) + 1):
            
            # Check if i is a proper divisor
            if n % i == 0:
                # Update sum
                sum = sum + i
                
                # Add the counterpart divisor if it's 
                # different from i and if it is not n itself
                if n // i != n and i != n // i:
                    sum = sum + (n // i)
        
        # Compare sum and n
        if sum == n:
            return True
        return False

if __name__ == "__main__":
    n = 6
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to find whether the given number is perfect or not
    ans = sol.isPerfect(n)
    
    if ans:
        print(f"{n} is a perfect number.")
    else:
        print(f"{n} is not a perfect number.")
