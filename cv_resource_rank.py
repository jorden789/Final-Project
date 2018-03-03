#! /usr/bin/env python

####################################################################################################
# Name: CV Resource Ranking Routine
# Author: Jorden Allcock
#
# Description: Script will receive as input the suitability matrix of all CV's per job(s) and return
#		the best candidate per job.
#
# Parameters:
#
#	p_cost_matrix - Cost Matrix of specified job(s)
#
# Output:
#
#		- Matrix location of best candidate per job(s) specified
####################################################################################################

###################################################################################
# Required imports
###################################################################################

import os, sys
from munkres import Munkres, print_matrix, make_cost_matrix

###################################################################################
# Pull CV Information
###################################################################################


def main(p_cost_matrix):
    l_cost_matrix = []

    #for x, score in p_cost_matrix.iteritems():
    for x, score in p_cost_matrix.items():
        l_cost_matrix.append(score)

    #print(l_cost_matrix)
    
    cost_matrix = Munkres.make_cost_matrix([l_cost_matrix], lambda cost: 800 - cost)

    m = Munkres()  
    indexes = m.compute(cost_matrix)
    #print_matrix(cost_matrix, msg='Highest profit through this matrix:')
    total = 0
    position = []
    for row, column in indexes:
        value = cost_matrix[row][column]
        total += value
        position.append(row)
        position.append(column)
        #print '(%d, %d) -> %d' % (row, column, value)

    #print 'total profit=%d' % total
    
    return(position)

if __name__ == "__main__":
     main(sys.argv[1])
