OPERATION_NAMES = ("conjunction", "disjunction",

                   "implication", "exclusive",

                   "equivalence")

​

​

def boolean(x, y, operation):

    z = 0

    if operation == OPERATION_NAMES[0]:

        z = x and y

    if operation == OPERATION_NAMES[1]:

        z = x or y

    if operation == OPERATION_NAMES[2]:

        z = not(x) or y

    if operation == OPERATION_NAMES[3]:

        z = (x and not y) or (not x and y)

    if operation == OPERATION_NAMES[4]:

        z = not ((x and not y) or (not x and y))

    return z

​

​

if __name__ == '__main__':

    # These "asserts" using only for self-checking

    # and not necessary for auto-testing

    assert boolean(1, 0, u"conjunction") == 0, "and"

    assert boolean(1, 0, u"disjunction") == 1, "or"

    assert boolean(1, 1, u"implication") == 1, "material"

    assert boolean(0, 1, u"exclusive") == 1, "xor"

    assert boolean(0, 1, u"equivalence") == 0, "same?"
