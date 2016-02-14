'''def weak_point(list):
    sum_of_rows = []
    sum_of_cols = []
    for i in list:
        result = sum(i)
        sum_of_rows.append(result)
    print(sum_of_rows)
    result=0
    for col in range(0,len(list)):
        for row in range(0,len(list)):
            result=result+list[row][col]
        sum_of_cols.append(result)
        result=0
    print(sum_of_cols)
    min_row = min(sum_of_rows)
    min_col = min(sum_of_cols)
    for i in range(0,len(sum_of_rows)):
        if sum_of_rows[i] == min_row:
            break
    for j in range(0,len(sum_of_cols)):
        if sum_of_cols[j] == min_col:
            break
    print(i,j)
'''
# Alternate Solution
def weak_point(list):
    sum_of_rows = []
    sum_of_cols = []
    result = 0
    result1 = 0
    for col in range(0,len(list)):
        for row in range(0,len(list)):
            result1 = result1 + list[col][row]
            result = result + list[row][col]
        sum_of_cols.append(result)
        sum_of_rows.append(result1)
        result=0
        result1=0
    print(sum_of_cols,sum_of_rows)
    min_row = sum_of_rows.index(min(sum_of_rows))
    min_col = sum_of_cols.index(min(sum_of_cols))

    print(min_row,min_col)


weak_point([[7, 2, 7, 2, 8], [2, 9, 4, 1, 7], [3, 8, 6, 2, 4], [2, 5, 2, 9, 1], [6, 6, 5, 4, 5]])



