import gensim
import  VectorizationUtils

def words_contains_in_text_OR_AND(text_words_array, list_words_seq):
    for seq in list_words_seq:
        if words_contains_in_text_AND(text_words_array, seq):
            return True
    return False

def words_contains_in_text_AND(text_words_array, words_seq):
    for seq in words_seq:
        if not word_contains_in_text(text_words_array, seq):
            return False
    return True

def word_contains_in_text(text_words_array, word_seq):
    word_seq = word_seq.lower()
    for word in text_words_array:
        if VectorizationUtils.contains_in_dict(word) and VectorizationUtils.contains_in_dict(word_seq):
            score = VectorizationUtils.similarity(word, word_seq)
            if score > 0.55:
                return True
        elif word == word_seq: return True
    return False