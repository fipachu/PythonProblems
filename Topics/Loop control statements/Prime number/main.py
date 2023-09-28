a = int(input())
count = 0

for x in range(1, a + 1):
    if a % x == 0:
        count += 1
    if count > 2:
        break

print("This number is prime" if count == 2 else
      "This number is not prime")
