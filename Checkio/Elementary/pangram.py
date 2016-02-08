""" A pangram  or holoalphabetic sentence for a given alphabet is a sentence
 using every letter of the alphabet at least once.
 Perhaps you are familiar with the well known pangram "The quick brown fox jumps over the lazy dog".
For this mission, we will use the latin alphabet (A-Z).
You are given a text with latin letters and punctuation symbols.
 You need to check if the sentence is a pangram or not. Case does not matter.
Input: A text as a string.
Output: Whether the sentence is a pangram or not as a boolean.
Precondition:"""

import string
def check_pangram(text):
    text=string.uppercase
    for ch in string.uppercase:
        if( ch in text):
            result='True'
            continue
        else:
            result='False'
            result='False'
            break

    return result

result=check_pangram("The quick brown fox jumps over the lazy dog")
result1=check_pangram("ABCDE")
print result1
print result