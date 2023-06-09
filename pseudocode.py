"""Blackjack, by Al Sweigart al@inventwithpython.com
 The classic card game also known as 21. (This version doesn't have
 splitting or insurance.)
 More info at: https://en.wikipedia.org/wiki/Blackjack
 This code is available at https://nostarch.com/big-book-small-python-programming
 Tags: large, game, card game"""

from blackjack_deck_of_cards import Deck


class Game:
    # Set up the constants:
    # (A list of chr codes is at https://inventwithpython.com/charactermap)
    suits = {'HEARTS': chr(9829),
             'DIAMONDS': chr(9830),
             'SPADES': chr(9824),
             'CLUBS': chr(9827),
             'BACKSIDE': 'backside'}
    
    def __init__(self, deck):
        self.money = 5000
        self.bet = 0
        self.deck = deck
        self.player_cards = None
        self.dealer_cards = None
        self.game_stops = 0
    
    def take_bet(self):
        print(f'How much do you bet? (100-{self.money}, or QUIT)')
        bet = input('> ')
    
    @staticmethod
    def count_points(cards):
        print('count_points')
    
    def show_table(self):
        print('DEALER: ???')
        self.display_cards()
        print('PLAYER: ???')
        self.display_cards()
        
    @staticmethod
    def display_cards():
        """Display all the cards in the cards list."""
        print('''
         ___   ___
        |## | |## |
        |###| |###|
        |_##| |_##|
         ---   --- ''')
    
    def start_round(self, num):
        self.dealer_cards = self.deck.deal_hand(num)
        print('DEALER: ', Game.count_points(self.dealer_cards))
        print()
        self.player_cards = self.deck.deal_hand(num)
        print('PLAYER: ', Game.count_points(self.player_cards))
    
    def check_total(self):
        print('check_total')
    
    def dealer_move(self):
        print('dealer_move')
        return 'hit'
    
    def ask_player(self):
        print('ask_player')
        return input()
    
    def player_move(self):
        player_decision = self.ask_player()
    
    
    def play(self):
        # self.print_intro()
        self.take_bet()
        print()
        self.start_round(2)
        self.show_table()
        result = self.check_total()
        print('\n', result)
        while not self.game_stops:
            dealer_move = self.dealer_move()
            print('DEALER: ', dealer_move)
            self.player_move()
            self.show_table()
            self.check_total()
            self.game_stops = 1
        print('win, lost or tie. Change money +-')
        


def main():
    deck = Deck()
    deck.shuffle()
    new = Game(deck)
    Game.play(new)


if __name__ == '__main__':
    main()
