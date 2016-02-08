




def count_inversion(sequence):
    seq=list(sequence)
    count=0
    for i in range(0,len(seq)):
        for j in range(i+1,len(seq)):
            if(seq[i]<seq[j]):
                continue
            else:

                temp=seq[i]
                seq[i]=seq[i+1]
                seq[i+1]=temp
                count=count+1


    print seq
    print count






if __name__ == "__main__":
    tuple=(5,3,2,1,0)
    count_inversion(tuple)