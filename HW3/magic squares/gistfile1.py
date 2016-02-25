#!/usr/bin/python
# encoding:utf-8
"""
幻方类型：N为奇数
构造方法： 

1. 先画一个n×n方格表,  
    则横向方向的坐标索引x为(0,1,2,3,...,n-2,n-1),  
    纵向方向的坐标索引y为(0,1,2,3,...,n-2,n-1);  

2. 把1填写在最顶行的中间((n-1)/2),0)；  
3. 当k填好后,假定k的位置为X(i,j)  
    定义k的斜上方为Q,k的正下方为E
4. 假定Q的位置为(k,l),  
    则当`i+1 <= n-1`时, `k = i+1` 否则 `k= 0`  
    当`j-1 >= 0`时, `l= j-1` 否则 `l= n-1`

5. 假定E的位置为(i,s),  
    则当`j+1 <= n-1`时, `s = j+1` 否则 `s= 0`
6. 现在来放置k+1,  
    如果X的斜上方Q为空,则将k+1放置于X中,  
    如果Q不为空,但是E为空,则将k+1放置于E中,  
7. ok,遍历k in range(2,n*n)的情况

    
    30	39	48	1	10	19	28
    38	47	7	9	18	27	29
    46	6	8	17	26	35	37
    5	14	16	25	34	36	45
    13	15	24	33	42	44	4
    21	23	32	41	43	3	12
    22	31	40	49	2	11	20

"""
import sys

def getQWE((y, x), n):
	"""
		在n维矩阵中
		获取x,y的斜上方q,正下方e坐标

		# 4. 假定Q的位置为(k,l),  
		#     则当`i+1 <= n-1`时, `k = i+1` 否则 `k= 0`  
		#     当`j-1 >= 0`时, `l= j-1` 否则 `l= n-1`

		# 6. 假定E的位置为(i,s),  
		#     则当`j+1 <= n-1`时, `s = j+1` 否则 `s= 0`

		>>> getQWE((0, 1), 3)
		([2, 2], [1, 1])
		>>> getQWE((0, 2), 3)
		([2, 0], [1, 2])
	"""
	e, q = ([y + 1, x], [y - 1, x + 1])
	for x in (e,q):
		if x[0] > n -1:
			x[0] = 0
		if x[0] < 0:
			x[0] = n - 1

		if x[1] > n - 1:
			x[1] = 0
		if x[0] < 0:
			x[0] = n - 1

	return (q,e)

def process(n):
	"""
		处理奇数n的幻方

		>>> process(3)
		[[8, 1, 6], [3, 5, 7], [4, 9, 2]]
		>>> process(5)
		[[17, 24, 1, 8, 15], [23, 5, 7, 14, 16], [4, 6, 13, 20, 22], [10, 12, 19, 21, 3], [11, 18, 25, 2, 9]]
	"""
	d = []
	for i in range(n):
		l = []
		for j in range(n):
			l.append(0)
		d.append(l)

	y, x = (0, (n-1)/2)
	k = 1
	d[y][x] = k
	n2 = n * n
	while k != n2:
		(qy,qx),(ey, ex) = getQWE((y,x), n)

		if d[qy][qx] != 0:
			qy,qx = ey,ex
			
		y, x = qy, qx
		k = k + 1
		d[y][x] = k

	return d
def output(result):
	for y in result:
		print y

if __name__ == '__main__':
	import sys

	import doctest
	x = doctest.testmod()
	if x[0]:sys.exit()


	n = int(sys.argv[1])
	if n%2 != 1:
		print("请输入奇数...!")
	else:
		result = process(n)
		output(result)