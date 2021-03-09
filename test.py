from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
stopw=stopwords.words('english')


tocsvlist=[["questions","answers","keywords"]]
import csv
import json
with open('question.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform([row[0]])
        keywords=[x for x in vectorizer.get_feature_names() if x not in stopw]
        tocsvlist.append([row[0],row[1],keywords])


with open('keywords.csv', 'w', newline='',encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(tocsvlist)

