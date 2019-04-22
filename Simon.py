# imports
import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute
import random

num_qubits = 4

q = QuantumRegister(num_qubits) # 4 qubit register
c = ClassicalRegister(1) # 1 classical register
circ = QuantumCircuit(q, c) # Quantum Circuit on q

#generating random secret
secret = ""
for i in range(0, int(num_qubits/2)):
    secret += str(random.randint(0, 10000)%2) #binary string

print(">> secret is:"+secret+"\n")

for i in range(0, int(num_qubits/2)):
    circ.h(q[i])
    #print("Hadamard on q[%d]" % i)

#begining of blackbox
circ.barrier()
for i in range(0, int(num_qubits/2)):
    circ.cx(q[i], q[int(i+num_qubits/2)])
    #copying first half of registers to second half

print(circ)



