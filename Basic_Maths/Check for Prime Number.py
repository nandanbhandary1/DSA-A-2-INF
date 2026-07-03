class Solution:
    # Function to find whether the
    # number is prime or not
    def isPrime(self, n):
        # Edge case
        if n < 2:
            return False

        # Loop from 2 to n-1
        for i in range(2, n):

            # Check if i is a divisor
            if n % i == 0:
                return False

        # Return true as the number is prime
        return True

if __name__ == "__main__":
    n = 5

    # Creating an instance of 
    # Solution class
    sol = Solution()

    # Function call to find whether the
    # given number is prime or not
    ans = sol.isPrime(n)

    if ans:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")
