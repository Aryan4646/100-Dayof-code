import random
import sample_data

winning = True
Win = 0
# Run till winning
d1 = random.choice(sample_data.data)
while winning:
# Collect two different data set from list
    d2 = random.choice(sample_data.data)
    while d2 == d1:
        d2 = random.choice(sample_data.data)
# Compare those data set
    print(f"\nCompare A: {d1['name']}, a {d1['description']}, from {d1['country']}.")
    print("VS")
    print(f"Compare B: {d2['name']}, a {d2['description']}, from {d2['country']}.")
    comparison = input("Which one has more followers: 'A' or 'B': ").lower()
    if comparison == "a":
        if d1["follower_count"] > d2["follower_count"]:
            Win += 1
            d1 = d2
            print(f"You won your new score: {Win}")
        elif d2["follower_count"] > d1["follower_count"]:
            winning = False
    elif comparison == "b":
        if d2["follower_count"] > d1["follower_count"]:
            Win += 1
            d1 = d2
            print(f"You won your new score: {Win}")
        elif d1["follower_count"] > d2["follower_count"]:
            winning = False
else:
    print(f"Sorry that's wrong, your score was {Win}")
