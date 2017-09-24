import filter as training_set
#Important to work
#Absolutely necessary
#Don't forget this line
from filter import split_into_lemmas

messages = training_set.messages
detector = training_set.get_detector()
print messages['message'][19]
print "Expected: ", messages['label'][19]
print "Actual: ", detector.predict([messages['message'][19]])
