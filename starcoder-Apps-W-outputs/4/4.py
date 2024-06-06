

def get_sentence_language(sentence):
    if sentence.endswith('po'):
        return 'FILIPINO'
    elif sentence.endswith('desu') or sentence.endswith('masu'):
        return 'JAPANESE'
    elif sentence.endswith('mnida'):
        return 'KOREAN'
    else:
        raise ValueError('Invalid sentence: {}'.format(sentence))
