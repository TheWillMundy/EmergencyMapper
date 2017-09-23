import matplotlib.pyplot as plt
import csv
from textblob import TextBlob
import pandas
import sklearn
import cPickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC, LinearSVC
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import StratifiedKFold, cross_val_score, train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.learning_curve import learning_curve

# messages = [line.rstrip() for line in open('./data/SMSSpamCollection')]

messages = pandas.read_csv('./data/SMSSpamCollection', sep="\t", quoting=csv.QUOTE_NONE, names=["label", "message"])
print messages

# Grouping Messages
print messages.groupby('label').describe()

#Length of Messages
messages['length'] = messages['message'].map(lambda text: len(text))
print messages.head()

def split_into_lemmas(message):
    message = unicode(message, 'utf8').lower()
    words = TextBlob(message).words
    #taking base form of each word -> base form being 'lemma'
    return [word.lemma for word in words]

# #Adjust Testing Data
# msg_train, msg_test, label_train, label_test = \
#     train_test_split(messages['message'], messages['label'], test_size=0.2)
#
# pipeline = Pipeline([
#     ('bow', CountVectorizer(analyzer=split_into_lemmas)),  # strings to token integer counts
#     ('tfidf', TfidfTransformer()),  # integer counts to weighted TF-IDF scores
#     ('classifier', MultinomialNB()),  # train on TF-IDF vectors w/ Naive Bayes classifier
# ])

message4 = messages['message'][3]
print message4

bow_transformer = CountVectorizer(analyzer=split_into_lemmas).fit(messages['message'])
print len(bow_transformer.vocabulary_)

bow4 = bow_transformer.transform([message4])
print bow4
print bow4.shape


messages_bow = bow_transformer.transform(messages['message'])
print 'sparse matrix shape:', messages_bow.shape
print 'number of non-zeros:', messages_bow.nnz
print 'sparsity: %.2f%%' % (100.0 * messages_bow.nnz / (messages_bow.shape[0] * messages_bow.shape[1]))

tfidf_transformer = TfidfTransformer().fit(messages_bow)
tfidf4 = tfidf_transformer.transform(bow4)
print tfidf4

print tfidf_transformer.idf_[bow_transformer.vocabulary_['u']]
print tfidf_transformer.idf_[bow_transformer.vocabulary_['university']]

messages_tfidf = tfidf_transformer.transform(messages_bow)
print messages_tfidf.shape

#One Message
spam_detector = MultinomialNB().fit(messages_tfidf, messages['label'])
print "Expected: " + messages['label'][0]
print "Actual: " + spam_detector.predict(messages_tfidf)[0]
#All Messages
all_predictions = spam_detector.predict(messages_tfidf)
#Accuracy Testing
print "Accuracy: ", accuracy_score(messages['label'], all_predictions)
print "Confusion Matrix: \n", confusion_matrix(messages['label'], all_predictions)
print "(row=expected, col=predicted)"
