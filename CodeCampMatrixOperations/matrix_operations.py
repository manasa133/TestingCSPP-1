def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''

    if (len(m1)!=len(m2)):
        return "Error: Matrix shapes invalid for addition"
    for i,j in zip(m1,m2):
        if(len(i)!= len(j)):
          return "Error: Matrix shapes invalid for addition"
    result =[]  
    for i in m1 :
        row =[]
        colNum = 0
        add = 0
        for k in range(len(i)):
            for q in m2:
                add += q[colNum] * i[colNum]
            row.append(add)
        result.append(row)
    return result

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if (len(m1)!=len(m2)):
        return "Error: Matrix shapes invalid for addition"
    for i,j in zip(m1,m2):
        if(len(i)!= len(j)):
          return "Error: Matrix shapes invalid for addition"
    result =[]  

    for i,j in zip(m1,m2):
        row =[]
        for p,q in zip(i,j):
            row.append(p+q)
        result.append(row)
    # print(result)
    return result
        


def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    rows,columns = [int(i) for i in raw_input().split(",")]
    matrix =[]
    for i in range(rows):
        temp = [int(i) for i in raw_input().split(" ")]
        matrix.append(temp)
    return matrix

   

def main():
    # read matrix 1


    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
   
    matrix_1 = read_matrix()
    # print(matrix_1)
    matrix_2 = read_matrix()
    # print(matrix_2)
    result = add_matrix(matrix_1,matrix_2)
    print(result)

    result = mult_matrix(matrix_1,matrix_2)
    print(result)




if __name__ == '__main__':
    main()
