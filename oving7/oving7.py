from sys import stdin
from itertools import repeat

def flett(left, right):
	resultat = []
	while len(left)>0 or len(right)>0:
		if len(left)>0 and len(right)>0:
			if left[0][0] > right[0][0]:
				resultat.append(right.pop(0))
			else:
				resultat.append(left.pop(0))
		elif len(left)>0:
			resultat.append(left.pop(0))
		elif len(right)>0:
			resultat.append(right.pop(0))
	return resultat
		

def merge(decks):
	if len(decks) <=1:
		return decks
	middle = len(decks)/2
	left = decks[:middle]
	right = decks[middle:]
	left = merge(left)
	right = merge(right)
	res = flett(left, right)
	return res

def mergesort(decks):
	mid = len(decks)/2
	left,right=decks[:mid],decks[mid:]
	if len(left) > 1:
		left = mergesort(left)
	if len(right) > 1:
		right = mergesort(right)
	res = []
	while left and right:
		if left[-1] >= right[-1]:
			res.append(left.pop())
		else:
			res.append(right.pop())
	res.reverse()
	print "Right",right
	print "Left",left
	return (left or right) + res

	
deck = []
for line in stdin:
	(index, list) = line.split(':')
	deck = deck + zip(map(int, list.split(',')), repeat(index))

decks=mergesort(deck)
#decks=merge(deck)

final=''
for x in decks:
	final +=str(x[1])
print final
