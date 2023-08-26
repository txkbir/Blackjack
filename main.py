################## Blackjack Project #####################

############### My Blackjack House Rules #####################

# The deck is unlimited in size. 
# There are no jokers. 
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import random
from typing import List
from art import logo
from replit import clear
#                                        J,  Q,  K
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def main():
  play = True
  while play:
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start_game != 'y':
      play = False
      continue
  
    clear()
    print(logo)
    user_cards = []
    computer_cards = []
    for _ in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())
      
    printStateOfGame(user_cards, computer_cards)
    if calculate_score(computer_cards) == 0 and calculate_score(user_cards) == 0:
      printEndgame(user_cards, computer_cards)
      print("You both have Blackjack. Draw")
    elif calculate_score(computer_cards) == 0:
      printEndgame(user_cards, computer_cards)
      print("Opponent has Blackjack. You lose")
    else:
      continuePulling = True
      while continuePulling:
        pullCards = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if pullCards == 'n':
          while calculate_score(computer_cards) < 17:
            computer_cards.append(deal_card())
          printEndgame(user_cards, computer_cards)
          compare(user_cards, computer_cards)
          continuePulling = False
        else:
          user_cards.append(deal_card())
          printStateOfGame(user_cards, computer_cards)
          if calculate_score(user_cards) > 21:
            printEndgame(user_cards, computer_cards)
            compare(user_cards, computer_cards)
            continuePulling = False
  

def printStateOfGame(user_cards: List[int], computer_cards: List[int]) -> None:
  user_score = calculate_score(user_cards)
  if user_score == 0:
    user_score = 21
  print(f"\tYour cards: {user_cards}, current score: {user_score}")
  print(f"\tComputer's first card: {computer_cards[0]}")


def printEndgame(user_cards: List[int], computer_cards: List[int]) -> None:
  user_score = calculate_score(user_cards)
  if user_score == 0:
    user_score = 21
  npc_score = calculate_score(computer_cards)
  if npc_score == 0:
    npc_score = 21
  print(f"\tYour final hand: {user_cards}, final score: {user_score}")
  print(f"\tComputer's final hand: {computer_cards}, final score: {npc_score}")


def deal_card() -> int:
  return random.choice(cards)


def calculate_score(cards: List[int]) -> int:
  score = sum(cards)
  if len(cards) == 2 and score == 21:
    return 0
  if score > 21 and 11 in cards:
    i = cards.index(11)
    cards[i] = 1
    score -= 10
  return score


def compare(user_cards: List[int], computer_cards: List[int]) -> None:
  if calculate_score(computer_cards) == 21 or calculate_score(computer_cards) == 0:
    print('Dealer hit Blackjack. You lose.')
  elif calculate_score(user_cards) == 21 or calculate_score(user_cards) == 0:
    print('You hit Blackjack! You win!')
  elif calculate_score(user_cards) > 21:
    print('You went over. You lose.')
  elif calculate_score(computer_cards) > 21:
    print('Opponent went over. You win!')
  elif calculate_score(user_cards) > calculate_score(computer_cards):
    print('You win!')
  elif calculate_score(user_cards) < calculate_score(computer_cards):
    print('Bust. You lose')
  else:
    print('Draw')


main()