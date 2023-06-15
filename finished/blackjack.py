"""Blackjack, by Al Sweigart al@inventwithpython.com
 The classic card game also known as 21. (This version doesn't have
 splitting or insurance.)
 More info at: https://en.wikipedia.org/wiki/Blackjack
 This code is available at https://nostarch.com/big-book-small-python-programming
 Tags: large, game, card game"""
import sys

from blackjack_deck_of_cards import Deck


class Game:
    # Set up the constants:
    # (A list of chr codes is at https://inventwithpython.com/charactermap)
    suits = {'HEARTS': chr(9829),
             'DIAMONDS': chr(9830),
             'SPADES': chr(9824),
             'CLUBS': chr(9827),
             'BACKSIDE': 'backside'}
    
    def __init__(self):
        self.money = 5000
        self.bet = 0
        self.deck = None
        self.player_cards = list()
        self.player_total = 0
        self.dealer_cards = list()
        self.dealer_total = 0
        self.game_stops = 0
    
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
          On your first play, you can (D)ouble down to double your bet:
          player takes a single card, and finishes the round.
          In case of a tie, the bet is returned to the player.
          The dealer stops hitting at 17.''')
        
    def take_bet(self):
        print('Money: ', self.money)
        print(f'How much do you bet? (100-{self.money}, or QUIT)')
        bet = input('> ')
        if bet.lower().startswith('q'):
            print('Thanks for playing!')
            sys.exit()
        else:
            if 100 <= int(bet) <= self.money:
                self.bet = int(bet)
                print(f'Bet: {self.bet}\n')
            else:
                self.take_bet()
    
    @staticmethod
    def count_points(cards):
        """aces count as either 1 or 11"""
        values = list()
        aces_count = 0
        for card in cards:
            if card.value.isdecimal():
                values.append(int(card.value))
            else:
                if card.value != 'A':
                    values.append(10)
                else:
                    aces_count += 1
        if aces_count == 0:
            return sum(values)
        elif aces_count == 1:
            if sum(values) + 11 <= 21:
                values.append(11)
            else:
                values.append(1)
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
    
    def clean_table(self):
        deck = Deck()
        deck.shuffle()
        self.deck = deck
        self.bet = 0
        self.player_total = 0
        self.player_cards = list
        self.dealer_total = 0
        self.dealer_cards = list
        self.game_stops = 0
        
    def start_round(self):
        self.player_cards = self.deck.deal_hand(1)
        self.dealer_cards = self.deck.deal_hand(1)
        Game.take_card(self, 'player')
        Game.take_card(self, 'dealer')
    
    def take_card(self, who):
        new_card = self.deck.deal_card()
        if who == 'dealer':
            self.dealer_cards.append(new_card)
            self.dealer_total = Game.count_points(self.dealer_cards)
        else:
            self.player_cards.append(new_card)
            self.player_total = Game.count_points(self.player_cards)
    
    def show_table(self):
        if self.game_stops:
            dealer_points = self.dealer_total
            dealer_cards = self.dealer_cards
        else:
            dealer_points = '???'
            dealer_cards = list()
            dealer_cards.append(self.dealer_cards[0])
            for _ in range(len(self.dealer_cards) - 1):
                dealer_cards.append('BACKSIDE')
        print('DEALER: ', dealer_points)
        print(*[(card.value, card.suit) for card in self.dealer_cards], sep=', ')
        Game.display_cards(dealer_cards)
        print('PLAYER: ', self.player_total)
        print(*[(card.value, card.suit) for card in self.player_cards], sep=', ')
        Game.display_cards(self.player_cards)
    
    def check_total(self) -> str:
        """
        """
        if len(self.player_cards) == 2 and self.player_total == 21:  # (1)
            self.game_stops = 1
            if self.dealer_total == 21:
                return 'tie'
            else:
                self.money += self.bet
                return f'blackjack! player wins {self.bet}!'
        elif self.player_total > 21:  # (2)
            self.game_stops = 1
            self.money -= self.bet
            return 'player busts!'
        elif self.game_stops:
            if self.dealer_total > 21:
                self.money += self.bet
                return f'dealer busts. player wins {self.bet}!! '
            elif self.player_total == self.dealer_total:
                return 'tie'
            elif self.dealer_total > self.player_total:  # (3)
                self.money -= self.bet
                return 'player busts!'
            elif self.game_stops and self.player_total > self.dealer_total:
                self.money += self.bet
                return f'player wins {self.bet}!'
        else:
            return 'next turn'
        
    def dealer_move(self):
        """Dealer draws cards until his hand achieves a total of 17 or higher
        If the total is 17 or more, it must stand. If the total is 16 or under, he must take a card.
        """
        if self.dealer_total >= 17:
            return 'stand'
        else:
            self.take_card('dealer')
            return 'hit'
    
    @staticmethod
    def ask_player():
        print('(H)it, (S)tand, (D)ouble down>')
        player_decision = input('> ')
        if player_decision.lower().startswith('h'):
            return 'hit'
        elif player_decision.lower().startswith('s'):
            return 'stand'
        elif player_decision.lower().startswith('d'):
            return 'double'
    
    def player_move(self):
        """Player decisions: "hit" (take a card), "stand" (stop without taking a card),
        "double" (double their wager, take a single card, and finish)."""
        player_decision = self.ask_player()
        print('PLAYER: ', player_decision)
        if player_decision == 'stand':
            return False
        elif player_decision == 'double':
            self.bet *= 2
            self.game_stops = 1
        print('take a card')
        self.take_card('player')
        print(f'You drew a {self.player_cards[-1].value} of {Game.suits[self.player_cards[-1].suit.upper()]}')
        return True
   
    def play(self):
        self.print_intro()
        while True:
            self.clean_table()
            self.take_bet()
            self.start_round()
            result = self.check_total()
            self.show_table()
            print('\n', result)
            while not self.game_stops:
                dealer_move = self.dealer_move()
                print('DEALER: ', dealer_move)
                player_move = self.player_move()
                if not player_move and self.dealer_total >= 17:
                    self.game_stops = 1
                result = self.check_total()
                self.show_table()
                print('\n', result)
            
            print('MONEY: ', self.money)
            print('Press Enter to continue...')
            input()


def main():
    new = Game()
    Game.play(new)


if __name__ == '__main__':
    main()
