# Michael O'Regan
# 25.07.2018

# to see if a word is a palindrome

def isapalendrome(s):
    ans = True

    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            ans = False
    return ans  

print(isapalendrome("radar"))
print(isapalendrome("radars"))