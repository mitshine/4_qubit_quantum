import math
import numpy as np

matrix = [[1, 2, 3, 4], 
	[5, 6, 7, 8],
	[9, 10, 11, 12]]

print("Matrix =", matrix)

pauli_x = [[0, 1], [1, 0]]

print("Pauli_X =", pauli_x)

pauli_y = [[0, complex(0,-1)], [complex(0,1), 0]]

print("Pauli_Y =", pauli_y)

pauli_z = [[1, 0], [0, -1]]

print("Pauli_Z =", pauli_z)

hadamard = np.array([[1, 1], [1, -1]])

hadamard = (1/math.sqrt(2))*hadamard

print("Hadamard =", hadamard)

phase = [[1, 0], [0, complex(0,1)]]

print("Phase =", phase)

# pi_8 = [[1, 0], [0, math.exp((complex(0,1)*math.pi)/4)]]

# print("PI/8 =", pi_8)

pi_8 = [[1, 0], [0, math.exp((math.pi)/4)]]

print("PI/8 =", pi_8)

cnot = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]

print("Controlled NOT =", cnot)

cz = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, -1]]

print("Controlled Z =", cz)

swap = [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]

print("SWAP =", swap)

toffoli = [[1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0]]

print("TOFFOLI (CCNOT, CCX, TOFF) =", toffoli)

