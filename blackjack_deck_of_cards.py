from random import shuffle


class Card:
    """Each instance of Card  should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades") and
    a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    """
    
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __repr__(self):
        """display the card's value and suit (e.g. "A of Clubs", "J of Diamonds"""
        # return "{} of {}".format(self.value, self.suit)
        return f"{self.value} of {self.suit}"


class Deck:
    """Each instance of Deck  have a cards attribute with all 52 possible instances of Card"""
    
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(value, suit) for suit in suits for value in values]
    
    def __repr__(self):
        """Display information on how many cards are in the deck (e.g. 'Deck of 12 cards')"""
        return f"Deck of {self.count()} cards"
    
    def count(self):
        """Return a count of how many cards remain in the deck."""
        return len(self.cards)
    
    def _deal(self, num):
        """Accepts a number and removes at most that many cards from the deck (it may need to remove fewer
        if you request more cards than are currently in the deck!). If there are no cards left,
        this method should return a ValueError  with the message "All cards have been dealt"."""
        count = self.count()
        actual = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards_dealt = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards_dealt
    
    def deal_card(self):
        """Uses the _deal  method to deal a single card from the deck"""
        return self._deal(1)[0]
    
    def deal_hand(self, hand_size):
        """Accepts a number and uses the _deal method to deal a list of cards from the deck."""
        return self._deal(hand_size)
    
    def shuffle(self):
        """shuffle a full deck of cards. If there are cards missing from the deck, this method should return
         a ValueError  with the message "Only full decks can be shuffled"."""
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        
        shuffle(self.cards)
        return self


def main():
    d = Deck()
    d.shuffle()
    print(*[(card.value, card.suit) for card in d.cards], sep=', ')
    print(d.count())
    card = d.deal_card()
    print(card)
    print((card.value, card.suit))
    print(card.__dict__)
    card2 = d.deal_card()
    print((card2.value, card2.suit))
    hand = d.deal_hand(2)
    print(*[(card.value, card.suit) for card in hand], sep=', ')
    print(d.count())


if __name__ == '__main__':
    main()
