n = int(input())
stair = []
for _ in range(n):
    stair.append(int(input()))

stair.reverse()
score = [0]
isPrepOne = False
pointer = 0

def recursive():
    if pointer == n-14:
        if isPrepOne:

