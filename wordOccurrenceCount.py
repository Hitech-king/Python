from collections import Counter

sentence = input ("Enter the sentence:- ")

words = sentence.lower().split()
word_count = Counter(words)
for word , count in word_count.items():
    print(f"{word}: {count}")