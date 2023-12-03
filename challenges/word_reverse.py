"""
    Write a function that takes a sentence as input and returns
    the words reversed (not the characters within each word)
    e.g. "Hello World" -> "World Hello"
"""
print('Enter a sentence you wish to have reversed')
sentence = input('> ')


def reverse_sentence(sent):
    list_sent = sent.split()[::-1]
    rev_sent = ' '.join(list_sent)
    print(rev_sent.capitalize())


reverse_sentence(sentence)
