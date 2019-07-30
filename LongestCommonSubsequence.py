#:: longest common subsequence
def LCS(A1, A2):
    m = len(A1)
    n = len(A2)
    LCSmatric = [[None]*(n+1) for x in range(m+1)]  #intializing new matric for dynamic programming
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                LCSmatric[i][j] = 0

            elif A1[i-1] == A2[j-1]:
                LCSmatric[i][j] = LCSmatric[i-1][j-1] + 1  #add one to the value of the upper left diagonal

            else:
                LCSmatric[i][j] = max(LCSmatric[i-1][j], LCSmatric[i][j-1]) #find the maximum between top and left
    return LCSmatric[m][n]

print(LCS("GXTXAYB", "AGGTAB"))
