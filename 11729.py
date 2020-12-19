def hanoi(n,a,b,c):
    if len(c) == n:
        return a,b,c
    
    
# 3개를 A에서 B로 옮기기.
n = int(input())
A = [range(n,0,-1)]
B = []
C = []
      
