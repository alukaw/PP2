def is_palindrome(s):
    return s == s[::-1]

string = "radar"
print("Palindrome:", is_palindrome(string))

string = "hello"
print("Palindrome:", is_palindrome(string))
