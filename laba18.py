stopWords = ["hallo", "klempner", "das", "ist", "fantastisch", "fluggegecheimen"]

lets = {}
countLet = 0

for let in range(97, 123):
    lets[chr(let)] = 0

for word in stopWords:
    for let in word:
        lets[let] += 1
        countLet += 1

stopWord = input("Введите стоп слово: ")

chance = 1
for let in stopWord:
    chance *= lets[let] / countLet

print(chance)