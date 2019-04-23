# imports
import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute
import random
    
regs = 2

q = QuantumRegister(regs*2) # qubit register
c = ClassicalRegister(regs) # classical register
circ = QuantumCircuit(q, c) # Quantum Circuit on q
secret = None
number = None

    
def gen_rand():
    number = 0
    secret = [None] * regs
    j = regs-1
    for i in range(0, regs):
        rand = random.randint(0, 9)%2
        number += rand*(2**i)
        print("rand is %d" %rand)
        secret[j] = str(rand) #binary string
        j -= 1
    if number == 0:
        secret = []
        j = regs-1
        return gen_rand()
    else:
        return number, secret
    
#generating random secret


number, secret = gen_rand()
print("binary is: "+"{0:b}".format(number))
print("number is %d" %number)
for i in range(0, len(secret)):
    print(">> secret[%d] is %s" %(i,secret[i]))
#print("secret[0] is %c" %secret[0])
print(">> secret is: "+''.join(secret)+"\n")

for i in range(0, regs):
    circ.h(q[i])
    #print("Hadamard on q[%d]" % i)

#begining of blackbox
circ.barrier()
for i in range(0, regs):
    circ.cx(q[i], q[i+regs])
    #copying first half of registers to second half

# for i in range(0, regs):
    #if i % 2 == 0:
     #   circ.x(q[i])
    #else:
     #   circ.cx(q[i-1], q[i])
#    0
circ.barrier()
print(circ)






