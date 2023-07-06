def count_vowels(v):
    vowels = 'aeiouAEIOU'
    count = 0
    for characters in v:
        if characters in vowels:
            count += 1
    return count

print(count_vowels('aeiou'))
