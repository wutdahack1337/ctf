cipher_text = "PYB DRO XOHD WOODSXQ LO CEBO DY ECO UOI WKXUSXN. DROBO RKFO LOOX CYWO QBOKD SNOKC PVISXQ KBYEXN YEB WOODSXQC KC YP VKDO. DRO KEDRYBSDI GSVV QY YFOB CYWO YP DROW DY COO SP DROI PSD SXDY YEB KQOXNK.";

for k in range(0, 27):
	for c in cipher_text:
		if (ord('A') <= ord(c) and ord(c) <= ord('Z')):
			hihi = ord(c) - ord('A');
			print(chr((hihi + k)%26 + ord('A')), end='');
		else:
			print(c, end='');

	print('\n');