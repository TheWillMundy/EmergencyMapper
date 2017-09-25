import filter as training_set
#Important to work
#Absolutely necessary
#Don't forget this line
from filter import split_into_lemmas
import pandas
import csv

messages = training_set.messages
detector = training_set.get_detector()

def data_open():
    return pandas.read_csv('./data/testing_data.txt', sep="\t", quoting=csv.QUOTE_NONE, names=["label", "message"])

testing_data = data_open()
expect_predict = []
counter = 0
corrects = 0

for testing_msg in testing_data['message']:
    message_index = counter
    if type(message_index) == int:
        message_label = testing_data['label'][message_index]
        expected_label = message_label
        predicted_label = detector.predict([testing_msg])
        print "Expected", expected_label
        print "Predicted", predicted_label
        if expected_label == predicted_label:
            corrects += 1
    counter += 1

print "Number model got correct: " + str(corrects) + " out of " + str(counter)
