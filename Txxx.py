import bs4 as bs
import urllib.request
import re
import nltk
sd=urllib.request.urlopen('https://en.wikipedia.org/wiki/artificial')
article=sd.read()
parse=bs.BeautifulSoup(article,'lxml')
paragraphs=parse.find_all('p')
a=""
for p in paragraphs:
    a+=p.text
a = re.sub(r'\[[0-9]*\]', ' ', a)  
a = re.sub(r'\s+', ' ', a)
formatted_article_text = re.sub('[^a-zA-Z]', ' ',a )  
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
sente=nltk.sent_tokenize(a)
stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}  
for word in nltk.word_tokenize(formatted_article_text):  
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1
maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():  
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
sentence_scores = {}  
for sent in sente:  
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]
import heapq  
summary_sentences = heapq.nlargest(3, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)  
print(summary)                      
