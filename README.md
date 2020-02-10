# Codenames

## Data Collection
What size vocabulary should we use?
- 1000
- 5000
- 10000
- 20000
- 50000

Number of examples? 

Choice of embeddings (if time)
- GloVe
- BERT/ELMO

## Model Parameters
Choice of clue generating function: 
- Cosine distance (is this differentiable?) 
  - weights on bad word, death word
- v.T * w
- something else???

Loss 
- Rank choice
- Cross-entropy
