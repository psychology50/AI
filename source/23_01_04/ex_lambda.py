import re
from collections import Counter

file = open(fname, "r")
contents = file.read()

freq = {}
for S in re.split('[.?!]', contents):
    words = sorted(filter(lambda w: w not in stop_words and len(w) > minlen, set(S.lower().split())))
    for x in range(len(words) - 1):
        for y in range(x+1, len(words)):
            freq[(words[x], words[y])] = freq.get((words[x], words[y]), 0) + 1

c = Counter(freq)
c.most_common(5)