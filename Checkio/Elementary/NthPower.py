'''def index_power(array, n):

    try: return array[n] ** n

    except IndexError: return -1 '''

def index_power(array, n):

    return array[n] ** n if n < len(array) else -1

result=index_power([1,2,3,4],3)
print result
result=index_power([0],0)
print result