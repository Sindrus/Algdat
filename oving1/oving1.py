from sys import stdin

class Kubbe:
    vekt = None
    neste = None
    def __init__(self, vekt):
        self.vekt = vekt 
        self.neste = None 

def spor(kubbe):
# SKRIV DIN KODE HER
	stor = kubbe.vekt
	while kubbe.neste:
		kubbe = kubbe.neste
		if kubbe.vekt > stor:
			stor = kubbe.vekt
	return stor
	

# Oppretter lenket liste
forste = None
siste = None
for linje in stdin:
    forrige_siste = siste
    siste = Kubbe(int(linje))
    if forste == None:
        forste = siste
    else:
        forrige_siste.neste = siste

# Kaller loesningsfunksjonen og skriver ut resultatet
print spor(forste)
