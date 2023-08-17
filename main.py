from functions import dealer

# Create a list with all the cards available
all_cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]
num_of_decks = int(input("How many decks do you want to play with? "))

all_cards *= num_of_decks
all_cards.sort()
print("All cards:", all_cards)

cards_dealt = [] # A list of all the cards already played in the game
num_of_players = int(input("How many players are there (without the dealer)? "))
your_cards = [] # A list of the cards available to the player
remaining_cards = all_cards.copy()

# Add cards of the player to the list
for i in range(2):
	your_cards.append(int(input(f"What is your {i+1}. card? ")))
your_cards.sort()
print("Your cards:", your_cards)

# Save the card of the dealer
dealer_card = int(input("What card does the dealer have? "))

# Add cards of the other players to the list of played cards and remove them from the remaining cards
for card in your_cards:
	cards_dealt.append(card)
cards_dealt.append(dealer_card)
for i in range((num_of_players-1)*2):
	cards_dealt.append(int(input(f"What is the {i%2+1}. card of the {int((i-i%2)/2)+1}. player? ")))
print("Cards dealt:", cards_dealt)

for card in cards_dealt:
	remaining_cards.remove(card)
print("Remaining cards:", remaining_cards)

probabilities = dealer(dealer_card, remaining_cards)
print(probabilities)