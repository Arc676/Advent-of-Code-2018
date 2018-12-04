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

import datetime
import re

file = open("input", 'r')
entries = []
for line in file.readlines():
	match = re.match(r'\[(.+)\] (.+)', line)
	timestamp, event = match.groups()
	timestamp = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
	if event == "falls asleep":
		event = "f"
	elif event == "wakes up":
		event = "w"
	else:
		match = re.match(r'Guard #(\d+) begins shift', event)
		event = int(match.groups()[0])
	entries.append((timestamp, event))
file.close()

currentGuard = -1
lastSleep = -1
sleepTimes = {}
for entry in sorted(entries, key=lambda entry: entry[0]):
	timestamp, event = entry
	if event == "f":
		lastSleep = timestamp.minute
	elif event == "w":
		wake = timestamp.minute
		for minute in range(lastSleep, wake):
			sleepTimes[currentGuard][minute] = sleepTimes[currentGuard].get(minute, 0) + 1
	else:
		currentGuard = event
		if currentGuard not in sleepTimes:
			sleepTimes[currentGuard] = {}
sleepyGuards = sorted(sleepTimes.keys(), key=lambda guard: sum(sleepTimes[guard].values()))
guard = sleepTimes[sleepyGuards[-1]]
bestMin = max(guard.keys(), key=lambda minute: guard[minute])
print "Guard ID:", sleepyGuards[-1]
print "Sleepiest minute:", bestMin
print "Product:", (sleepyGuards[-1] * bestMin)
