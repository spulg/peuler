# a lattice path must contain the same amount of down moves as right moves
# the problem is to find all permutation of ups and downs
# in an n x n grid there are n + n = 2n moves to the right and down

import scipy

if __name__ == '__main__':
    n = 20
    print(int(scipy.special.binom(2*n, n)))

