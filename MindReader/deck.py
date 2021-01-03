from card import Card
import random



class Deck:

    
    SUITS = ['Hearts','Spades','Clubs','Diamonds']
    VALUES= list(range(2,10)) + ['JACK','QUEEN','KING','ACE']

    def __init__(self):

        self._create_deck()
    

    @property
    def empty(self):
        return not self.deck

    def _create_deck(self):


        self.deck = [Card(value,suit) for value in self.VALUES for suit in self.SUITS]


        self.shuffle()
    
    
    def shuffle(self):

        random.shuffle(self.deck)

    def remove_card(self):


        card = self.deck.pop()


        return card
















