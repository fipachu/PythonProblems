best = ["", 0]
while True:
    input_ = input().split()
    if input_ == ["MEOW"]:
        break
    cafe = [input_[0], int(input_[1])]
    if cafe[1] > best[1]:
        best = cafe
print(best[0])
