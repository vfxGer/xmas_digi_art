from matplotlib.pyplot import imsave, imshow
import random
from pprint import pprint
from sys import maxsize

WIDTH = 1024
HEIGHT = 1024
NUM_SPOTS = 100

def create_random_spots():
	x = random.sample(range(WIDTH), NUM_SPOTS)
	y = random.sample(range(HEIGHT), NUM_SPOTS)
	points = list(zip(x, y))
	points.sort()
	colours = {}
	for p in points:
		colours[p] = random.sample(range(255), 3)
	return colours


def squared_dist(p1, p2):
	res = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
	# print("(%d - %d)**2 + (%d - %d)**2=%d"%(p1[0], p2[0], p1[1], p2[1], res) )
	# print(p1)
	# print(p2)
	# print(res)
	return res


def test():
	row = [0] * 10
	img_arr = []
	for _ in range(10):
		img_arr.append(row.copy())
	pprint(img_arr)
	img_arr[0][0] = 72
	pprint(img_arr)
	assert img_arr[1][0]==0


def main():
	colours = create_random_spots()
	row = [0] * WIDTH
	img_arr = []
	for _ in range(HEIGHT):
		img_arr.append(row.copy())
	pprint(colours)
	# pprint(img_arr)
	for y in range(WIDTH):
		for x in range(HEIGHT):
			# print([x,y])
			min_dist = maxsize
			for p in colours:
				d = squared_dist([x,y], p)
				if d < min_dist:
					min_dist = d
					# if d==0:
					# # # 	print((x,y))
					#   	img_arr[y][x] = "x"
					# else:
					img_arr[y][x] = colours[p]
					# print("Setting %d, %d to %d"%(x,y,colours[p]))
					# print("----------")
		print( "%.2f%%" %(((y+1)/WIDTH)*100))
	# pprint(img_arr)
	# red = (1.0,0.0,0.0)
	# redline = [red] * 1024
	# redimage = [redline] * 1024
	imsave("ver1.png", img_arr)

if __name__=="__main__":
	main()
