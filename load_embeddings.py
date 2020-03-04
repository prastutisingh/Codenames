import numpy as np
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Download BERT embeddings into a dictionary
from bert_serving.client import BertClient
client = BertClient()

bert_embeddings = {}
glove_embeddings = {}

with open("./top_50000.txt", 'r', encoding="utf8") as f:
    for line in f:
        values = line.split()
        word = values[0]
        tag = nltk.pos_tag([word])[0][1]
        if len(word) > 1 and word.isalpha() and tag in ['NN', 'NNP']:
            # add to bert_embeddings
            vector_bert = client.encode([word])
            bert_embeddings[word] = vector_bert[0]

            # add to glove_embeddings
            vector_glove = np.asarray(values[1:], "float32")
            glove_embeddings[word] = vector_glove

# Save dictionaries
np.save('bert.npy', bert_embeddings)
np.save('glove.npy', glove_embeddings)