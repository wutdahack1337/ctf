cipher_text = "JR UNIR QVFPBIRERQ GUNG BHE YNFG GUERR GENAFZVFFVBAF JR'ER RNFVYL QRPVCURERQ. JR UNIR GNXRA PNER BS GUR CNEGL ERFCBAFVOYR SBE GURVE RAPBQVAT NAQ NER ABJ HFVAT N ARJ ZRGUBQ. HFR GUR VASBEZNGVBA CEBIVQRQ NG YNFG JRRX.F ZRRGVAT GB QRPVCURE NYY ARJ ZRFFNTRF. NAQ ERZRZORE, GUVF JRRX.F XRL VF BOSHFPNGRQ.";

for k in range(0, 27):
	for c in cipher_text:
		if (ord('A') <= ord(c) and ord(c) <= ord('Z')):
			hihi = ord(c) - ord('A');
			print(chr((hihi + k)%26 + ord('A')), end='');
		else:
			print(c, end='');

	print('\n');