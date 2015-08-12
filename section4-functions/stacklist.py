def stackadd(list,data):
	list = list.append(data)
	return list
def stackretrieve(list):
	list=list.pop()
	return list
if __name__=='__main__' :
	list=[1,2,3]
	while list:
		input = raw_input("enter the operation to do in the list:\n 1.append\n2.retrieve\n3.exit\n")
		if(input=='append'or input=='1'):
			data = int(raw_input("enter the number to append in the list"))
			stackadd(list,data)
			print "The list after appended is :",list
			continue
		elif(input=='retrieve'or input=='2'):
			stackretrieve(list)
			print "The list after retreived is :",list
			continue	
		else:
			break
print "Operation Exit"
print "The current list is",list
