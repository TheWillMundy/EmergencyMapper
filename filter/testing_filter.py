import filter as training_set
#Important to work
#Absolutely necessary
#Don't forget this line
from filter import split_into_lemmas

messages = training_set.messages
detector = training_set.get_detector()
print "Expected: ", messages['label'][2]
print "Actual: ", detector.predict([messages['message'][2]])
