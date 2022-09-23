# Lar, Jeff Emerson F.
# 2019-03845

# Function that generates the actual alignment
def traceback(a,x,y, match_score=3,gap_cost=2):
	mrows = len(x)
	ncols = len(y)
	numMax = 0
	# Find max number in matrix
	for i in range(1,mrows+1):
		for j in range(1,ncols+1):
			if (a[i][j]>numMax):
				numMax = a[i][j]
				indexI = i
				indexJ = j
	# Sequence list holds traceback
	sequence = []
	# Loop that determines where to traceback
	while(True):
		maxNum = 0
		match = a[indexI-1][indexJ-1] - match_score
		if(x[indexI-1] == y[indexJ-1]):
			match = a[indexI-1][indexJ-1] + match_score
		delete = a[indexI - 1][indexJ] - gap_cost
		insert = a[indexI][indexJ - 1] - gap_cost
		num = max(match,delete,insert,0)
		if (match == num):
			sequence.insert(0,0)
			indexI-=1
			indexJ-=1
		elif (insert == num):
			sequence.insert(0,1)
			indexJ-=1
		else:
			sequence.insert(0,2)
			indexI-=1
		if (a[indexI][indexJ]==0):
			if (sequence[0]==0):
				indexI+=1
				indexJ+=1
			elif (sequence[0]==1):
				indexJ+=1
			else:
				indexI+=1
			break
	# Printing of alignment
	for i in range(0,3):
		indexX = indexI
		indexY = indexJ
		for j in range(0,len(sequence)):
			if (sequence[j]==0):
				if (i==0 or i==2):
					print(x[indexX-1],end="")
				else:
					print("|",end="")
				indexX+=1
				indexY+=1
			elif (sequence[j]==1):
				if (i==0):
					print("-",end="")
				elif (i==1):
					print(" ",end="")
				else:
					print(y[indexY-1],end="")
				indexY+=1
			else:
				if (i==0):
					print(x[indexX-1],end="")
				elif (i==1):
					print(" ",end="")
				else:
					print("-",end="")
				indexX+=1
		print()


# Printing of matrix
def print_matrix1(a,x,y):
	x = " "+x
	y = " "+y
	mrows = len(x)
	ncols = len(y)


	print("%2s" % " ", end=" ")
	for i in range(ncols):
		print("%2s" % y[i], end=" ")
	print()
	print("%2s" % " ", end=' ')
	for i in range(mrows):
		if (i!=0):
			print("%2s" % x[i], end=' ')
		for j in range(ncols):
			print("%2d" % a[i][j], end=' ')
		print()


def gen_matrix(x, y, match_score=3, gap_cost=2):
	mrows = len(x)
	ncols = len(y)

	#initialize matrix to zeroes
	a = [0] * (mrows + 1)
	for i in range(mrows + 1):
		a[i] = [0] * (ncols + 1)
	
	# print_matrix1(a,x,y)
	# print()
	
	for i in range(1,mrows+1):
		for j in range(1,ncols+1):
			match = a[i-1][j-1] - match_score
			if(x[i-1] == y[j-1]):
				match = a[i-1][j-1] + match_score
			delete = a[i - 1][j] - gap_cost
			insert = a[i][j - 1] - gap_cost
			a[i][j]=max(match,delete,insert,0)

	print_matrix1(a,x,y)	
	print()

	return(a)
	
x = "GGTTGACTA"	
y = "TGTTACGG"

# x = "ATAGACGACAT"
# y = "TTTAGCATGCGCAT"

a=gen_matrix(x,y)

traceback(a,x,y)

# print_matrix1(a,x,y)


