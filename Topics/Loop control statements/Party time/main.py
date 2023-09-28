names = []
counter = 0
while True:
    name = input()
    if name == '.':
        break
    else:
        names.append(name)
        counter += 1
print(names)
print(counter)
