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
