import numpy as np
import cv2 as cv
import os

dirList = os.listdir("./Raw images")

for di in dirList:
	for root, dirs, files in os.walk(os.path.join("./Raw images", di)):
		for name in files:
			print(os.path.join(root, name))
			img = cv.imread(os.path.join(root, name))
			res = cv.resize(img, (1280, 720), interpolation = cv.INTER_CUBIC)
			print(os.path.join(os.path.join("./Pre-processed dataset", di), name))
			cv.imwrite(os.path.join(os.path.join("./Pre-processed dataset", di), name), res)
