from matplotlib.pyplot import imsave, imshow
import random
from pprint import pprint
from sys import maxsize
from PIL import Image
import numpy as np

WIDTH = 1024
HEIGHT = 1024
NUM_SPOTS = 100

COLOR_PALETTE = [
	[0.0859375,  0.35546875, 0.19921875],
	[0.078125,   0.41796875, 0.2265625],
	[0.96875,    0.6953125,  0.16015625],
	[0.73046875, 0.14453125, 0.15625],
	[0.9140625,  0.2734375,  0.1875]
	]


def create_random_spots():
	x = random.sample(range(WIDTH), NUM_SPOTS)
	y = random.sample(range(HEIGHT), NUM_SPOTS)
	points = list(zip(x, y))
	points.sort()
	colours = {}
	for p in points:
		colours[p] = random.choice(COLOR_PALETTE)
	return colours


def squared_dist(p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


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
	img_arr = np.zeros((WIDTH, HEIGHT, 3))
	pprint(colours)
	for y in range(WIDTH):
		for x in range(HEIGHT):
			min_p = min(((x - p[0])**2 + (y - p[1])**2, p) for p in colours)
			img_arr[y][x] = colours[min_p[1]]
		print( "%.2f%%" %(((y+1)/WIDTH)*100))
	imsave("ver1.png", img_arr)
	im = Image.fromarray((img_arr * 255).astype(np.uint8))
	im.save("pillow.png")

if __name__=="__main__":
	main()
