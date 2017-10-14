import math
import numpy as np

def hadamard_gate():
	return 1/math.sqrt(2) * np.array([[1,1],[1,-1]])

def not_gate():
	return np.array([[0,1],[1,0]])
