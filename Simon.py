# imports
import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute

num_qubits = 4

q = QuantumRegister(num_qubits) # 4 qubit register
circ = QuantumCircuit(q) # Quantum Circuit on q

for i in range(num_qubits/2 + 1):
    circ.h(q[i])
    #print("Hadamard on q[%d]" % i)

circ.draw()
