from Crypto.Util.number import getPrime, bytes_to_long
import random
import os

e = 65537
p = getPrime(1024)
# tìm p sao cho phi(n)=(p-1)*(q-1) không chia hết cho e
# while (p - 1) % e == 0:
#     p = getPrime(1024)

# Ns = []
# # có được mảng 4 số n=p*q;
# while len(Ns) < 4:
# 	q = getPrime(2048)
# 	N = p * q
# 	if (q - 1) % e != 0 and N not in Ns:
# 		Ns.append(N)

flag = b"flaghihi";
#print(flag);
flag += os.urandom(3072 // 8 - 2 - len(flag))
print(flag);
flag = bytes_to_long(flag)

# cts = [pow(flag, e, N) for N in Ns] # vẫn là N cũ
# Ns = [N + int(os.urandom(32).hex(), 16) for N in Ns]
# random.shuffle(Ns)
print(int(os.urandom(32).hex(), 16));

#f = open("output.txt", "w")
# print(f"{Ns = }\n")
# print(f"{cts = }\n")
#f.close()