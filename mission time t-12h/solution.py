n = input()
s = list(raw_input())
k = input() % 26
temp = map(lambda x: ord(x), s)
for i in range(len(s)):
    if 65 <= temp[i] <= 90:
        temp[i] = 65 + ((temp[i] - 65) + k) % 26
    elif 97 <= temp[i] <= 122:
        temp[i] = 97 + ((temp[i] - 97) + k) % 26
print "".join(map(chr, temp))