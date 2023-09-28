for char in input():
    if char in 'aeiou':
        print('vowel')
    elif char.islower():
        print('consonant')
    else:
        break
