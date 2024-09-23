frequency_letter = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z'];

cipher_text = "LQBN XBEE IG HWV EDNL LVDCNSBNNBHC. ZHW'MG DEE VGKGBMGO ZHWV DNNBPCSGCLN. BA ZHW DVG DIEG LH KHSTEGLG ZHWV LDNR VGTEZ IDKR LH WN WNBCP LQG RGZXHVO AVHS LQBN GCKVZTLBHC DEPHVBLQS DN ZHWV RGZ. JWNL VGSGSIGV LQDL LQBN BN DEE AHV LQG PVGDLGV PHHO.";

cnt = {};
for c in cipher_text:
	if (c in frequency_letter):
		if (c in cnt):
			cnt[c] += 1;
		else:
			cnt[c] = 1;

cnt = sorted(cnt.items(), key = lambda x: x[1], reverse = True);

for c, amount in cnt:
	print(c, end='');

print();

for c in frequency_letter:
	print(c, end='');

print("\n\n============================\n");

print("Before: " + cipher_text + '\n');
print("After : ", end='');

substitution = {' ':' ', ',':',', '.':'.', "'":"'"}
def add_pair(e, d) :
	substitution[e] = d

add_pair('A', 'F');
add_pair('B', 'I');
add_pair('C', 'N');
add_pair('D', 'A');
add_pair('E', 'L');
add_pair('F', '?'); # Q X Z
add_pair('G', 'E');
add_pair('H', 'O');
add_pair('I', 'B');
add_pair('J', 'J');
add_pair('K', 'C');
add_pair('L', 'T');
add_pair('M', 'V');
add_pair('N', 'S');
add_pair('O', 'D');
add_pair('P', 'G');
add_pair('Q', 'H');
add_pair('R', 'K');
add_pair('S', 'M');
add_pair('T', 'P');
add_pair('U', '?'); # Q X Z
add_pair('V', 'R');
add_pair('W', 'U');
add_pair('X', 'W');
add_pair('Y', '?'); # Q X Z
add_pair('Z', 'Y');
# FINAL?EOBJCTVSDGHKMP?RUW?Y

# FINALQEOBJCTVSDGHKMPXRUWZY
# FINALQEOBJCTVSDGHKMPZRUWXY
# FINALXEOBJCTVSDGHKMPQRUWZY
# FINALXEOBJCTVSDGHKMPZRUWQY
# FINALZEOBJCTVSDGHKMPQRUWXY
# FINALZEOBJCTVSDGHKMPXRUWQY

for c in cipher_text:
	try:
		print(substitution[c], end='');
	except KeyError:
		print('?', end='');