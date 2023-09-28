scores = input().split()
lives = 3
final_score = 0
for score in scores:
    lives -= score == "I"
    final_score += score == "C"
    if lives <= 0:
        print("Game over")
        break
else:
    print("You won")
print(final_score)
