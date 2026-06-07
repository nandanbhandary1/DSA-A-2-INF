class Solution:
    
    # Function to print pattern1
    def pattern1(self, n):
        
        # Outer loop will run for rows.
        for i in range(n):
            
            # Inner loop will run for columns.
            for j in range(n):
                print("*", end="")
                
            """ As soon as N stars are printed, move
            to the next row and give a line break."""
            print()

    def main(self):
        N = 4

        # Create an instance of the Solution class
        sol = Solution()

        sol.pattern1(N)

if __name__ == "__main__":
    Solution().main()



class Solution:
    
    # Function to print pattern2
    def pattern2(self, n):
        
        # Outer loop will run for rows.
        for i in range(n):
            
            # Inner loop will run for columns.
            for j in range(i+1):
                print("*", end="")
                
            """ As soon as n stars are printed, move
            to the next row and give a line break."""
            print()

    def main(self):
        N = 5

        # Create an instance of the Solution class
        sol = Solution()

        sol.pattern2(N)

if __name__ == "__main__":
    Solution().main()



class Solution:
    
    # Function to print pattern3
    def pattern3(self, n):
        
        # Outer loop will run for rows.
        for i in range(1,n+1):
            
            # Inner loop will run for columns.
            for j in range(1,i+1):
                print(j, end="")
                
            """ As soon as n stars are printed, move
            to the next row and give a line break."""
            print()

    def main(self):
        N = 5

        # Create an instance of the Solution class
        sol = Solution()

        sol.pattern3(N)

if __name__ == "__main__":
    Solution().main()


class Solution:
    
    # Function to print pattern4
    def pattern4(self, n):
        
        # Outer loop will run for rows.
        for i in range(1,n+1):
            
            # Inner loop will run for columns.
            for j in range(1,i+1):
                print(i, end="")
                
            """ As soon as n stars are printed, move
            to the next row and give a line break."""
            print()

    def main(self):
        N = 5

        # Create an instance of the Solution class
        sol = Solution()

        sol.pattern4(N)

if __name__ == "__main__":
    Solution().main()


class Solution:
    
    # Function to print pattern5
    def pattern5(self, n):
        
        # Outer loop will run for rows.
        for i in range(0,n):
            
            # Inner loop will run for columns.
            for j in range(0,n-i):
                print("*", end="")
                
            """ As soon as n stars are printed, move
            to the next row and give a line break."""
            print()

    def main(self):
        N = 5

        # Create an instance of the Solution class
        sol = Solution()

        sol.pattern5(N)

if __name__ == "__main__":
    Solution().main()


class Solution:
    
    # Function to print pattern6
    def pattern6(self, n):
        
        # Outer loop will run for rows.
        for i in range(0,n):
            
            # Inner loop will run for columns.
            for j in range(0,n-i):
                print(j+1, end="")
                
            """ As soon as n stars are printed, move
            to the next row and give a line break."""
            print()

    def main(self):
        N = 5

        # Create an instance of the Solution class
        sol = Solution()

        sol.pattern6(N)

if __name__ == "__main__":
    Solution().main()




class Solution:
    
    # Function to print pattern7
    def pattern7(self, n):
        
        # Outer loop will run for rows.
        for i in range(0,n):
            
            #This loop will print the spaces
            for j in range(0, (n-i-1)):
                print(" ",end="")
            
            # This loop will print asterisk.
            for j in range(0,2*i+1):
                print("*", end="")

            """ As soon as n stars are printed, move
            to the next row and give a line break."""
            print()

    def main(self):
        N = 5

        # Create an instance of the Solution class
        sol = Solution()

        sol.pattern7(N)

if __name__ == "__main__":
    Solution().main()


class Solution:
    
    # Function to print pattern8
    def pattern8(self, n):
        
        # Outer loop will run for rows.
        for i in range(0,n):
            
            #This loop will print the spaces
            for j in range(0, i):
                print(" ", end="")
            
            
            # This loop will print asterisk.
            for j in range(0, 2*n-(2*i+1)):
                print("*", end="")
                
            """ As soon as n stars are printed, move
            to the next row and give a line break."""
            print()

    def main(self):
        N = 5

        # Create an instance of the Solution class
        sol = Solution()

        sol.pattern8(N)

if __name__ == "__main__":
    Solution().main()


class Solution:
    def pattern9(self, n):
        self.erect_pyramid(n)
        self.inverted_pyramid(n)

    def erect_pyramid(self, n):
        # Outer loop which will loop for the rows.
        for i in range(n):
            # For printing the spaces before stars in each row
            for j in range(n - i - 1):
                print(" ", end="")

            # For printing the stars in each row
            for j in range(2 * i + 1):
                print("*", end="")

            # As soon as the stars for each iteration are printed,
            # we move to the next row and give a line break
            print()

    def inverted_pyramid(self, n):
        # Outer loop which will loop for the rows.
        for i in range(n):
            # For printing the spaces before stars in each row
            for j in range(i):
                print(" ", end="")

            # For printing the stars in each row
            for j in range(2 * n - (2 * i + 1)):
                print("*", end="")

            """ As soon as the stars for each iteration are printed,
            we move to the next row and give a line break"""
            print()

if __name__ == "__main__":
    N = 5

    # Create an instance of Solution class
    sol = Solution()

    sol.pattern9(N)


class Solution:
    #Function to print pattern10
    def pattern10(self, n):
        # Outer loop for number of rows.
        for i in range(1, 2 * n):
            
            """ stars would be equal to the
            row no. uptill first half"""
            stars = i if i <= n else 2 * n - i
            
            # for printing the stars in each row.
            for j in range(1, stars + 1):
                print("*", end="")
            
            """ As soon as the stars for each iteration are 
            printed, we move to the next row and give a line break"""
            print()

if __name__ == "__main__":
    N = 5
    
    # Create an instance of Solution class
    sol = Solution()
    
    sol.pattern10(N)
