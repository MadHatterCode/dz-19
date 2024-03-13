import string
def is_palindrome(text):
    s = "".join(letter for letter in text if letter not in string.punctuation).replace(" ", '')
    return s[::-1].lower() == s.lower()

assert is_palindrome('A man, a plan, a canal: Panama') == True
assert is_palindrome('0P') == False
assert is_palindrome('a.') == True
assert is_palindrome('aurora') == False
print("ОК")