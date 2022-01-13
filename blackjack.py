import random

def main():
  dealer_cards = []
  player_cards = []

  print(" ")

  while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
      print("Dealer has X & " + str(dealer_cards[1]))
      break

  while len(player_cards) != 2:
    player_cards.append(random.randint(1,11))
    if len(player_cards) == 2:
      print("You have " + str(player_cards[0]) + " & " + str(player_cards[1]))

  if sum(dealer_cards) == 21:
    print("Dealer has 21 and wins!")
  elif sum(dealer_cards) > 21:
    print("The dealer has busted!")

  while sum(player_cards) < 21:
    action_taken = str(input("Do you want to stay or hit? "))
    if action_taken == "hit":
        player_cards.append(random.randint(1,11))
        print("You have " + str(player_cards) + " for a total of " + str(sum(player_cards)))
    else:
        print("The dealer has a total of " + str(sum(dealer_cards)) + " with " + str(dealer_cards))
        print("You have a total of " + str(sum(player_cards)) + " with " + str(player_cards))
        break

  if sum(player_cards) > 21:
    print("BUST!")
  elif sum(player_cards) == 21:
    print("You have blackjack!")
  elif sum(dealer_cards) == sum(player_cards):
    print("It's a tie! Play another hand.")
  elif sum(dealer_cards) > sum(player_cards):
    print("The dealer wins at " + str(sum(dealer_cards)) + " with " + str(dealer_cards))
  else:
    print("You WON!")

def looper():
  play_again = str(input("Keep the cards coming? (y/n)  "))
  while play_again == "y".strip(" "):
    main()
    play_again = str(input("Keep the cards coming? (y/n)  "))
  print("Thanks for playing!")
      

main()

looper()