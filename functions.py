def dealer(card, all_cards):
	probabilities = [0, 0, 0, 0, 0, 0]

	for card1 in all_cards:
		print(card1)
		deck1 = all_cards.copy()
		deck1.remove(card1)
		cards = [card, card1]
		sum = card1 + card
		turnAceInto1(sum, cards)
		probabilities = addProbability(sum, probabilities, 1)
		if sum < 17:
			for card2 in deck1:
				deck2 = deck1.copy()
				deck2.remove(card2)
				cards = [card, card1, card2]
				sum = card + card1 + card2
				turnAceInto1(sum, cards)
				probabilities = addProbability(sum, probabilities, 1/len(deck1))
				if sum < 17:
					for card3 in deck2:
						deck3 = deck2.copy()
						deck3.remove(card3)
						cards = [card, card1, card2, card3]
						sum = card + card1 + card2 + card3
						turnAceInto1(sum, cards)
						probabilities = addProbability(sum, probabilities, 1/len(deck2)**2)
						if sum < 17:
							for card4 in deck3:
								deck4 = deck3.copy()
								deck4.remove(card4)
								cards = [card, card1, card2, card3, card4]
								sum = card + card1 + card2 + card3 + card4
								turnAceInto1(sum, cards)
								probabilities = addProbability(sum, probabilities, 1/len(deck3)**3)
								if sum < 17:
									for card5 in deck4:
										deck5 = deck4.copy()
										deck5.remove(card5)
										cards = [card, card1, card2, card3, card4, card5]
										sum = card + card1 + card2 + card3 + card4 + card5
										turnAceInto1(sum, cards)
										probabilities = addProbability(sum, probabilities, 1/len(deck4)**4)
										if sum < 17:
											for card6 in deck5:
												deck6 = deck5.copy()
												deck6.remove(card6)
												cards = [card, card1, card2, card3, card4, card5, card6]
												sum = card + card1 + card2 + card3 + card4 + card5 + card6
												turnAceInto1(sum, cards)
												probabilities = addProbability(sum, probabilities, 1/len(deck5)**5)
												if sum < 17:
													for card7 in deck6:
														deck7 = deck6.copy()
														deck7.remove(card7)
														cards = [card, card1, card2, card3, card4, card5, card6, card7]
														sum = card + card1 + card2 + card3 + card4 + card5 + card6 + card7
														turnAceInto1(sum, cards)
														probabilities = addProbability(sum, probabilities, 1/len(deck6)**6)
														if sum < 17:
															for card8 in deck7:
																deck8 = deck7.copy()
																deck8.remove(card8)
																cards = [card, card1, card2, card3, card4, card5, card6, card7, card8]
																sum = card + card1 + card2 + card3 + card4 + card5 + card6 + card7 + card8
																turnAceInto1(sum, cards)
																probabilities = addProbability(sum, probabilities, 1/len(deck7)**7)
																if sum < 17:
																	for card9 in deck8:
																		deck9 = deck8.copy()
																		deck9.remove(card9)
																		cards = [card, card1, card2, card3, card4, card5, card6, card7, card8, card9]
																		sum = card + card1 + card2 + card3 + card4 + card5 + card6 + card7 + card8 + card9
																		turnAceInto1(sum, cards)
																		probabilities = addProbability(sum, probabilities, 1/len(deck8)**8)
	return probabilities

def turnAceInto1(sum, cards):
	while sum > 21:
		if 11 in cards:
			cards[cards.index(11)] = 1
			sum -= 10
		else:
			return

def addProbability(sum, probabilities, probability):
	print(sum, sum > 16 and sum < 22)
	if sum > 16 and sum < 22:
		probabilities[sum-17] += probability
	elif sum > 21:
		probabilities[5] += probability
	print(probabilities)
	print("")
	return probabilities