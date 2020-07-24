import numpy as np

"""
Command to run the DAN on movie dataset:
python neural_sentiment_classifier.py --model DAN --word_vecs_path data/glove.6B.50d-relativized.txt --train_path train.txt --dev_path dev.txt --blind_test_path test.txt
"""


new_file = open("clean_data.txt", "w")

with open("takehome1.txt", 'r') as data:
	lines = data.readlines()
	for line in lines:
		if line == "\n":
			continue
		splits = line.split('\t')
		sentiment = splits[0]
		sentence = splits[1][1:-2]
		new_file.write("{label}\t{sentence}\n".format(label=sentiment, sentence=sentence))

train_file = open("train.txt", 'w')
dev_file = open("dev.txt", 'w')
test_file = open("test.txt", 'w')

with open("clean_data.txt", 'r') as data:
	lines = data.readlines()
	idxs = np.array([i for i in range(len(lines))])
	np.random.shuffle(idxs)
	np_splits = np.split(idxs, [int(.8 * len(idxs)), int(.9 * len(idxs))])
	train_idxs = np_splits[0]
	dev_idxs = np_splits[1]
	test_idxs = np_splits[2]

	for i in train_idxs:
		train_file.write(lines[i])

	for i in dev_idxs:
		dev_file.write(lines[i])

	for i in test_idxs:
		test_file.write(lines[i])
