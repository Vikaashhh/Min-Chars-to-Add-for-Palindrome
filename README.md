# Day 19 - Min Chars to Add for Palindrome

## Problem Statement

The task is to determine the minimum number of characters that need to be added at the front of the string in order to make it a palindrome. A palindrome is a string that reads the same forward and backward.

## Approach

The approach utilizes the concept of **Longest Prefix Suffix (LPS)** from the **Knuth-Morris-Pratt (KMP)** string matching algorithm. The solution works by:

1. Reversing the string.
2. Combining the original string with its reverse using a special delimiter.
3. Computing the LPS array for the combined string.
4. Using the LPS value to determine how many characters need to be added to the front to make the string a palindrome.

### Detailed Steps:

1. **Reverse the string**: First, we reverse the given string.
2. **Combine original and reversed strings**: We concatenate the original string with a special character (e.g., `#`) and then the reversed string. This helps avoid overlaps in the LPS calculation.
3. **Compute the LPS array**: The LPS array will help us find the longest palindromic prefix of the string.
4. **Find the minimum characters to add**: Using the LPS array, the length of the longest palindromic prefix is determined. The minimum characters to be added to the front is the difference between the length of the original string and the length of the longest palindromic prefix.

### Time Complexity:
- The time complexity of the algorithm is **O(n)**, where `n` is the length of the input string.

## 📌 Hashtags:
#Day19 #gfg160 #geekstreak2025 #kmpalgorithm #palindrome #stringmanipulation #dsa #interviewprep #pythondeveloper #dsawithvikash #dsasimplified

