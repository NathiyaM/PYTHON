def compressed_String(text):
	count=1
	lst=[]
	prevstring=''
	for char in text:
		if char!=prevstring:
			if prevstring:
				if (count!=1):
					lst.append(str(count)+prevstring)
				else:
					lst.append(prevstring)
			count=1
			prevstring=char
		else:
			count+=1	
	else:
		if(count!=1):
			lst.append(str(count)+char)
		else:
			lst.append(char)
	string=("".join(lst))
	print len(string)
	return string

def write_originalstring(text):
	f=open("OriginalString.txt",'wb+')
	f.write(text)
	f.close()

def write_compressstring(text):
    f=open("compressedString.txt",'wb+')
    f.write(text)
    f.close()

originaltext='''GGCAGATTCCCCCTAGACCCGCCCGCACCATGGTCAGGCATGCCCCTCCTCATCGCTGGGCACAGCCCAGAGGGTATAAACAGTGCTGGAGGCTGGCGGGGCAGGCCAGCTGAGTCCTGAGCAGCAGCCCAGCGCAGCCACCGAGACACCATGAGAGCCCTCACACTCCTCGCCCTATTGGCCCTGGCCGCACTTTGCATCGCTGGCCAGGCAGGTGAGTGCCCCCACCTCCCCTCAGGCCGCATTGCAGTGGGGGCTGAGAGGAGGAAGCACCATGGCCCACCTCTTCTCACCCCTTTGGCTGGCAGTCCCTTTGCAGTCTAACCACCTTGTTGCAGGCTCAATCCATTTGCCCCAGCTCTGCCCTTGCAGAGGGAGAGGAGGGAAGAGCAAGCTGCCCGAGACGCAGGGGAAGGAGGATGAGGGCCCTGGGGATGAGCTGGGGTGAAC'''

cs=compressed_String(originaltext)
write_originalstring(originaltext)
write_compressstring(cs)
print "Final Compresses String",cs
print "The number of character in original string & compressed string is",len(originaltext),len(cs)
			
