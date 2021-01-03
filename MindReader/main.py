from deck import Deck
from collections import defaultdict




def draw_n_cards(deck,n):

    cards = []

    for _ in range(n):
        card = deck.remove_card()
        cards.append(card)
    

    return cards


def assistants_job(cards):

    
    suits = defaultdict(list)

    for card in cards:
        suits[card.suit].append(card)

        if len(suits[card.suit]) == 2:
            two_cards = suits[card.suit]
            break
    
    print(two_cards)


    values = [card.true_value for card in two_cards]
    
    mod = 13
    distances = [(values[1] - values[0]) % mod,(values[0] - values[1]) % mod]

    
    distance = min(distances)
    print(distance)
    min_index = distances.index(distance)

    if min_index == 0:
        revealed_card,secret_card = two_cards[0],two_cards[1]
    else:
        revealed_card,secret_card = two_cards[1],two_cards[0]


    print(revealed_card,secret_card)
    

    three_other_cards = []
    for card in cards:
        if card not in two_cards:
            three_other_cards.append(card)

    print(three_other_cards)    
    

    minimum_card = min(three_other_cards)
    maximum_card = max(three_other_cards)

    other_card = [card for card in three_other_cards if card is not minimum_card and card is not maximum_card][0]



    print(minimum_card,other_card,maximum_card)

    
    print(revealed_card,end=',')
    if distance == 1:
        revealed_cards = [minimum_card,other_card,maximum_card]
    elif distance == 2:
        revealed_cards = [minimum_card,maximum_card,other_card]
    elif distance == 3:
        revealed_cards = [other_card,minimum_card,maximum_card]
    elif distance == 4:
        revealed_cards = [other_card,maximum_card,minimum_card]
    elif distance == 5:
        revealed_cards = [maximum_card,minimum_card,other_card]
    else:
        revealed_cards = [maximum_card,other_card,minimum_card]



    revealed_cards.insert(0,revealed_card)


    print(','.join(map(str,revealed_cards)))


    magicians_job(revealed_cards,secret_card)










def magicians_job(revealed_cards,secret_card):

    last_three = revealed_cards[-3:]

    minimum,maximum = min(last_three),max(last_three)


    min_index,max_index = last_three.index(minimum),last_three.index(maximum)

    mod = 13

    if min_index == 0 and max_index == 2:
        distance = 1
    elif min_index == 0 and max_index == 1:
        distance = 2
    elif min_index ==1 and max_index == 2:
        distance = 3
    elif min_index == 2 and max_index == 1:
        distance = 4
    elif min_index == 1 and max_index == 0:
        distance = 5
    else:
        distance = 6

    print(distance)


    secret_card_suit =  revealed_cards[0].suit

    secret_card_value = (revealed_cards[0].true_value + distance) % mod


    if secret_card_value == 11:
        secret_card_value = 'JACK'
    elif secret_card_value == 12:
        secret_card_value = 'QUEEN'
    elif secret_card_value == 13:
        secret_card_value = 'KING'
    elif secret_card_value == 1:
        secret_card_value = 'ACE'


    print(f"The secret card is {secret_card_value} of {secret_card_suit}")


















def read_mind():

    
    deck = Deck()
    
    n = 5
    five_cards = draw_n_cards(deck,n)


    assistants_job(five_cards)






if __name__ == "__main__":
    
    read_mind()















