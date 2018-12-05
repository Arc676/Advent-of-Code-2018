# Copyright (c) 2018 Alessandro Vinciguerra

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

def abs(x):
	if x < 0:
		return -x
	return x

def letterDist(a, b):
	return abs(ord(a) - ord(b))

def react(pairs, remove):
	caseSwitch = ord('a') - ord('A')
	pairCount = len(pairs)
	pos = 0
	while pos < pairCount - 1:
		if pairs[pos].lower() == remove:
			pairs.pop(pos)
			pairCount -= 1
			pos -= 1
		elif letterDist(pairs[pos], pairs[pos + 1]) == caseSwitch:
			pairs.pop(pos)
			pairs.pop(pos)
			pairCount -= 2
			if pos > 0:
				pos -= 1
		else:
			pos += 1
	return pairCount

file = open("input", 'r')
pairs = list(file.read().strip())
file.close()

shortest = sorted(
	[react(pairs[:], chr(remove)) for remove in range(ord('a'), ord('z') + 1)]
)
print "Shortest chain:", shortest[0]
