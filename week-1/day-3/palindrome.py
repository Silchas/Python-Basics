def is_palindrome(s):
    return s == s[::-1]

words = []

with open('words.txt', 'r') as file:
    for line in file:
        word = line.strip()
        if is_palindrome(word):
            print(f"{word} is a palindrome")