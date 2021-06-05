# def main():
#     t = int(input())
#     for _ in range(t):
#         x, y = map(int, input().split())
#         k = 0
#         count = 0
#         while y > x:
#             count += 1
#             k += 1
#             x += k
#             if y-k >= x:
#                 count += 1
#                 y -= k
#         print(count)


def main():
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        k = 1
        count = 0
        num = y - x
        while num >= k:
            num -= k
            count += 1
            if num >= k:
                num -= k
                count +=1
            k += 1
        if num > 0:
            count +=1
        print(count)

main()


