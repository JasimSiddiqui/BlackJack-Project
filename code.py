'''
BLACKJACK:

This will be a normal blackjack game. You are started with two random cards and prompted to hit or stand
until you stand or bust (go over 21). The dealers hand is then revealed.

The dealer does not have any significant AI, will simply hit on value 16< and stand >17. 


Possible Additional Features:
- Stats being saved using a .txt file
- Money being involved
- Shifting program to GUI with custom art
- Rigging the game in dealers favor (Realism)

Club Diamond Heart Spade
1 2 3 4 5 6 7 8 9 X J Q K 
'''
import random

starter_deck = []
dealer_hand = []
player_hand = []
cards = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
suits = [' of Hearts', ' of Clubs', ' of Diamonds', ' of Spades']

#Turns starterDeck into a full deck with all cards and all suits
def reset_deck():
    starter_deck.clear()
    for suit in suits:
        for card in cards:
            starter_deck.append(card+suit)

#Takes a random card out of the deck, returns it, and removes it from the starter deck.
def pick_card():
    card_index = random.randint(0,len(starter_deck))
    card = starter_deck[card_index]
    starter_deck.pop(card_index)
    return card

#Counts and returns the total of the given hand, hardcoded logic for starting Ace and Jack,Queen,King being 10
def count_total(hand):
    total = 0
    aces = 0
    for card in hand:
        for c in cards:
            if card.startswith(c):
                if c is cards[0]:
                    total += 11
                    aces += 1
                elif c in cards[-4:]:
                    total += 10
                else:
                    total += cards.index(c) + 1
                break
    #Shifts Aces to 1 if bust
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total



reset_deck()
#Card dealing (start with 4)
dealer_hand.append(pick_card())
player_hand.append(pick_card())
dealer_hand.append(pick_card())
player_hand.append(pick_card())
while True:
    print(f'The dealer has a {dealer_hand[0]}')
    print(f'You have{player_hand}\nYour card count is {count_total(player_hand)}')
    player_choice = input('[h] hit or [s] stand (default)\n> ')
    if player_choice.lower().startswith('h'):
        player_hand.append(pick_card())
    if count_total(player_hand) == 21 or count_total(dealer_hand) == 21:
        break
    if count_total(player_hand) > 21:
        break
    if count_total(dealer_hand) < 16:
        dealer_hand.append(pick_card())
    if not player_choice.lower().startswith('h') and count_total(dealer_hand) >= 16:
        break

print(f'The dealers cards were {dealer_hand}. Their total is {count_total(dealer_hand)}\nYour Total is {count_total(player_hand)}')
if count_total(player_hand) > 21:
    print('You busted! Dealer wins!')
elif count_total(dealer_hand) > 21:
    print('Dealer busted! You win!')
elif count_total(player_hand) == 21 and count_total(dealer_hand) != 21:
    print('BLACKJACK! You win!')
elif count_total(player_hand) != 21 and count_total(dealer_hand) == 21:
    print('BLACKJACK! You lose!')
elif count_total(dealer_hand) > count_total(player_hand):
    print('Dealer total is higher. You lose!')
elif count_total(dealer_hand) < count_total(player_hand):
    print('Your total is higher. You win!')
else:
    print('Tie!')