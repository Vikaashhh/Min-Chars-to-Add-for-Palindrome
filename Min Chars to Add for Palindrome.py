class Solution:
    def minChar(self, s):
        # Palindrome banane ke liye kitne characters front mein add karne padenge

        def computeLPS(str_):
            lps = [0] * len(str_)
            length = 0
            i = 1
            
            while i < len(str_):
                if str_[i] == str_[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        # Step 1: Reverse string
        rev = s[::-1]
        # Step 2: Combine original + special character + reverse
        combined = s + '#' + rev

        # Step 3: Create LPS array of combined string
        lps = computeLPS(combined)

        # Step 4: Minimum characters = total length - length of longest palindromic prefix
        return len(s) - lps[-1]
    

# ✅ Test the function with a sample input
if __name__ == "__main__":
    obj = Solution()
    s = "abc"
    print("Minimum characters to add:", obj.minChar(s))  # Output: 2