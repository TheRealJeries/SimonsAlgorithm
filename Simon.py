# imports
import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute
import random

regs = 2

q = QuantumRegister(regs*2) # qubit register
c = ClassicalRegister(regs) # classical register
circ = QuantumCircuit(q, c) # Quantum Circuit on q

#generating random secret
secret = ""
for i in range(0, regs):
    secret += str(random.randint(0, 9)%2) #binary string

print(">> secret is: "+secret+"\n")

for i in range(0, regs):
    circ.h(q[i])
    #print("Hadamard on q[%d]" % i)

#begining of blackbox
circ.barrier()
for i in range(0, regs):
    circ.cx(q[i], q[i+regs])
    #copying first half of registers to second half

print(circ)



