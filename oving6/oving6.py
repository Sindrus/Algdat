from sys import stdin
True=1
False=0

# Quicksort
def oppdeling(innliste):
	a=len(innliste)/2
#	a=len(innliste)-1
	liste = innliste[:a]+innliste[(a)+1:]
#	liste = innliste[:a-1]
#	print liste
	mindre = [x for x in liste if x <= innliste[a]]
	mer = [x for x in liste if x > innliste[a]]
#	mindre = [x for x in innliste[1:] if x <= innliste[0]]
#	mer = [x for x in innliste[1:] if x > innliste[0]]
	return mindre, innliste[a], mer

def sorter(A):
	if len(A) <=1:
		return A
	mindre, r, mer  = oppdeling(A)
	return sorter(mindre) + [r] + sorter(mer)

#Binnart search
def binup(A,upper):
	mini = 0
	maxi = len(A)-1
	while True:
		mid = (mini + maxi)/2
		if upper > A[mid]:
			mini=mid+1
		else:
			maxi=mid-1
		
		if upper == A[mid] or mini > maxi:
			if upper > A[mid] and mid < (len(A)-1):
				return A[mid+1]
			else:
				return A[mid]

def bindown(A, lower):
	mini = 0
	maxi = len(A)-1
	while True:
		mid = (mini + maxi)/2
		if lower > A[mid]:
			mini = mid+1
		else:
			maxi = mid-1
		if lower == A[mid] or mini > maxi:
			if lower < A[mid] and mid > 0:
				return A[mid-1]
			else:
				return A[mid]

#Resterende kode
liste = []
for x in stdin.readline().split():
    liste.append(int(x))

sortert = sorter(liste)

for linje in stdin:
    ord = linje.split()
    minst = int(ord[0])
    maks = int(ord[1])
    print str(bindown(sortert,minst))+" "+str(binup(sortert,maks))
