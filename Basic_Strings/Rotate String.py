class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
   # Strings must be same length to be rotations of each other
        if len(s) != len(goal):
            return False  
        # Try all possible rotations of s
        for i in range(len(s)):
            rotated = s[i:] + s[:i]  # Create a new rotation
            if rotated == goal:
                return True  
        return False  

# Test cases
sol = Solution()
print(sol.rotateString("abcde", "cdeab"))  # Output: True
print(sol.rotateString("abcde", "abced"))  # Output: False


class Solution:
# Strings must be of the same length to be rotations of each other
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False  
        doubled_s = s + s  # Concatenate s with itself
        return goal in doubled_s  # Check if goal is a substring of s + s

# Test cases
sol = Solution()
print(sol.rotateString("abcde", "cdeab")) 
print(sol.rotateString("abcde", "abced")) 
