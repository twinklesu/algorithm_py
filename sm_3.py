# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
class Node():
	def __init__(self, value, x, y):
		self.value = value
		self.x = x
		self.y = y
class Matrix():
	def __init__(self,li,n,m):
		self.n = n
		self.m = m
		self.matrix = []
		self.li = li
		for n_ in range(m):
			for m_ in range(n):
				self.matrix.append(Node(li[m*n_ + m_], m_, n_))
	def find(self,x,y):
		if x<0 or y<0 or x>=m or y>= n:
			return False
		return self.matrix[y*n + x]
	def change(self, x,y):
		if self.find(x,y) == False or self.find(x,y).value == 0:
			return False
		self.find(x,y).value == None
		return True
	
	
t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    li = []
    for _ in range(n):
    	li.extend(list(map(int, input().split())))
    ma = Matrix(li,n,m)
    res = True
    for node in ma.matrix:
    	if node.value == 1:
    		semires = []
    		semires.append(ma.change(node.x -1, node.y))
    		semires.append(ma.change(node.x-1, node.y-1))
    		semires.append(ma.change(node.x, node.y-1))
    		if False in semires:
    			semires = []
    			semires.append(ma.change(node.x-1, node.y))
    			semires.append(ma.change(node.x-1, node.y+1))
    			semires.append(ma.change(node.x, node.y+1))
    			if False in semires:
    				semires = []
    				semires.append(ma.change(node.x, node.y-1))
    				semires.append(ma.change(node.x+1, node.y-1))
    				semires.append(ma.change(node.x+1, node.y))
    				if False in semires:
    					semires = []
    					semires.append(ma.change(node.x+1, node.y))
    					semires.append(ma.change(node.x, node.y+1))
    					semires.append(ma.change(node.x+1, node.y+1))
    					if False in semires:
    						res = False
    	if not res:
    		break
    		
    if res:
    	print("YES")
    else:
    	print("NO")
