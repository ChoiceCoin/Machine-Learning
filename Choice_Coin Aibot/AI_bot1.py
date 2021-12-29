import nltk
from nltk.stem.lancaster import LancasterStemmer
from numpy.core.records import array
stemmer = LancasterStemmer()

# things we need for Tensorflow
import numpy as np
import tflearn
import tensorflow as tf
import random


# import our chat-bot intents file
import json
with open('intents.json') as file:
    data = json.load(file)

words = []
labels = []
docs_x = []
docs_y = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intent["tag"])
    if intent['tag'] not in labels:
        labels.append(intent['tag'])

words = [stemmer.stem(w.lower()) for w in words if w != '?']
words = sorted(list(set(words)))

labels = sorted(labels)
print(words)

training = []
output = []

out_empty = [0 for _ in range(len(labels))]

for x,docs in enumerate(docs_x):
    bag = []

    wrds = [stemmer.stem(w) for w in docs]
    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)

training = np.array(training)
output = np.array(output)


net = tflearn.input_data(shape = [None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation = 'softmax')
net = tflearn.regression(net)
model = tflearn.DNN(net)

try:
    model.load('model.tflearn')
except:
    model.fit(training,output, n_epoch= 1000, batch_size=8, show_metric = True)
    model.save('model.tflearn')

def bag_of_words(s,words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for cw in s_words:
        for i, w in enumerate(words):
            if w == cw:
                bag[i] = (1)

    return np.array(bag)


def chat():
    print("the bot is listening (type quit to stop chatting with the bot)")
    while True:
        inp = input('You: ')
        if inp.lower() == 'quit':
            break
        result = model.predict([bag_of_words(inp,words)])
        result_index = np.argmax(result)
        tag = labels[result_index]
        if result_index > 0.7:
            for ts in data['intents']:
                if ts['tag'] == tag:
                    responses = ts['responses']
            print(random.choice(responses))
        else:
            print("sorry i didn't get that try being more specific but for more information you can head on to the choice coin website https://choice-coin.com/")

chat()