import random
friends = ["John", "Emily", "Michael", "Sarah", "David"]

# en = len(friends)-1
# ran = random.randint(0, en)
# print(f"The person who will pay today bill is: {friends[ran]}")

print(f"The person who will pay today bill is: {random.choice(friends)}")