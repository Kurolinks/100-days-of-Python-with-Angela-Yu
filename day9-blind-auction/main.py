from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

bidders = {}
bidding_on = True
highest_bid = 0
person = ""

#Function to get highest bid and print it
def bidding_list(bidders_list):
  for bid in bidders:
    current_bid = bidders[bid]
    global highest_bid
    if highest_bid > current_bid:
      highest_bid = highest_bid
      person = bid
    else:
      highest_bid = current_bid
      person = (bid)
  print(f"The winner is {person} with a bid of ${highest_bid}.")

#Check if there are other bidders and loop the process
while bidding_on:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  bidders[name] = bid
  more_bidders = input("Are there any other bidders? 'yes' or 'no': \n")
  if more_bidders == ("yes"):
    clear()
    bidding_on = True
  elif more_bidders == ("no"):
    bidding_on = False
    bidding_list(bidders)
