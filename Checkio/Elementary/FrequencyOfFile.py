def removepunctuation(list):
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "
    final_string=""
    for i in list:
        if i not in punctuation:
            final_string=final_string+i
    final_string=final_string.lower()
    print final_string
    return final_string


def count(list):
    newlist={}
    for i in list:
        newlist[i]=newlist.get(i,0)+1
    newlist=dict(sorted(newlist.items()))
    print newlist
    return newlist

def max(dict):
    value=0
    for values in dict.values():
        if (values>value):
            value=values
    return value


def find_key(dict,value):
    for k,v in dict.items():
        if v==value:
            return k
            break


if __name__ == "__main__":
    list="Aaaooo!!!"
    finalstring=removepunctuation(list)
    dictcount=count(finalstring)
    max=max(dictcount)
    result=find_key(dictcount,max)
    print result


