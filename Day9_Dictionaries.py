logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

def highest_bidders(biding_record):
    highest_amount = 0
    winner = ""
    for bidder in biding_record:
        bid_amount = biding_record[bidder]
        if bid_amount > highest_amount:
            highest_amount = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_amount}")




bids = {}

continue_bidding = False
while not continue_bidding:
    name = input("What's your name: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    others = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    if others == 'no':
        continue_bidding = True
        highest_bidders(bids)

    elif others == 'yes':
        print("\n" * 20)





