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


class Solution:
    # Function to print pattern11
    def pattern11(self, n):
        # First row starts by printing a single 1.
        start = 1

        # Outer loop for the no. of rows
        for i in range(n):

            # if the row index is even then 1
            # is printed first in that row.
            if i % 2 == 0:
                start = 1

            # if odd, then the first 0 
            # will be printed in that row
            else:
                start = 0

            # We alternatively print 1's and 0's 
            # in each row by using inner for loop
            for j in range(i + 1):
                print(start, end="")
                if j != i:
                    print(" ", end="")

                start = 1 - start

            # As soon as the numbers for each 
            # iteration are printed, we move to the
            # next row and give a line break
            print()


if __name__ == "__main__":
    N = 5

    # Create an instance of Solution class
    sol = Solution()

    sol.pattern11(N)
    
class Solution:
    # Function to print pattern12
    def pattern12(self, n):
        # Initial no. of spaces in row 1.
        spaces = 2 * (n - 1)

        # Outer loop for the number of rows.
        for i in range(1, n + 1):
            # For printing numbers in each row
            for j in range(1, i + 1):
                print(j, end="")

            # For printing spaces in each row
            for j in range(1, spaces + 1):
                print(" ", end="")

            # For printing numbers in each row
            for j in range(i, 0, -1):
                print(j, end="")

            """ As soon as the numbers for each iteration
            are printed, we move to the next row and give
            a line break otherwise all numbers would get 
            printed in 1 line"""
            print()

            """ After each iteration nos. increase by 
            2, thus spaces will decrement by 2"""
            spaces -= 2

if __name__ == "__main__":
    N = 5

    # Create an instance of Solution class
    sol = Solution()

    sol.pattern12(N)



class Solution:
    # Function to print pattern13
    def pattern13(self, n):
        # starting the number
        num = 1

        # Outer loop for the number of rows.
        for i in range(1, n + 1):
            
            """ Inner loop will loop for i times and
            print numbers increasing by 1 each time"""
            for j in range(1, i + 1):
                print(num, end=" ")
                num += 1
                
            """ As soon as the numbers for each iteration
            are printed, we move to the next row and give
            a line break otherwise all numbers would get
            printed in 1 line"""
            print()

if __name__ == "__main__":
    N = 5

    # Create an instance of Solution class
    sol = Solution()

    sol.pattern13(N)


class Solution:
    # Function to print pattern13
    def pattern13(self, n):
        # starting the number
        num = 1

        # Outer loop for the number of rows.
        for i in range(1, n + 1):
            
            """ Inner loop will loop for i times and
            print numbers increasing by 1 each time"""
            for j in range(1, i + 1):
                print(num, end=" ")
                num += 1
                
            """ As soon as the numbers for each iteration
            are printed, we move to the next row and give
            a line break otherwise all numbers would get
            printed in 1 line"""
            print()

if __name__ == "__main__":
    N = 5

    # Create an instance of Solution class
    sol = Solution()

    sol.pattern13(N)


class Solution:
    # Function to print pattern14
    def pattern14(self, n):
        # Outer loop for the number of rows.
        for i in range(n):
            
            """Inner loop will loop for i times and
            print alphabets from A to A + i."""
            for ch in range(ord('A'), ord('A') + i + 1):
                print(chr(ch), end="")
                
            """ As soon as the letters for each iteration 
            are printed, we move to the next row and give
            a line break otherwise all letters would get
            printed in 1 line."""
            print()

if __name__ == "__main__":
    N = 5

    # Create an instance of Solution class
    sol = Solution()

    sol.pattern14(N)


class Solution:
    # Function to print pattern15
    def pattern15(self, n):
        # Outer loop for the number of rows.
        for i in range(n):
            
            """Inner loop will loop for i times and
            print alphabets from A to A + (n - i - 1)."""
            for ch in range(ord('A'), ord('A') + n - i):
                print(chr(ch), end="")
                
            """As soon as the letters for each iteration
            are printed, we move to the next row and give
            a line break otherwise all letters would get
            printed in 1 line."""
            print()

if __name__ == "__main__":
    N = 5

    # Create an instance of Solution class
    sol = Solution()

    sol.pattern15(N)


