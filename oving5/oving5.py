from sys import stdin

Inf = float(1e3000)
False = 0
True = 1

def mst(nm):
	visited = []
#	print nm
	mest = 0
	visited.append(nm[0])
		
#	teller=0
#	nodenar=Inf
#	narnode=0
#	for tall in visited[0]:
#		if tall < nodenar:
#			nodenar = tall
#			narnode = teller
#		teller+=1
#		
#	visited.append(nm[narnode])
#	print visited
	
	
#	print nm[0]
#	print visited
	
#	print nm[0] not in visited
	maks = 0
#	while len(visited)<len(nm):
	while True:
		stilengde = Inf
		node = -1
		teller = 0
		for noder in visited:
		#	stilengde = Inf
			teller = 0
			for tall in noder:
				if tall < stilengde and (nm[teller] not in visited):
					stilengde = tall
					node = teller
				teller += 1
#			if stilengde > maks and not stilengde==Inf:# and (len(visited)<len(nm)-1):
#				maks = stilengde
		visited.append(nm[node])
#		print visited
		if len(visited)==len(nm):
			break
		if stilengde > maks and not stilengde==Inf and len(visited)<(len(nm)):
			maks = stilengde
	return maks
	
	pass
	teller=0
	nodenar=Inf
	narnode=0
	for noder in visited:
		nodenar=Inf
		narnode = 0
		teller = 0
		for tall in noder:
			print noder
			print "teller",teller
			if tall < nodenar and not nm[teller] in visited:
				nodenar = tall
				narnode = teller
			teller+=1
	
	print nm[narnode] in visited
	print visited
	return nodenar
	
	
	pass
	for n in nm:
		for node in visited:
			ind=0
			minst=Inf
			for tall in node:
				if tall < minst:
					print "Funnet mindre tall"
					tall = minst
					visited.append(node[ind])
				ind+=1
			if minst > mest:
				mest = minst
	return mest
		


linjer = []
for str in stdin:
    linjer.append(str)
n = len(linjer)
nabomatrise = [None] * n
node = 0
for linje in linjer:
    nabomatrise[node] = [Inf] * n
    for k in linje.split():
        data = k.split(':')
        nabo = int(data[0])
        vekt = int(data[1])
        nabomatrise[node][nabo] = vekt
    node += 1
print mst(nabomatrise)

