# imports
import numpy as np
from sympy import *
#import qiskit_aqua.components.oracles 
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute
from qiskit.tools.monitor import job_monitor
from qiskit import execute, BasicAer
from qiskit.providers.ibmq import least_busy
import matplotlib.pyplot
from qiskit.tools.visualization import plot_state_city, plot_histogram
import pylab
import random


#first ipythin cell
def simons_circuit(qbits, secret):
    n = qbits

    qr = QuantumRegister(n*2) # 4 qubit register
    cr = ClassicalRegister(n) # 1 classical register
    circ = QuantumCircuit(qr, cr) # Quantum Circuit on q

    for i in range(0, n):
        circ.h(qr[i])

    circ.barrier()

    for i in range(0, n):
        circ.cx(qr[i], qr[n+i])
    circ.barrier()

    s = secret

    #xor s.
    for i, c in enumerate(s):
        if c == '0':
            circ.cx(qr[i], qr[n+i])

    circ.barrier()

    for i in range(0, n):
        circ.h(qr[i])
        circ.measure(qr[i], cr[i])
    return circ

#second Ipython cell
n = 6
secret = '100011'
circ = simons_circuit(n, secret)
#to draw in Ipython notebook
#circ.draw(output='mpl')

#Third Ipython cell
simulator = Aer.get_backend('qasm_simulator')

#get first measurement to start making the matrix ofr the system of equations.
result = execute(circ, simulator, shots=1).result()
temp = result.get_counts(circ)
mes = next(iter(temp))
count = {}
count[mes] = 1
wi = get_wi(mes)
M = Matrix([wi])

#while loop to collect the rest
dim = 1
i = 0
while(True and i < 100 ):
    #run simul, get measurement
    result = execute(circ, simulator, shots=1).result()
    temp = result.get_counts(circ)
    mes = next(iter(temp))
    wi = get_wi(mes)
    if mes in count:
        count[mes] = count[mes] + 1
    # make augment matrix by adding the new row
    ma = M.col_join(Matrix([wi]))
    
    #check if new measuremnt is in the span of {w_i}
    m, mr = M.rref()
    mA, mar = ma.rref()
    if mr != mar:
        count[mes] = 1
        M = ma
        dim = dim + 1
    elif (dim == n - 1):
        break
    i = i + 1
    
#ptrint the system of equations that satisfy s
rows, cols = M.shape
for r in range(rows):
    Yr = [ "s[ "+str(i)+" ]" for i, v in enumerate(list(M[r,:])) if v == 1 ]
    if len(Yr) > 0:
        tStr = " + ".join(Yr)
        print(tStr, "= 0")
M

#fifth Ipython cell and code to print histogram in notebook
#plot_histogram(count, title='Simons problem')

# turn the measured string into an array of integers.
def get_wi(w):
    v = []
    for i in range(n):
        v.append(int(w[(n-i) - 1]))
    return v

''' old code below

regs = 2

q = QuantumRegister(regs*2) # qubit register
c = ClassicalRegister(regs) # classical register
circ = QuantumCircuit(q, c) # Quantum Circuit on q
secret = None
number = None
simulate = True
backend = None
job = None
result = None
outputstate = None
counts = None

#generating random secret
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
    #if number == 0:
    #    secret = []
    #    j = regs-1
    #    return gen_rand()

    return number, secret


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
circ.barrier()
    
for i in range(0, regs):
    if secret[i] == '1':
        #circ.x(q[i+regs])
        circ.cx(q[i], q[i+regs])
        
# for i in range(0, regs):
    #if i % 2 == 0:
     #   circ.x(q[i])
    #else:
     #   circ.cx(q[i-1], q[i])
#    0
circ.barrier()
for i in range(0, regs):
    circ.h(q[i])
    circ.measure(q[i], c[i])
print(circ)
        
if simulate:
    backend = BasicAer.get_backend('qasm_simulator')
    job = execute(circ, backend, shots = 1000)
    result = job.result()
    #outputstate = result.get_statevector(circ, decimals=3)
    counts = job.result().get_counts(circ)
    print(counts)
    plot_histogram(counts)
    #print(outputstate)
    #plot_state_city(outputstate)
    #pylab.show()
else:
    print("here")'''
        








