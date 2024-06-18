import random


suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
cards = []
for suit in suits:
    for rank in ranks:
        card = f'{rank} of {suit}'
        cards.append(card)

print(cards)

card = cards[3]
random_card = random.choice(cards)
print(f'Random card: {random_card}')


deck = [ f'{rank} of {suit}'
         for suit in suits
         for rank in ranks ]

print(deck)