from itertools import combinations


n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
chicken = []
house = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i,j))

safeChicken = combinations(chicken, m)
minCityDist = 10**7
for combination in safeChicken:
    cityDist = 0
    for h in house:
        minHouseDist = n+n+1
        for c in combination:
            houseDist = abs(c[0]-h[0])+abs(c[1]-h[1])
            minHouseDist = min(minHouseDist, houseDist)
        cityDist += minHouseDist
    minCityDist = min(minCityDist, cityDist)

print(minCityDist)