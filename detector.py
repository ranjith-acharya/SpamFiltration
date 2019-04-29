import pickle as c
import os
from collections import Counter
from sklearn.naive_bayes import MultinomialNB

def load(clf_file):
    with open('text-classifier.mdl', 'rb') as f:
        clf = c.load(f)
    return clf

def make_dict():
	direc = "emails/"
	files = os.listdir(direc)

	emails = [direc + email for email in files]

	words = []
	c = len(emails)

	for email in emails:
		f = open(email)
		blob = f.read()
		words += blob.split(" ")
		print (c)
		c = c - 1

	for i in range(len(words)):
		if not words[i].isalpha():
			words[i] = ""

	dictionary = Counter(words)
	del dictionary[""]
	return dictionary.most_common(3000)

clf = load("text-classifier.pkl")
d = make_dict()

features = []
inp = input("Enter to Classify : ")

for word in d:
    features.append(inp.count(word[0]))

res = clf.predict([features])
print (["Not Spam!", "Spam!"][res[0]])