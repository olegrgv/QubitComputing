from qutip import *
from scipy import *
 
spin = basis(2, 0)
print (sigmam() * spin)
print (sigmap() * spin)
