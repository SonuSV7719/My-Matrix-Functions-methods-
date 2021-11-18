# Function to find multiplication of matrix using 3 loops---------------------->>

def productMat(mat1, mat2, colMat2,rowMat2, colMat1):
    if colMat1 == rowMat2:
        sum = 0
        
        sumApp = []

        for i in range(len(mat1)):
            for j in range(colMat2):
                for k in range(colMat1):
                    multi = mat1[i][k]*mat2[k][j]
                    sum = sum + multi
                sumApp.append(sum)
                sum = 0
            
    return sumApp
# Function to find multiplication of matrix using two loops------------------->>

def multiMatrix(mat1, mat2, rowMat1, colMat2, rowMat2, colMat1):
    try: 
        if colMat1 == colMat2 and rowMat1==rowMat2:
        
        
            k = 0
            m = 0
            sum = 0
            ran = (rowMat1*colMat2)
            productMatrix = []
            for i in range(ran):
                for j in range(len(mat2)):

                    multi = mat1[m][j]*mat2[j][k]
                    sum = sum + multi
                productMatrix.append(sum)
                if j == (rowMat2-1) and k == (colMat2-1):
                    m+=1
                    
                k+=1
                sum = 0
                if k>=len(mat2):
                    k = 0
            return productMatrix    
        else:
            print("You have entered wrong matrix please select matrix with same columns!") 
         
    except Exception as e:
        print(e)  
    
     
# Function to find addition of matrix-------------------------------->>

def matAddition(mat1, mat2, r, c):
    if r==c:
        '''
        mat = matrix
        r= Number of rows
        c= Number of columns
        '''
        addition = []
        for i in range(r):
            subList = []
            for j in range(c):
                sum = mat1[i][j]+mat2[i][j]
                subList.append(sum)
            addition.append(subList)
        return addition   

# Function to find matrix subtraction-------------------------------------->>

def matSubtraction(mat1, mat2, r, c):
    if r == c:
        '''
        mat = matrix
        r= Number of rows
        c= Number of columns
        '''
        subtraction = []
        for i in range(r):
            subList = []
            for j in range(c):
                sum = mat1[i][j]-mat2[i][j]
                subList.append(sum)
            subtraction.append(subList)
        return subtraction  

# Function to check lower triangular matrix--------------------------->>

def cLowerTriangular(mat, c):
    for i in range(len(mat)):
        for j in range((i+1), c):
            if mat[i][j] != 0:
                return False
            
    return True

# Function to check uppper triangular matrix------------------------------>>


def cUpperTriangular(mat):
    for i in range(1, len(mat)):
        for j in range(i):
            if mat[i][j] != 0:
                return False
    return True

# Function to find transpose of matrix--------------------------->>>

def transpose(mat, r, c):
    """r=row, mat= matrix and c=column"""
    try:
        for i in range(r):
            for j in range(c):
                print(mat[j][i],end="\t")
            print("\n")
    except Exception as e:
        print(e)

def cMatrix(r, c):
    mat = []
    for i in range(r):
            row = []
            for j in range(c):
                element = int(input("Enter elements of matrix: "))
                row.append(element)
            mat.append(row)
    return mat
    
 


r1 = int(input("Enter number of rows: "))
c1 = int(input("Enter number of columns: "))

mat1 = cMatrix(r1, c1)
r2 = int(input("Enter number of rows: "))
c2 = int(input("Enter number of columns: "))
mat2 = cMatrix(r2, c2)

# if r1==c1:  
#     print("Addition of two matrix: ", matAddition(mat1, mat2, r1, c1))    
#     print("Subtraction of two matrix: ", matSubtraction(mat1, mat2, r1, c1))
#     print("Multiplication of two matrix: ", multiMatrix(mat1, mat2,r1, c2, r2, c1))  
#     print("Multiplication of two matrix: ", productMat(mat1, mat2,c2, r2, c1))  
#     if cUpperTriangular(mat1):
#         print ("Above matrix is upper triangular matrix")
#     else:
#         print ("Above matrix is not upper triangular matrix")

#     if cLowerTriangular(mat1, c1):
#         print ("Above matrix is lower triangular matrix")
#     else:
#         print ("Above matrix is not lower triangular matrix")
# else:
#     print("Please enter row and columns equal i.e. n*n formate\nTry again!")

# print("Transpose of matrix 1: ")
# transpose(mat1, r1, c1)
