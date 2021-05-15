t = int(input())


mem = [1,1,1,2,2]
mem_len = 5
for _ in range(t):
    n = int(input())
    n -= 1 # 0 인덱싱
    while n >= mem_len:
        mem.append(mem[mem_len-1]+mem[mem_len-5])
        mem_len += 1
    print(mem[n])
