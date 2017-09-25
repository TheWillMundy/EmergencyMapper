import filter as training_set
#Important to work
#Absolutely necessary
#Don't forget this line
from filter import split_into_lemmas

messages = training_set.messages
detector = training_set.get_detector()
test_message = "Houston is still reeling from Harvey's damage. The Trump administration's response? Close the Houston EPA lab."
test_label = "spam"
test_message2 = "Illegal immigration is a problem at least 100x more urgent than Harvey, Irma & every other hurricane since 2005"
test_label2 = "spam"
test_message3 = "Being reminded to pray for all the loss and recovery from Harvey, Irma and Maria #POstables"
test_label3 = "spam"
test_message4 = "If anyone in the Port Arthur area can help, my cousin is trapped at 2320  E 17th street. Four adults and two kids."
test_label4 = "ham"
test_message5 = "Please, my family needs help so much. One Bellaire Road. They have 3 kids and 4 pets and are devastated"
test_label5 = "ham"
print messages['message'][19]
print "Expected: ", messages['label'][19]
print "Actual: ", detector.predict([messages['message'][19]])
print "Expected: ", test_label
print "Actual: ", detector.predict([test_message])
print "Expected: ", test_label2
print "Actual: ", detector.predict([test_message2])
print "Expected: ", test_label3
print "Actual: ", detector.predict([test_message3])
print "Expected: ", test_label4
print "Actual: ", detector.predict([test_message4])
print "Expected: ", test_label5
print "Actual: ", detector.predict([test_message5])
