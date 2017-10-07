class Solution(object):
	"""docstring for Solution"""
	def countBattleships(set,board):
		h,v=len(board),len(board[0])
		count=0
		for x in range(h):
			for y in range(v):
				if board[x][y]=='X':
					if x==0 or board[x-1][y]=='.':
						if y==0 or board[x][y-1]=='.':
							count+=1
		return count
a=Solution()
b=[['X','X','X','X']]#,['.','.','.','X'],['.','.','.','X']]
print(a.countBattleships(b))
