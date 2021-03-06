def count_words(text, words):

    count=0

    for w in words:

        if w in text.lower():

            count+=1



    return count

​

​

if __name__ == '__main__':

    #These uu"1sserts" using only for self-checking and not necessary for auto-testing

    assert count_words(u"How aresjfhdskfhskd you?", {u"how", u"are", u"you", u"hello"}) == 3, "Example"

    assert count_words(u"Bananas, give me bananas!!!", {u"banana", u"bananas"}) == 2, "BANANAS!"

    assert count_words(u"Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",

                       {u"sum", u"hamlet", u"infinity", u"anything"}) == 1, "Weird text


# alternative solution
'''
def count_words(text, words):

    return sum(w in text.lower() for w in words)

​

​

if __name__ == '__main__':

    #These "asserts" using only for self-checking and not necessary for auto-testing

    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"

    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"

    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",

                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
                       '''
