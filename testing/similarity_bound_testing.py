#! /usr/bin/env python

####################################################################################################
# Name: CV Match Routin - Word Vectors on Keywords
# Author: Jorden Allcock
#
# Description: File is responsible for:
#
#	- Reading appropriate contents of specified resource request
#	- Selecting appropriate information from CV (keywords)
#	- Identifying similarity/match between CV elements and Resource Request elements
#
# Parameters:
#
#	- p_resource_request_loc        Directory/file location of specified resource request to be
#                                       analysed
#
####################################################################################################

###################################################################################
# Required imports
###################################################################################

from __future__ import unicode_literals
import spacy
import random
import xlrd                             # To enable analysis of Resource Request Spreadsheet
import os                               # To enable file browsing of local directory
import collections                      # To enable dictionary addition/updating
import operator                         # To enable sorting of dictionary elements
import sys
sys.path.append('..')			# Required to import scripts from parent folder

import cv_resource_rank                 # Custom script written to return the best candidate per job
import cv_resource_score
import cv_match_word_vectors

import fileinput

with open('/home/jallcock/environments/Final-Project/testing/similarity_bounds_test.txt', 'a') as log_file:
    for x in range (1):
        similarity_bound = x * 0.01
        print('Test [' + str(x) + '] - Similarity Bound [' + str(similarity_bound) + ']')

        for line in fileinput.input('/home/jallcock/environments/Final-Project/cv_match_word_vectors.py', inplace=1):
            if 'similarity_bound = ' in line:
                line = 'similarity_bound = ' + str(similarity_bound) + '\n'

            sys.stdout.write(line)

        log_file.write('Test [' + str(x) + '] - Similarity Bound [' + str(similarity_bound) + ']\n')
        log_file.write(str(cv_match_word_vectors.main('/home/jallcock/environments/Final-Project/resource_requests/resource_request_1.xlsx')))

