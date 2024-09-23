cipher_text = "VAOZM HPXC YZGDWZMVODJI OCZ VPOCJMDOT CVN YZXDYZY OCVO OCZMZ DN JIZ DYZV RCDXC RZ RDGG OVFZ PK VN KVMO JA JPM XVPNZ. OJ CZVM HJMZ VWJPO DO, WZ NPMZ OJ VOOZIY OCZ IZSO HZZODIB, PNZ OCZ FZT BZIZMVODJI OJ BZO DI. OCZMZ DN HPXC KGVIIDIB IZZYZY OJ WZ YJIZ, WPO DA RZ XVI ZSZXPOZ OCZ KGVI RZ RDGG WZ AMZZY.";

for k in range(0, 27):
	for c in cipher_text:
		if (ord('A') <= ord(c) and ord(c) <= ord('Z')):
			hihi = ord(c) - ord('A');
			print(chr((hihi + k)%26 + ord('A')), end='');
		else:
			print(c, end='');

	print('\n');