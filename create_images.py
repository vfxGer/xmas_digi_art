from matplotlib.pyplot import imsave, imshow
import random
from pprint import pprint
from sys import maxsize

WIDTH = 10
HEIGHT = 10
NUM_SPOTS = 5

def create_random_spots():
	x = random.sample(range(WIDTH), NUM_SPOTS)
	y = random.sample(range(HEIGHT), NUM_SPOTS)
	points = list(zip(x, y))
	points.sort()
	colours = {}
	for p in points:
		colours[p] = random.sample(range(0, 255), 3)
	return colours


def squared_dist(p1, p2):
	res = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
	# print(p1)
	# print(p2)
	# print(res)
	# print("*****")
	return res


def main():
	colours = create_random_spots()
	img = [[0] * (WIDTH)] * (HEIGHT)
	# pprint(colours)
	for x in range(WIDTH):
		for y in range(HEIGHT):
			min_dist = maxsize
			for p in colours:
				d = squared_dist([x,y], p)
				if d < min_dist:
					min_dist = d
					if d==0:
						print((x,y))
						img[x][y] = [255, 0, 0]
					else:
						img[x][y] = colours[p]
					print("----------")
		
		# print(((x+1)/WIDTH)*100)
	pprint(img)
	# red = (1.0,0.0,0.0)
	# redline = [red] * 1024
	# redimage = [redline] * 1024
	imsave("ver1.jpg", img)

if __name__=="__main__":
	main()