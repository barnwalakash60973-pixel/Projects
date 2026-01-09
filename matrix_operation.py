def matrix_transpose(mat1):
#check matricx is transpose or not


    mat2 = []
    n1 = len(mat1[0])               #Number of columns
    n2 = len(mat1)                  #number of rows

    for i in range(n1):                   
        row = []

        for j in range(n2):
            row.append(mat1[j][i])
        
        mat2.append(row)

    return mat2

mat1 = [[1,4,0],[-3,6,8]]

result = matrix_transpose(mat1)
print("The matrix after transpose:\n",result)

#==================================================================


def matrix_addition(mat1,mat2):


    n1 = len(mat1[0])
    n2 = len(mat1)
    mat = []

    for i in range(n2):
        row = []

        for j in range(n1):
            row.append(mat1[i][j] + mat2[i][j])
        mat.append(row)

    return mat

mat1 = [[1,-4],[7,9]]
mat2 = [[2,-6],[5,-8]]

res = matrix_addition(mat1, mat2)
print("The matrix after addition:\n",res)


#==========================================================================
    
def check_symetric_matrix(mat):
    #check symetric matrix

    mat1 = []
    n1 = len(mat[0])
    n2 = len(mat)
    if n1 != n2:
        print('Not a square matrix')
        return

    symetric = True
    for i in range(n2): 

        for j in range(n1):

            if mat[i][j] != mat[j][i]:
                symetric = False
                break                   #stop inner loop
                    
        if not symetric:                #stop outer loop
            break


    if symetric:
        print('Symetric Metrix')
    else:
        print('Not a symetric matrix')

mat = [[1,3],[2,1]]
check_symetric_matrix(mat)



    