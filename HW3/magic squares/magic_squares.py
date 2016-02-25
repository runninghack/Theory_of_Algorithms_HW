import timeit

start = timeit.default_timer()



def magic(n):
	if n > 2 and n % 2 == 0:
		print "You need an odd number."
	elif n <=2:
		print "You need a number greater or equal to 3."
	else:
		print "Magic Square: ", n, 'x', n
		grid = [ [ 0 for c in xrange(n) ] for r in xrange(n) ]
		row, col = 0, n/2
		n2, v = n*n, 1;
		r, c = 0, 0
		grid[row][col] = v
		while v != n2:
			v += 1
			if (row-1) >= 0:
			    r = row-1
			else:
			    r = n-1
			if (col+1) < n:
			    c = col+1
			else: c = 0
			if grid[r][c]:
				if (row+1) < n:
					r = row+1
					if grid[r][col]:
					    break
					c = col
			grid[r][c] = v
			row = r
			col = c
		for r in xrange(n):
			for c in xrange(n):
                                iiii = 1
				#print "%2d" % grid[r][c],
			#print
                                

magic(12999)
stop = timeit.default_timer()

print stop - start 
