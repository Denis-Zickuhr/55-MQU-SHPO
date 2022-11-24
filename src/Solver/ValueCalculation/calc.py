def calc(P, D, S):
    
    pairs = []

    for i in range(len(S)):
        for j in range(len(S[i])-1):
            pairs.append([S[i][j], S[i][j+1]])

    S_Value = 0

    for x in pairs:
        S_Value += round(P[x[0]][x[1]], 0)

    return round(S_Value, 0)
