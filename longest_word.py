def longest_word(string):
    words=string.split()
    return max(words, key=len)

print(longest_word('ala ma kota a kot ma pas ktory mowi blablabla'))