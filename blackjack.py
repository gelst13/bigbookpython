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
    
    @staticmethod
    def print_intro():
        print('Blackjack, by Al Sweigart al@inventwithpython.com')
        print('''Rules:
          Try to get as close to 21 without going over.
          Kings, Queens, and Jacks are worth 10 points.
          Aces are worth 1 or 11 points.
          Cards 2 through 10 are worth their face value.
          (H)it to take another card.
          (S)tand to stop taking cards.
          On your first play, you can (D)ouble down to increase your bet
          but must hit exactly one more time before standing.
          In case of a tie, the bet is returned to the player.
          The dealer stops hitting at 17.''')
        
    def take_bet(self):
        print(f'How much do you bet? (100-{self.money}, or QUIT)')
        bet = input('> ')
        if bet.lower().startswith('q'):
            self.bet = 0
        else:
            if 100 < int(bet) <= self.money:
                self.bet = int(bet)
                print(f'Bet: {self.bet}')
            else:
                self.take_bet()
    
    @staticmethod
    def count_points(cards):
        values = list()
        for card in cards:
            if card.value.isdecimal():
                values.append(int(card.value))
            else:
                if card.value != 'A':
                    values.append(10)
                else:
                    values.append(1)
        return sum(values)
    
    @staticmethod
    def display_cards(cards: list):
        """Display all the cards in the cards list."""
        rows = ['', '', '', '', '']  # The text to display on each row.
        
        for i, card in enumerate(cards):
            rows[0] += ' ___  '  # the top line of the card.
            if card == 'BACKSIDE':
                #  a card's back:
                rows[1] += '|## | '
                rows[2] += '|###| '
                rows[3] += '|_##| '
            else:
                # the card's front:
                rank = card.value  # The card is a tuple data structure.
                suit = Game.suits[card.suit.upper()]
                rows[1] += '|{} | '.format(rank.ljust(2))
                rows[2] += '| {} | '.format(suit)
                rows[3] += '|_{}| '.format(rank.rjust(2, '_'))
        
        # Print each row on the screen:
        for row in rows:
            print(row)
    
    def play_round(self):
        self.dealer_cards = self.deck.deal_hand(2)
        print('DEALER: ', Game.count_points(self.dealer_cards))
        print(*[(card.value, card.suit) for card in self.dealer_cards], sep=', ')
        Game.display_cards(self.dealer_cards)
        
        self.player_cards = self.deck.deal_hand(2)
        print('PLAYER: ', Game.count_points(self.player_cards))
        print(*[(card.value, card.suit) for card in self.player_cards], sep=', ')
        Game.display_cards(self.player_cards)
    
    def play(self):
        self.print_intro()
        self.play_round()
        
        self.take_bet()


def main():
    deck = Deck()
    deck.shuffle()
    new = Game(deck)
    Game.play(new)


if __name__ == '__main__':
    main()
