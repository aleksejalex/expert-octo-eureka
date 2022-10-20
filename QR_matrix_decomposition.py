"""
QR matrix decomposition (need that for RAD)
source >>> https://www.quantstart.com/articles/QR-Decomposition-with-Python-and-NumPy/

by AG, 20221020
"""

import pprint
import numpy as np
import scipy
import scipy.linalg   # SciPy Linear Algebra Library

A = np.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]])  # From the Wikipedia Article on QR Decomposition
Q, R = scipy.linalg.qr(A)

#print "A:"
pprint.pprint(A)

#print "Q:"
pprint.pprint(Q)

#print "R:"
pprint.pprint(R)

A_composed_back = Q * R
pprint.pprint(A_composed_back)




