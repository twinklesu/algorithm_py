start, end = map(int, input().split())
x,y = map(int, input().split())

start = (start - y)//x
end = (end-y)//x
if start != end:
    print("Unknwon Number")
else:
    print(int(start))