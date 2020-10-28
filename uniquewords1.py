#!/usr/bin/env python3

import string
import sys

words = {}
strip = string.whitespace + string.punctuation + string.digits + "\"'"
for filename in sys.argv[1:]:
    with open(filename, 'r' , encoding='utf-8') as file:
        for line in file:
            for word in line.lower().split():
                words1=list(words.items())
                words1.sort(key=lambda i : i[1], reverse=True)
                word = word.strip(strip)
                if len(word) > 2:
                    words[word] = words.get(word, 0) + 1

for i in words1 :
    print(i[0], ':', i[1])
