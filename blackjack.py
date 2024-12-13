# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
# Use randint to generate random cards. 
from blackjack_helper import *

# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
player_num = int(input("Welcome to Blackjack! How many players? "))

players = []
scores = {}

for i in range(1, player_num +1):
  player_name = input(f"what is player's {i} name? ")
  players.append(player_name)
  scores[player_name] = 3

# USERS TURNS
while True:
  players_hands = {}
  for player in players:
    user_hand = draw_starting_hand(player.upper() + "'S")
    should_hit = 'y'
    while user_hand < 21:
      should_hit = input("You have {}. Hit (y/n)? ".format(user_hand))
      if should_hit == 'n':
        break
      elif should_hit != 'y':
        print("Sorry I didn't get that.")
      else:
        user_hand += draw_card()
    players_hands[player] = user_hand
    print_end_turn_status(user_hand)
    
  # DEALER'S TURN
  dealer_hand = draw_starting_hand("DEALER")
  while dealer_hand < 17:
    print("Dealer has {}.".format(dealer_hand))
    dealer_hand = dealer_hand + draw_card()
  print_end_turn_status(dealer_hand)

  # GAME RESULT
  
  print_end_game_status(players_hands,dealer_hand,scores)

  #eliminations
  for player in list(players):
    if scores[player] <= 0:
      print(f"{player} eliminated!")
      players.remove(player)
  
  if not players:
    print("All players eliminated")
    break

  # If the players want to play again
  another_game = input("Do you want to play another hand (y/n)? ")
  if another_game.lower() != 'y': 
    break
    
