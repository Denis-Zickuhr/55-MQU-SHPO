from numpy import *

def ValidSupplyRoute(l, c):

    l.remove(0)
    
    Solution = BestTruck(l.copy(), c)
    factor = c / min(l.copy())

    for i in range(int(factor)):
        for i in range(Solution.count([c, []])):
            Solution.remove([c, []])

        sl = len(Solution)
        d = 0.50

        OptimalRoutesPool = []

        for i in range(sl):
            if min(Solution)[0] == 0:
                OptimalRoutesPool.append(min(Solution))
                Solution.remove(min(Solution))

        sl = len(Solution)

        Aptees = [0 for i in range(int(sl*d))]
        Inaptees = [0 for i in range(int(sl*d))]
    
        for i in range(int(sl*d)):
            Inaptees[i] = max(Solution)
            Solution.remove(max(Solution))

        for i in range(int(sl*d)):
            Aptees[i] = min(Solution)
            Solution.remove(min(Solution))

        while(len(Inaptees) > 0):
            inaptee = min(Inaptees)
            Inaptees.remove(inaptee)

            bestImprove = 0
            lastIndex = []
            for i in range(len(Aptees)):
                for j in range(len(Aptees[i][1])):
                    if Aptees[i][1][j] > bestImprove:
                        if inaptee[0] - Aptees[i][1][j] >= 0:
                            bestImprove = Aptees[i][1][j]
                            lastIndex = [i, j]

            if(len(lastIndex) > 0):
                inaptee[1].append(bestImprove)
                Aptees[lastIndex[0]][1].remove(Aptees[lastIndex[0]][1][lastIndex[1]])
                Aptees[lastIndex[0]][0] = c - sum(Aptees[lastIndex[0]][1])
                inaptee[0] = c - sum(inaptee[1])
            lastIndex.clear()
            Aptees.append(inaptee)

        Solution = Solution + Aptees + OptimalRoutesPool
        for i in range(Solution.count([c, []])):
            Solution.remove([c, []])
    
    return Solution

def BestTruck(l, c):

    # Bins
    b = NextFit(l, c)

    Solution = [[c, []] for i in range(b)]

    # Itens
    Bin = 0
    while (len(l) > 0):

        Item = l[len(l)-1]

        if Solution[Bin][0] - Item >= 0:
            Solution[Bin][1].append(Item)
            Solution[Bin][0] += -Item
            l.remove(Item)
            Bin = 0
        else:
            Bin += 1
            if Bin >= len(Solution):
                Bin = 0

    return Solution

def NextFit(l, c):
    n = 1
    Bin = 0
    for i in range(len(l)):
        val = Bin + l[i]
        if val <= c:
            Bin = val
        else:
            n = n + 1
            Bin = l[i]
    return n