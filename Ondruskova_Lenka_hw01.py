import json

dictionary = {}

with open("alice.txt", encoding="utf-8") as inputfile:
    for line in inputfile:
        words = line.lower().strip("\n").split(" ")
        for word in words:
            for letter in word:
                if letter in dictionary.keys():
                    dictionary[letter] = dictionary[letter] + 1
                else:
                    dictionary[letter] = 1

with open("hw01_output.json", mode="w", encoding="utf-8") as file:
    json.dump(dictionary, file, indent=4, ensure_ascii=False, sort_keys=True)
