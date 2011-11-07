from sys import stdin, maxint

def korteste_rute(rekkefolge, nabomatrise, byer):
	return 1
	# SKRIV DIN KODE HER

testcases = int(stdin.readline())
for test in range(testcases):
	byer = int(stdin.readline())
	rekkefolge = [int(by) for by in stdin.readline().split()]
	nabomatrise = []
	for by in range(byer):
		# SKRIV DIN KODE HER
		print by
	print korteste_rute(rekkefolge, nabomatrise, byer)
