import csv
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import json
from nltk.corpus import stopwords
STOPW=stopwords.words('english')



class BOT:
    def find_keyword(text):
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform([text])
        keywords=[x for x in vectorizer.get_feature_names() if x not in STOPW]
        return keywords
        
    def get_file_data(filename):
        with open(filename, 'r') as file:
            filedata = list(csv.reader(file))
        return filedata

    def get_file_data_key2(lh):
        keyshai=[]
        for row in lh:
            key=BOT.find_keyword(row[0])
            keyshai.append(key)
        return keyshai

    def common_member(a, b): 
        d=[x for x in a if x in b]
        return d[::-1]
        




