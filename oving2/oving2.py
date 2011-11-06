from sys import stdin
from collections import deque

# var ikke definert i den gamle python-versjonen som 
# ligger paa noen av stud sine maskiner
True = 1
False = 0

class Node:
    barn = None 
    ratatosk = None
    nesteBarn = None # bare til bruk i DFS
    level = None
    def __init__(self):
        self.barn = []
        self.ratatosk = False
        self.nesteBarn = 0

def dfs(rot): #Her er koden for dfs
	level=0
	
	que = []
	que.append(rot)
	if rot.ratatosk:
		return level
	while que:
		n=que[len(que)-1]
		if n.ratatosk:
			return level
		if n.nesteBarn < len(n.barn):
			que.append(n.barn[n.nesteBarn])
			n.nesteBarn += 1
			level+=1
		else:
			que.pop()
			level-=1
		
def bfs(rot): # Her kommer koden for bfs
	q = deque()				#Initialiserer lista
	rot.level = 0				#Setter levelen til rota
	if rot.ratatosk:			#Sjekker om ratatosk er i rotnoden
		return 0			#Hvis den er, returner level 0
	q.append(rot)				#Legger til rota i lista
	for x in rot.barn:			#Finner fram alle barna
		x.level = rot.level+1		#Setter nodebarn levelen til ett over foreldrenoden
		q.append(x)			#Setter nodebarnet i lista
	
	while q:				#Mens det er noder i lista
		for x in q[0].barn:		#Finner alle barna til node en i lista
			x.level = q[0].level+1	#Setter levelen til nodebarnet
			q.append(x)		#Legger nodebarnet til lista
		n = q.popleft()			#Tar ut node nr 1 i lista
		if n.ratatosk:			#Sjekker om ratatosk er i lista
			return n.level		#Returnerer levelen til noden
	
funksjon = stdin.readline().strip()
antall_noder = int(stdin.readline())
noder = []
for i in range(antall_noder):
    noder.append(Node())
start_node = noder[int(stdin.readline())]
ratatosk_node = noder[int(stdin.readline())]
ratatosk_node.ratatosk = True
for linje in stdin:
    tall = linje.split()
    temp_node = noder[int(tall.pop(0))]
    for barn_nr in tall:
        temp_node.barn.append(noder[int(barn_nr)])

if funksjon == 'dfs':
    print dfs(start_node)
elif funksjon == 'bfs':
    print bfs(start_node)
elif funksjon == 'velg':
    print dfs(start_node) # SKRIV DIN KODE HER
