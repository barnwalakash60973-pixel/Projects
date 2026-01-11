def determinant(mat):

    n1 = len(mat[0])
    n2 = len(mat)
    if n1 != n2:
        return ValueError("Please enter square matrix")
    else:    
        det = 0

        if n1 == 2:
            det += (mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0])
            print(f'The determinant of the matrix is:{det}')


        

        elif n1 == 3:
            j = 1
            k = n1 -1
            for i in range(n2):
                p = (-1) ** i
                if i == (n1 - 1):
                    k = 1
                
                det += mat[0][i]*(mat[1][j]*mat[2][k] - mat[1][k]*mat[2][j]) * p
                j = 0
            print('The determinant of the matrix is: ',det)


        else:
            print('Please enter matrix must be 2*2 or 3*3 only')
        
        
        
mat = [[2,1,3],[2,3,3],[1,2,3]]
determinant(mat)


