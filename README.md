# Usage of GLOVE-embedding

## Get the feature vector from word
### Run getVector.py file


## Get the word from feature vector
### Run getWord.py file
* we have to give the list of vectors. For example, if there are 7 words (300 dim each) in a sentence then list will have shape (7, 300).
* This code will first load the pretrained glove embedding and then return the sentence according to your vector (vec).
* Please note that, vec should be 2D, i.e., number of words, dimension (e.g. 300)
