import re

def get_dict_words(text):
    sentence = []
    comment = text.lower().replace('ё', 'е')
    replaced_comment = re.sub('[^а-яa-z]', ' ', comment)
    for word in replaced_comment.split(' '):
        if word:
            sentence.append(word)
    #if len(sentence) == 0:
    #    print("WTF...NORMALIZATION:" +text)
    return sentence

def normalize_all_data(array):
    return [get_dict_words(X) for X in array]