class Solution:
    # Function to print pattern16
    def pattern16(self, n):
        # Outer loop for the number of rows.
        for i in range(n):
            
            # Defining character for each row.
            ch = chr(ord('A') + i)
            for j in range(i + 1):
                
                """same char is to be printed
                i times in that row."""
                print(ch, end="")
                
            """ As soon as the letters for each 
            iteration are printed, we move to the
            next row and give a line break otherwise
            all letters would get printed in 1 line. """
            print()

N = 5

# Create an instance of Solution class
sol = Solution()

sol.pattern16(N)


class Solution:
    # Function to print pattern17
    def pattern17(self, n):
        # Outer loop for the number of rows.
        for i in range(n):
            
            # Printing spaces before characters.
            for j in range(n - i - 1):
                print(" ", end="")
            
            # Printing characters.
            ch = 'A'
            breakpoint = (2 * i + 1) // 2
            for j in range(1, 2 * i + 2):
                print(ch, end="")
                if j <= breakpoint:
                    ch = chr(ord(ch) + 1)
                else:
                    ch = chr(ord(ch) - 1)
            
            # Move to the next line for the next row.
            print()

if __name__ == "__main__":
    N = 5
    
    #Create an instance of Solution class
    sol = Solution()
    
    sol.pattern17(N)

class Solution:
    # Function to print pattern18
    def pattern18(self, n):
        # Outer loop for the number of rows.
        for i in range(n):
            
            """ Inner loop for printing alphabets
            from 'A' + n - 1 - i to 'A' + n - 1."""
            for ch in range(ord('A') + n - 1 - i, ord('A') + n):
                print(chr(ch), end=" ")
            
            # Move to the next line for the next row.
            print()

if __name__ == "__main__":
    N = 5
    
    # Create an instance of Solution class
    sol = Solution()
    
    sol.pattern18(N)

class Solution:
    # Function to print pattern19
    def pattern19(self, n):
        # Print the upper half pattern
        
        # Store the initial spaces.
        iniS = 0
        
        for i in range(n):
            # Printing the stars in the row.
            print("*" * (n - i), end="")
            
            # Printing the spaces in the row.
            print(" " * iniS, end="")
            
            # Printing the stars in the row.
            print("*" * (n - i))
            
            """ The spaces increase by 2 
            every time we hit a new row."""
            iniS += 2
        
        # Print the lower half pattern
        
        # Store the initial spaces.
        iniS = 2 * n - 2
        
        for i in range(1, n + 1):
            # Printing the stars in the row.
            print("*" * i, end="")
            
            # Printing the spaces in the row.
            print(" " * iniS, end="")
            
            # Printing the stars in the row.
            print("*" * i)
            
            """ The spaces decrease by 2 
            every time we hit a new row."""
            iniS -= 2

if __name__ == "__main__":
    N = 5
    
    # Create an instance of Solution class
    sol = Solution()
    
    sol.pattern19(N)


class Solution:
    # Function to print pattern20
    def pattern20(self, n):
        # Initialising the spaces.
        spaces = 2 * n - 2
        
        # Outer loop to print the row.
        for i in range(1, 2 * n):
            # Stars for first half
            stars = i
            
            # Stars for the second half.
            if i > n:
                stars = 2 * n - i
            
            # For printing the stars
            print("*" * stars, end="")
            
            # For printing the spaces
            print(" " * spaces, end="")
            
            # For printing the stars
            print("*" * stars, end="")
            
            # Give a line break for new row.
            print()
            
            # Adjust spaces for the next row
            if i < n:
                spaces -= 2
            else:
                spaces += 2

# Main function
if __name__ == "__main__":
    N = 5
    
    # Create an instance of Solution class
    sol = Solution()
    
    sol.pattern20(N)

class Solution:
    # Function to print pattern21
    def pattern21(self, n):
        # Outer loop for the rows.
        for i in range(n):
            
            """ Inner loop for printing 
            the stars at borders only."""
            for j in range(n):
                
                if i == 0 or j == 0 or i == n-1 or j == n-1:
                    print("*", end="")
                else:
                    print(" ", end="")
                    
            # Move to the next row.
            print()

if __name__ == "__main__":
    N = 5
    
    # Create an instance of Solution class
    sol = Solution()
    
    sol.pattern21(N)
