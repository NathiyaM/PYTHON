
def checkio(data):
    if len(data)==0: return 0
    return data[0]+checkio(data[1:])

data=[1,2,3,4]
result =checkio(data)
print(result)