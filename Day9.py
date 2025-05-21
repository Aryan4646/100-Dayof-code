import art
print(art.logo)

def highest(dict_auction):
    highest = 0
    highestbider = None
    for i in dict_auction:
        if dict_auction[i] > highest:
            highest = dict_auction[i]
            highestbider = i
    return highestbider,highest
print("Welcome to Secret Auction !")
dict_auction = {}
name = input("What is your name?:\n")
bid = float(input("What is your bid?:\n$"))
dict_auction[name] = bid
bidding = True
while bidding:
    bidder = input("Are there any other bidders? Type 'yes' or 'no':\n").casefold()
    if bidder == "yes":
        print("\n"* 100)
        name = input("What is your name?:\n")
        bid = float(input("What is your bid?:\n$"))
        dict_auction[name] = bid
    elif bidder == "no":
        bidding = False
    else:
        print("\nInvalid input for bidders.")
        break
highestbider, highest  = highest(dict_auction)
print(f"The highest bidder is {highestbider} with bid of ${highest}")

