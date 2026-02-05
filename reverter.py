print("\033[40;37m\ngive the file .txt reverter ? ")
a = input().strip()

print("\033[40;37m\ngive the file .dat reverter ? ")
b = input().strip()

with open(a, "rb") as f:
    data = f.read()

out = bytearray()

for byte in data:
    out.insert(0, (~byte) & 0xFF)   # NOT + reverse

with open(b, "wb") as f:
    f.write(out)