# Feature-vector-to-original-word-using-GLOVE-embedding
Get the original word from feature vector using GLOVE embedding

## Run getWord.py file
### we have to give the list of vectors. For example, if there are 7 wprds (300 dim each) in a sentence then list will have shape (7, 300).
### This code will first load the pretrained glove embedding and then return the sentence according to your list.

### Please note that, list should be 2D, i.e., number of words, dimension of each word (e.g. 300)
