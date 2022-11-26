import numpy
def calc(P, D, S, C, Dc):

    pairs = []

    STATUS = "VALID"

    if Dc.count(0) != len(Dc):
        STATUS = "INVALID"

    for i in range(len(S)):
        c = 0
        for j in range(len(S[i])-1):
            pairs.append([S[i][j], S[i][j+1]])
            c += D[S[i][j]]
            # print(f"{i},{j},: {D[S[i][j]]}")
        # print(c)
        if C - c < 0:
            STATUS = "INVALID"

    S_Value = 0

    for x in pairs:
        if x != 0:
            n = round(P[x[0]][x[1]], 0)
            S_Value += n if not numpy.isnan(n) else 0
        
    return round(S_Value, 0), STATUS, pairs
