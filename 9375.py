def solution():
    n = int(input())
    clothes = dict()
    for _ in range(n):
        item, cat = map(str, input().split())
        if cat in clothes:
            clothes[cat].append(item)
        else:
            clothes[cat] = [item]

    totalNum = 1
    for items in clothes.values():
        totalNum *= (len(items)+1)

    print(totalNum-1)


def main():
    t = int(input())
    for _ in range(t):
        solution()


main()
