def sum_even(array):
    sum=0
    for i in range(0,len(array)):
        if(i%2==0):
            sum+=array[i]
            print sum,i
    print len(array)
    return sum*array[-1]
  """

        sums even-indexes elements and multiply at the last



    if len(array) == 0: return 0

    return sum(array[0::2]) * array[-1] """

result=sum_even([1,3,5])
print result