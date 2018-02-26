#! /usr/bin/env python

####################################################################################################
# Name: CV Key Item Routine
# Author: Jorden Allcock
#
# Description: File is not essential to core processing, however is designed to assist in formatt-
# ing CV's into an easier to read format.
#
# Parameters:
#
#	p_cv_locatoin - Location of file to be processed to be passed as an absolute value
#
# Output:
#
#		- Parsed Key Information consisting of
####################################################################################################

###################################################################################
# Required imports
###################################################################################

import os, sys
from munkres import Munkres, print_matrix

###################################################################################
# Pull CV Information
###################################################################################


def main(p_directory):

    matrix = [[5, 9, 1],[10, 3, 2],[8, 7, 4]]
    cost_matrix = []
    for row in matrix:
        cost_row = []
        for col in row:
            cost_row += [sys.maxsize - col]
        cost_matrix += [cost_row]

    m = Munkres()  
    indexes = m.compute(cost_matrix)
    print_matrix(matrix, msg='Highest profit through this matrix:')
    total = 0
    for row, column in indexes:
        value = matrix[row][column]
        total += value
        print '(%d, %d) -> %d' % (row, column, value)

    print 'total profit=%d' % total


if __name__ == "__main__":
     main(sys.argv[1])
