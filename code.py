'''

- 2025/11/09 12:54 am: Starting the project. Will try to get all the code for the user functions done.
- 2025/11/09 01:54 am: Completed basic code for blackjack game to play.  
- 2025/11/09 02:07 pm: Added ability to play multiple games.
- 2025/11/09 02:15 pm: Added money/betting gameplay

'''
import random, os

starter_deck = []
dealer_hand = []
player_hand = []
wins = 0
losses = 0
ties = 0
games = 0
cash = 1000
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
    card_index = random.randint(0,len(starter_deck)-1)
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




while True:
    games += 1
    #Put all cards back in deck
    reset_deck()
    player_hand = []
    dealer_hand = []
    #User enters desired bet
    while True:
        try:
            bet = int(input(f'How much money would you like to bet? Current Balance: ${cash}\n> '))
            if bet <= cash:
                cash -= bet
                break
            else:
                print('Max bet is total cash')
        except:
            print('Please enter an integer value!')
    #Card dealing (start with 2 cards each)
    dealer_hand.append(pick_card())
    player_hand.append(pick_card())
    dealer_hand.append(pick_card())
    player_hand.append(pick_card())
    #Gameplay loop
    while True:
        #Breaks if any hit or start with Blackjack
        if count_total(player_hand) == 21 or count_total(dealer_hand) == 21:
            break
        #Can see one of dealers cards, and your cards + total count
        print(f'You can see the dealer has a {dealer_hand[0]}')
        print(f'You have a {', and a '.join(player_hand)}\nYour card count is {count_total(player_hand)}')
        player_choice = input('[h] hit or [s] stand (default)\n> ')
        #If they choose to hit a new card will be added to their hand
        if player_choice.lower().startswith('h'):
            player_hand.append(pick_card())
        #If player busts, break
        if count_total(player_hand) > 21:
            break
        #If dealer has a total under 16 they hit.
        if count_total(dealer_hand) < 16:
            dealer_hand.append(pick_card())
            print('Dealer hits.')
        else:
            print('Dealer stands.')
        #If the dealer busts, break
        if count_total(dealer_hand) > 21:
            break
        #If the player didnt select hit, it defaults to stand. If they stood and dealer stood, break.
        if not player_choice.lower().startswith('h') and count_total(dealer_hand) >= 16:
            break

    #After breaking, shows the dealers full hand and their count, as well as your final count. 
    print(f'The dealers cards were {', and a '.join(dealer_hand)}. Their total is {count_total(dealer_hand)}\nYour Total is {count_total(player_hand)}')
    
    #All possible end game conditions
    if count_total(player_hand) > 21:
        print('You busted! Dealer wins!')
        losses += 1
    elif count_total(dealer_hand) > 21:
        print('Dealer busted! You win!')
        wins += 1
        cash += bet * 2
    elif count_total(player_hand) == 21 and count_total(dealer_hand) != 21:
        print('BLACKJACK! You win!')
        wins += 1
        cash += bet * 2
    elif count_total(player_hand) != 21 and count_total(dealer_hand) == 21:
        print('BLACKJACK! You lose!')
        losses += 1
    elif count_total(dealer_hand) > count_total(player_hand):
        print('Dealer total is higher. You lose!')
        losses += 1
    elif count_total(dealer_hand) < count_total(player_hand):
        print('Your total is higher. You win!')
        wins += 1
        cash += bet * 2
    else:
        print('Tie!')
        ties += 1
        cash += bet

    #Can't play again if they go broke
    if cash <= 0:
        print('You lost all your money!')
        break

    #Can choose to play again (go back to start of first While loop)
    play_again = input('Would you like to play again?(y/n)\n> ')
    if not play_again.lower().startswith('y'):
        break
    else:
        os.system('cls')

print(f'Out of {games} games, you won {wins}, lost {losses} and tied {ties}.\nYou leave with {cash} dollars.')
