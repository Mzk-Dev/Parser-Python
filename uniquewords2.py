#!/usr/bin/env python3

import string
import sys

words = {}
strip = string.whitespace + string.punctuation + string.digits + "\"'"
for filename in sys.argv[1:]:
    with open(filename,'r',encoding='utf-8' ) as file:
        for line in file:   #построчно считываем строки
            for word in line.lower().split():
                word = word.strip(strip)
                if len(word) > 2:
                    words[word] = words.get(word, 0) + 1#Добавляем в существуещему ключу +1 , или создаем ключ со значением 1

def dict_sorted_by_value(item):
    return item[1], item[0]

print(sorted(word.items(), key=dict_sorted_by_value))
