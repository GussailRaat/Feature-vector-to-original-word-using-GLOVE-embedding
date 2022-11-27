import pickle

f = open('path-to-glove-embedding/glove.840B.300d.txt')
gloveDict = {}
for line in f:
    word, *vector = line.split()
    gloveDict[word] = vector
    
vec = gloveDict['hello]
