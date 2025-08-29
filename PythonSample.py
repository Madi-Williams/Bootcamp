T = (3007, 3067, 3244, 3375,3574, 3828, 4146, 4336, 4696, 5032,5234,5609,6094,6726,7226,7801,8592,9453,10565,
     11674,12575,13976,14434,15544,17121,18237,19071,20039,21417,22857,23889,24342,25419,26387,27695,28691,29968,
     31459,32854,34515,36330,37134,37998,39490,41725,44123,46302,48050,48570,47195,48651,50066,51784,53291,55124,
     56763,57867,59915,62805,65095,63028,69288)

year = 1959

for i in range(len(T)-1):
		year += 1
		percent_inc = (T[i+1] - T[i])/T[i]*100
		if percent_inc > 10:
			print(year)
		
		
# Set the second entry (index 1) to 17
#Add 4, 5, and 6 to the end of the list
# Remove the first entry from the list
# Sort the list
# Double the list (concatenate the list to itself)
# Insert 25 at index 3
# The final list should equal [4,5,6,25,10,17,4,5,6,10,17]

L = [8,9,10]
L[1] = 17
L.extend([4,5,6])
L.pop(0)
L.sort(reverse=False)
L = L + L
L.insert(3, 25)
print(L)


#The object deck defined below corresponds to a deck of cards. Estimate the probablity that a five card hand will be a flush, as follows:
	#Write a function that accepts a hand of 5 cards as argument, and returns whether the hand is a flush or not.
	#Randomly pull a hand of 5 cards from the deck. Call the function developed in (1) to determine if the hand is a flush.
	#Repeat (2) 10,000 times.
	#Estimate the probability of the hand being a flush from the results of the 10,000 simulations.
	#You may use the function shuffle() from the random library to shuffle the deck everytime before pulling a hand of 5 cards.

deck = [{'value':i, 'suit':c}
for c in ['spades', 'clubs', 'hearts', 'diamonds']
for i in range(2,15)]

### Your code here




