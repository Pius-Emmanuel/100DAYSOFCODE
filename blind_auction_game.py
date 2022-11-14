"""
Secret auction
"""
from  os import system
from blind_auction_game_ASCII import LOGO
print(LOGO)

bids = {}
BIDDING_FINISHED = False

def find_highest_bidder(bidding_record):
    """_summary_

    Args:
        bidding_record (_type_): _description_
    """
    highest_bid = 0
    winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not BIDDING_FINISHED:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        BIDDING_FINISHED = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        system('clear')