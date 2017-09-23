import filter as training_set
from filter import split_into_lemmas
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas

messages = training_set.messages
detector = training_set.get_detector()

analyzer = SentimentIntensityAnalyzer()
all_messages = pandas.Index(messages['message'])
for message in messages['message']:
    vs = analyzer.polarity_scores(message)
    compound_score = vs['compound']
    message_index = all_messages.get_loc(message)
    if type(message_index) == int:
        message_label = messages['label'][message_index]
        expected_label = message_label
        predicted_label = detector.predict([message])
        # if (expected_label != predicted_label):
        #     print "Text: {:-<65}, Senti: {}".format(message, str(compound_score))
        #     print "Expected: {}, Actual: {}".format(expected_label, predicted_label)
        #     # print("{:-<65} {}".format(message, str(vs)))
        #     print "-------"
