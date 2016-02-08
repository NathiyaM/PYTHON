import string
def safepassword(data):
    if len(data)<10:
        return False
    if string.contains(data.upper()):

            return True
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    input=('aaaaaaaaaaa')
    print(safepassword(input))