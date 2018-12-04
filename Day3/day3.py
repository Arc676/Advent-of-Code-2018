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

import re

fabric = [['.' for _ in range(1000)] for _ in range(1000)]
doubles = 0
file = open("input", 'r')
for line in file.readlines():
	match = re.match(r'#\w+ @ (\d+),(\d+): (\d+)x(\d+)', line)
	x, y, dx, dy = match.groups()
	x, y, dx, dy = int(x), int(y), int(dx), int(dy)
	for xco in range(x, x + dx):
		for yco in range(y, y + dy):
			if fabric[yco][xco] == '.':
				fabric[yco][xco] = '+'
			elif fabric[yco][xco] == '+':
				doubles += 1
				fabric[yco][xco] = 'X'
file.close()
print "Doubles:", doubles
