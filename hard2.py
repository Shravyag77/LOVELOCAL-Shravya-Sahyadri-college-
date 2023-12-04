def shortest_palindrome(s):
    def build_lps(pattern):
        lps = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            lps[i] = j
        return lps

    if not s:
        return ""

    reversed_s = s[::-1]
    combined = s + "#" + reversed_s
    lps = build_lps(combined)

    # Length of the longest palindrome prefix in the combined string
    len_palindrome_prefix = lps[-1]

    # Add the reverse of the remaining substring to the beginning of the original string
    return reversed_s[:len(s) - len_palindrome_prefix] + s

# Take input from the user
s = input("Enter a string: ")
result = shortest_palindrome(s)
print("Shortest palindrome:", result)
