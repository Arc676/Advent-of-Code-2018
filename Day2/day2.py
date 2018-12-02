file = open("input", 'r')
no2s = 0
no3s = 0
for line in file.readlines():
	letters = {x : 0 for x in "abcdefghijklmnopqrstuvwxyz"}
	for letter in line.strip():
		letters[letter] += 1
	if 2 in letters.values():
		no2s += 1
	if 3 in letters.values():
		no3s += 1
file.close()
print "Checksum: ", no2s * no3s
