



class Card:

    value_order = ['ACE'] + list(range(2,10)) + ['JACK','QUEEN','KING']
    suit_order = ['Clubs','Diamonds','Hearts','Spades']

    def __init__(self,value,suit):
        self.value = value
        self.suit = suit

    
    @property
    def true_value(self):
        

        l = ('JACK','QUEEN','KING','ACE')
        if self.value in l:
            if self.value == 'ACE':
                return 1
            else:
                return 11 + l.index(self.value)
        
        return self.value

    

    @property
    def order_value(self):


            values_to_i = {value: i for i,value in enumerate(values)}



            return values_to_i + suits.index(self.suit)

    def __lt__(self,card):


        if isinstance(card,Card):




            index_1,index_2 = self.value_order.index(self.value),self.value_order.index(card.value)

            if index_1 == index_2:
                suit_index_1,suit_index_2 = self.suit_order.index(self.suit),self.suit_order.index(card.suit)
                return suit_index_1 < suit_index_2
            else:
                return index_1 < index_2


        







    def __repr__(self):

        return f"{self.value} of {self.suit}"



