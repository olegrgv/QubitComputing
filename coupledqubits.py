from qutip import *
from scipy import *
 
#spin
q1 = basis(2, 0)
q2 = basis(2,0)
 
print (q1)
print (q2)
print (tensor(q1,q2))
