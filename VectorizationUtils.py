import gensim
from gensim import matutils
from numpy.core.multiarray import dot

print("LOAD VECS...")
w2v_fpath = "C:\javaTest\kaggleData/tenth.norm-sz500-w7-cb0-it5-min5.w2v"
w2v = gensim.models.KeyedVectors.load_word2vec_format(w2v_fpath, binary=True, unicode_errors='ignore')
w2v.init_sims(replace=True)

def contains_in_dict(word):
    return word in w2v.wv.vocab

def vectorize_array(array):
    arr_vec = []
    for word in array:
        vec = vectorize_word(word)
        if vec:
            arr_vec.append(vec)
        else:
            print("WORD NOT IN DICT... " + word)
    return arr_vec

def vectorize_word(word):
    if word in w2v.wv.vocab:
        return w2v.wv[word]

def similarity(w1,w2):
    return w2v.wv.similarity(w1,w2)

def distance(vec1, vec2):
    return dot(matutils.unitvec(vec1), matutils.unitvec(vec2))