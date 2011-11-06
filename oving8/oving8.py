from sys import stdin, stderr

def beste_sti(nm, sans):
	
	
	n = len(sans)
	done = [0]*n
	nesteNode=0
	sti=""
	for i in range(n):
		node = nesteNode
		sti+=(str(node)+"-")
		if node==n-1:
			return sti
#		print "jobber med node",node
		done[node]=1
		w=0
		for nabo in range(n):
			if not done[nabo]:
#				print "nm",nm[node][nabo]
				if nm[node][nabo]:
					if sans[nabo]>w:
						w=sans[nabo]
#						print "w",w
						nesteNode=nabo
	print 0
	exit()
#	return sti
	
	# SKRIV DIN KODE HER

n = int(stdin.readline())
sansynligheter = [float(x) for x in stdin.readline().split()]
nabomatrise = []
for linje in stdin:
    naborad = [0] * n
    naboer = [int(nabo) for nabo in linje.split()]
    for nabo in naboer:
        naborad[nabo] = 1
    nabomatrise.append(naborad)
print beste_sti(nabomatrise, sansynligheter)[0:-1]
