#The object deck defined below corresponds to a deck of cards. Estimate the probablity that a five card hand will be a flush, as follows:
	#Write a function that accepts a hand of 5 cards as argument, and returns whether the hand is a flush or not.
	#Randomly pull a hand of 5 cards from the deck. Call the function developed in (1) to determine if the hand is a flush.
	#Repeat (2) 10,000 times.
	#Estimate the probability of the hand being a flush from the results of the 10,000 simulations.
	#You may use the function shuffle() from the random library to shuffle the deck everytime before pulling a hand of 5 cards.

import random as rd

deck = [{'value':i, 'suit':c}
for c in ['spades', 'clubs', 'hearts', 'diamonds']
for i in range(2,15)]

### Your code here
def find_flush(h):
	first_card = h[0]['suit']
	x = 1
	s = 0
	for x in range(5):
		if h[x]['suit'] == first_card:
			s += 1
	if s == 5:
		return(True)
	else:
		return(False)
					
def get_hand():
	random_hand = []
	for i in range (5):
		card = rd.choice(deck)
		random_hand.append(card)
	return(random_hand)

number_of_flushes = 0

for x in range (50,000):
	hand = get_hand()
	flush = find_flush(hand)
	if flush == True:
		number_of_flushes += 1
	
print(number_of_flushes)


