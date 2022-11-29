"""_summary_
"""
input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
if score == dealer_score:
    return "push"
elif score > dealer_score and score > 21:
    return "You lose!"
elif score > dealer_score and score < 22:
    return "You win!"
elif score < dealer_score and dealer_score < 22:
    return "You lose!"
elif score < dealer_score and dealer_score > 21:
    return "You win!"