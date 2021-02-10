import numpy as np
import csv
__csv__ = "email-enron-only.csv"
matrix = None
width = None
height = None
with open(__csv__, newline='') as f:
	r = csv.reader(f, delimiter=',')
	x = list(r)
	matrix = np.array(x).astype("int")
	width = len(matrix[0])
	height = len(matrix)
