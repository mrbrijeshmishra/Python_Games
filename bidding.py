bid_logo = """
                         ___________
                                  /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'''---------'' '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\
"""

print(bid_logo,"\n\n")

bids = dict({})

continue_bid = True

def high_bid(bid_dict):
    high_bid = 0
    winner = ""

    max_bid = max(bid_dict)

    for bidder in bid_dict:
        bid_amount = bid_dict[bidder]
        if bid_amount > high_bid:
            high_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with price of Rs. {bid_dict[winner]}")


while continue_bid:
    name = input("Enter your name?: ")
    price = int(input("Enter your bid price?: Rs."))
    bids[name] = price
    proceed = input("Does anyone else want to bid? Type 'yes' or 'no'. \n")

    if proceed.lower() == 'yes':
        continue_bid = True
        print("\n"*20)
    elif proceed.lower() == 'yes':
        continue_bid = False
        high_bid(bids)
    else:
        print("Sorry wrong input!!!!!! Try again from beginning please.")
        continue_bid = False


