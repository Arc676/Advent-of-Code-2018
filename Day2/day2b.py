def diffs(a, b):
	numdiffs = 0
	positions = []
	for i in range(len(a)):
		if a[i] != b[i]:
			numdiffs += 1
			positions.append(i)
	return numdiffs, positions

file = open("input", 'r')
ids = [line.strip() for line in file.readlines()]
file.close()
for search in ids:
	matches = list(filter(lambda boxid: diffs(boxid, search)[0] == 1, ids))
	if len(matches) != 0:
		diff = diffs(search, matches[0])
		dpos = diff[1][0]
		print diff
		print search
		print matches[0]
		print search[:dpos] + search[dpos + 1:]
		break
