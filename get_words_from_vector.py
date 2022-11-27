#=================================================================================
#================================ GloVe ==========================================
#=================================================================================
print("Loading GloVe model, this can take some time...")
glv_vector = {}
inv_glv_vector = {}

## the file can be downloaded from https://nlp.stanford.edu/projects/glove/ ##
f = open('/DATA/dushyant_1821cs17/datasets/glove/glove.840B.300d.txt')
for line in f:
    values = line.split()
    word = values[0]
    try:
        coefs = np.asarray(values[1:], dtype='float32')
        glv_vector[word] = coefs
        inv_glv_vector[''.join([str(item) for item in coefs[:15]])] = word
    except ValueError:
        continue
f.close()
print("Completed loading pretrained models.")

inv_glv_vector['0.00.00.00.00.00.00.00.00.00.00.00.00.00.00.0'] = ''


def getWord(vec):
    num_words = len(vec)
    sentence = ' '.join([inv_glv_vector[''.join([str(item) for item in vec[i][:15]])]
                         for i in range(num_words)])

    return ' '.join(sentence.split())


print(getWord(temp))
