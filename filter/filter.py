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

#General Functions
def open_data():
    return pandas.read_csv('./data/SMSSpamCollection', sep="\t", quoting=csv.QUOTE_NONE, names=["label", "message"])

#General Variables
    #Message 4 for testing
messages = open_data()
message4 = messages['message'][3]

def split_into_lemmas(message):
    """
    Splits
    """
    message = unicode(message, 'utf8').lower()
    words = TextBlob(message).words
    #taking base form of each word -> base form being 'lemma'
    return [word.lemma for word in words]

def adjust_training_size(messages):
    msg_train, msg_test, label_train, label_test = \
        train_test_split(messages['message'], messages['label'], test_size=0.2)
    return msg_train, label_train

#MultinomialNB Functions
# bow_transformer = CountVectorizer(analyzer=split_into_lemmas).fit(messages['message'])
# print len(bow_transformer.vocabulary_)

# messages_bow = bow_transformer.transform(messages['message'])
# print 'sparse matrix shape:', messages_bow.shape
# print 'number of non-zeros:', messages_bow.nnz
# print 'sparsity: %.2f%%' % (100.0 * messages_bow.nnz / (messages_bow.shape[0] * messages_bow.shape[1]))
#
# tfidf_transformer = TfidfTransformer().fit(messages_bow)
#
# messages_tfidf = tfidf_transformer.transform(messages_bow)

#     #Actual Detector using MultinomialNB
# spam_detector = MultinomialNB().fit(messages_tfidf, messages['label'])
# print "Expected: " + messages['label'][0]
# print "Actual: " + spam_detector.predict(messages_tfidf)[0]
# #All Messages
# all_predictions = spam_detector.predict(messages_tfidf)
# #Accuracy Testing
# print "Accuracy: ", accuracy_score(messages['label'], all_predictions)
# print "Confusion Matrix: \n", confusion_matrix(messages['label'], all_predictions)
# print "(row=expected, col=predicted)"

# def multinomialnb_accuracy(messages):
#     """
#     Uses sklearn Pipeline to create training model with MultinomialNB Classification, determines cross value scores
#     focusing on accuracy
#
#     Returns accuracy score of model
#     """
#     #Pipeline Detector
#     msg_train, label_train = adjust_training_size(messages)
#     pipeline = Pipeline([
#         ('bow', CountVectorizer(analyzer=split_into_lemmas)),  # strings to token integer counts
#         ('tfidf', TfidfTransformer()),  # integer counts to weighted TF-IDF scores
#         ('classifier', MultinomialNB()),  # train on TF-IDF vectors w/ Naive Bayes classifier
#     ])
#
#     scores = cross_val_score(pipeline,  # steps to convert raw messages into models
#                              msg_train,  # training data
#                              label_train,  # training labels
#                              cv=10,  # split data randomly into 10 parts: 9 for training, 1 for scoring
#                              scoring='accuracy',  # which scoring metric?
#                              n_jobs=-1,  # -1 = use all cores = faster
#                              )
#     print scores
#         #Mean and Standard Deviation
#     print scores.mean(), scores.std()
#     return scores

#SVM Functions
#Testing with SVM classifier
def svm_accuracy(messages):
    """
    Uses sklearn Pipeline to create training model with SVM Classification, creates an SVM grid
    which can make predictions and filter out messages.

    Saves detector into cPickle file for later use
    Returns accuracy score obtained by the detector
    """
    # Only used for development:
    # msg_train, label_train = adjust_training_size(messages)
    msgs = messages['message']
    labels = messages['label']
    pipeline_svm = Pipeline([
        ('bow', CountVectorizer(analyzer=split_into_lemmas)),
        ('tfidf', TfidfTransformer()),
        ('classifier', SVC()),  # <== change here
    ])

    #Parameters for SVM Pipeline
    param_svm = [
      {'classifier__C': [1, 10, 100, 1000], 'classifier__kernel': ['linear']},
      {'classifier__C': [1, 10, 100, 1000], 'classifier__gamma': [0.001, 0.0001], 'classifier__kernel': ['rbf']},
    ]

    grid_svm = GridSearchCV(
        pipeline_svm,
        param_grid=param_svm,
        refit=True,
        scoring='accuracy',
        n_jobs=-1,
        cv=StratifiedKFold(labels, n_folds=5),  # what type of cross validation to use
    )

    svm_detector = grid_svm.fit(msgs, labels)
    #Saves SVM Detector to File
    save_detector(svm_detector)
    return svm_detector.grid_scores_

def save_detector(detector):
    """
    Saves the Trained Model into a cPicle file for later use
    """
    #Serialization
    with open('sms_spam_detector.pkl', 'wb') as fout:
        cPickle.dump(detector, fout)

    #Reload the SVM Detector
    svm_detector_reloaded = cPickle.load(open('sms_spam_detector.pkl'))

def get_detector():
    return cPickle.load(open('sms_spam_detector.pkl'))
#Exported Variables
# svm_detector = cPickle.load(open('sms_spam_detector.pkl'))

# svm_accuracy(messages)
#SVM Test
# svm_accuracy(messages)
# #Test prediction of SVM Detector
# print 'before:', svm_detector.predict([message4])[0]
# print 'after:', svm_detector_reloaded.predict([message4])[0]

# Grouping Messages
# print messages.groupby('label').describe()

#Length of Messages
# messages['length'] = messages['message'].map(lambda text: len(text))
# print messages.head()
