frequency_letter = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z'];

cipher_text = "EKEMQ XI LEWI CIESQIH ULEU BVS USEQTPMTTMBQT ESI FIMQK PBQMUBSIH. ET E SITVCU XI ESI GLEQKMQK ULI IQGSDAUMBQ PIULBH EKEMQ. ULI QIX OID JBS QIYU PIIUMQK XMCC FI ABCDKBQ. MU MT MPAISEUMWI ULEU DBV ECC EUUIQH ECC PIIUMQKT JSBP LISI BQ MQ.";

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

add_pair('A', 'P');
add_pair('B', 'O');
add_pair('C', 'L');
add_pair('D', 'Y');
add_pair('E', 'A');
add_pair('F', 'B');
add_pair('G', 'C');
add_pair('H', 'D');
add_pair('I', 'E');
add_pair('J', 'F');
add_pair('K', 'G');
add_pair('L', 'H');
add_pair('M', 'I');
add_pair('N', '?');
add_pair('O', 'K');
add_pair('P', 'M');
add_pair('Q', 'N');
add_pair('R', '?');
add_pair('S', 'R');
add_pair('T', 'S');
add_pair('U', 'T');
add_pair('V', 'U');
add_pair('W', 'V');
add_pair('X', 'W');
add_pair('Y', 'X');
add_pair('Z', '?');

for c in cipher_text:
	try:
		print(substitution[c], end='');
	except KeyError:
		print('?', end='');

