


def zeroOut(B,row1,row2,col):
    A = B.copy()
    row1l = B[row1].copy()
    row2l = B[row2].copy()
    factor = row2l[col]
    for i in range(0,len(row1l)):
        row1l[i]*= factor
    for i in range(0,len(row2l)):
        row2l[i] -= row1l[i]
    A[row2] = row2l
    return A
def scaleRow(B,row):
    A = B.copy()
    rowl = A[row].copy()
    mult = 0
    for i in range(0,len(rowl)):
        if rowl[i] != 0:
            mult = 1/rowl[i]
            break
    for i in range(0,len(rowl)):
        rowl[i] *= mult
    A[row] = rowl
    return A
def numLeadingZeros(lis):
    c = 0
    for e in lis:
        if e == 0:
            c += 1 
        else:
            return c
    return c
def zeroOnBottom(B):
    return sorted(B, key=numLeadingZeros)
    

def rref(B):
    A = B.copy()
    rows = len(A)
    columns = len(A[0])
    for i in range(rows):
        A = zeroOnBottom(A)
        A = scaleRow(A,i)
        for j in range(rows):
            if j!=i:
                A = zeroOut(A,i,j,i)
    A = zeroOnBottom(A)
    return A



matrib = [[1,-1,3],[3,-3,0]]     

print(rref(matrib))
        
