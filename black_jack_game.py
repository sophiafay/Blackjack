# -*- coding: utf-8 -*-
"""black_jack_game.py

Original file is located at
    https://colab.research.google.com/drive/1a5riXYO5zlbSUzn9MOuNNQT9BXfT1Bld
"""

import random

class Blackjack:

  def __init__(self):
    print(f"{'-' * 20} BLACKJACK {'-' * 20}\n")

    self.player_total = 0
    self.player_hand = []

    self.dealer_total = 0
    self.dealer_hand = []

    self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"] * 4

  def play_game(self):
    """
    The Player (you, the user) and the Dealer play a game of Blackjack. They are
    each initially dealt two cards and then it is first the Player's turn. If
    the Player does not get to a total score of 21 or above during his/her turn,
    it is then the Dealer's turn to try to get to 21 or as close as possible. At
    the end, whichever player has a total score closest to or equal to 21
    without being over 21 wins the game.
    """
    if self.initial_deal_and_display():
      if self.player_turn():
        self.dealer_turn()
    self.results()

  def initial_deal_and_display(self):
    """
    To begin the game, deal two cards to the Player and two cards to the Dealer
    and display each of their scores. But, keep the Dealer's second card and
    total score hidden.

    Returns True if we should continue the game, False otherwise.
    """
    self.player_hand = random.sample(self.deck, 2)
    self.remove_cards(self.player_hand)
    self.player_total = self.calculate_score(self.player_hand)

    self.dealer_hand = random.sample(self.deck, 2)
    self.remove_cards(self.dealer_hand)
    self.dealer_total = self.calculate_score(self.dealer_hand)

    self.display_score(show_dealer=False)

    return self.player_total != 21

  def remove_cards(self, hand):
    """
    Remove cards from the deck each time the Player or the Dealer is dealt a new
    card.
    """
    for card in hand:
      self.deck.remove(card)

  def calculate_score(self, hand):
    """
    Calculate the player or the dealer's total score. Number cards have a value
    equal to the value of their number, while face cards (J, Q, and K) have a
    value of 10. Aces (A) have a value of either 11 or 1 depending on the
    Player's/Dealer's total score.
    """
    total = num_aces = 0
    
    for card in hand:
      if card in ["J", "Q", "K"]:
        total += 10
      elif card == "A":
        total += 11
        num_aces += 1
      else:
        total += card

    # handle aces
    while total > 21 and num_aces > 0:
      total -= 10
      num_aces -= 1

    return total

  def results(self):
    """
    If the Player's score is greater than the Dealer's score after each of their
    turns, the player wins. If the Dealer's score is greater than the Player's
    score after each of their turns, the Dealer wins.
    """
    if self.player_total == 21:
      print("Player wins!")
      print("Blackjack!")
    elif self.player_total > 21:
      print("Player busts")
      print("Dealer wins!")
    elif self.dealer_total == 21:
      print("Dealer wins!")
      print("Blackjack!")
    elif self.dealer_total > 21:
      print("Dealer busts")
      print("Player wins!")
    elif self.player_total > self.dealer_total:
      print("Player wins!")
      print(f"{self.player_hand} = {self.player_total} to " + \
            f"Dealer's {self.dealer_hand} = {self.dealer_total}")
    elif self.dealer_total > self.player_total:
      print("Dealer wins!")
      print(f"{self.dealer_hand} = {self.dealer_total} to " + \
            f"Player's {self.player_hand} = {self.player_total}")
    else:
      print("It's a tie!")

  def player_turn(self):
    """
    The Player can continue to choose Hit (get a new card) or Stand (end their
    turn) as long as their total score does not get to exactly 21 or go above
    21. If neither of those scenarios occurs, once they choose Stand, their turn
    ends and it then becomes the Dealer's turn.

    Returns True if we should continue the game, False otherwise.
    """
    print(f"{'=' * 10} PLAYER'S TURN {'=' * 10}\n")
    while True:
      player_turn = input("Would you like to (H)it or (S)tand? ").upper()
      if player_turn == "H":
        print("\nPlayer hits")
        self.player_hand += random.sample(self.deck, 1)
        print(f"Dealt card: {self.player_hand[-1]}")
        self.remove_cards([self.player_hand[-1]])
        self.player_total = self.calculate_score(self.player_hand)
        self.display_score(show_dealer=False)
        if self.player_total >= 21:
          return False
      elif player_turn == "S":
        print("\nPlayer stands")
        self.display_score(show_dealer=False)
        return True
      else:
        print("Please type in H or S")

  def dealer_turn(self):
    """
    The Dealer continually hits as long as the Dealer's total score is less than
    17. Once the Dealer gets to 17 or above, the Dealer's turn automatically
    ends.
    """
    print(f"{'=' * 10} DEALER'S TURN {'=' * 10}\n")
    print(f'Dealer: {self.dealer_hand} = {self.dealer_total}')
    while self.dealer_total < 17:
      print("\nDealer hits")
      self.dealer_hand += random.sample(self.deck, 1)
      print(f"Dealt card: {self.dealer_hand[-1]}")
      self.remove_cards([self.dealer_hand[-1]])
      self.dealer_total = self.calculate_score(self.dealer_hand)
      self.display_score(show_dealer=True)
    if self.dealer_total < 21:
      print("\nDealer stands")

  def display_score(self, show_dealer):
    """
    Display the Player's/Dealer's total score on the screen.
    """
    print(f'Player: {self.player_hand} = {self.player_total}')
    if show_dealer:
      print(f'Dealer: {self.dealer_hand} = {self.dealer_total}')
    else:
      print(f'Dealer: {self.dealer_hand[0]}, ? = ?')
    print()

  def print_deck(self):
    print()
    print('Deck is:', self.deck)
    print('Number of cards:', len(self.deck))
    print()

if __name__ == "__main__":
  play = True
  while play:
    bj = Blackjack()
    bj.play_game()

    while True:
      print()
      play_again = input('Play again? (Y/N)').upper()
      if play_again not in ['Y', 'N']:
        continue
      elif play_again == 'N':
        play = False
        print("Thanks for playing!")
      print()
      break

