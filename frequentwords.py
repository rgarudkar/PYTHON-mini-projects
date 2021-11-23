words = []
with open(r"C:\Users\ramgo\OneDrive\Desktop\frequentwords.txt", "r") as f:
    for line in f:
        words.extend(line.split())

from collections import Counter
counts = Counter(words)
Top5 = counts.most_common(5) #returns top5 common words
print(Top5)