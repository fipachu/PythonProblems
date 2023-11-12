def check_name(name):
    if name in set('lOI'):
        print("Never use the characters 'l', 'O', or 'I' "
              "as single-character variable names")
    elif name.islower():
        print('It is a common variable')
    elif name.isupper():
        print('It is a constant')
    else:
        print("You shouldn't use mixedCase")


def test():
    check_name('l')
    check_name('a')
    check_name('A')
    check_name('lOI')
