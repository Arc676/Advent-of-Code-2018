// Copyright (c) 2018 Alessandro Vinciguerra

// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:

// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.

// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
	if (argc != 2) {
		return 1;
	}
	int freq = 0;
	int reached[1000000];
	int fcount = 1;
	FILE* input = fopen(argv[1], "r");
	char line[10];
	while (1) {
		while (fgets(line, sizeof(line), input)) {
			freq += (int)strtol(line, (char**)NULL, 0);
			reached[fcount++] = freq;
			for (int i = 0; i < fcount - 1; i++) {
				if (freq == reached[i]) {
					printf("Duplicate frequency (index %d): %d\n", fcount, freq);
					fclose(input);
					return 0;
				}
			}
		}
		rewind(input);
	}
}