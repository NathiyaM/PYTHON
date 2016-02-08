def eliminateNonUniqueElement(list):
    newlist={}
    for i in list:
        newlist[i]=newlist.get(i,0)+1
    for k,v in newlist.items():
        if (v==1):
            list.remove(k)
    return list
#return [r for i in list if list.count(i)>1]




if __name__ == "__main__":
    list=[1,2,3,1,3]
    result=eliminateNonUniqueElement(list)
    print(result)


#return [r for i in list if list.count(i)>1]