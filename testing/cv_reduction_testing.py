#! /usr/bin/env python
# -*- coding: utf-8 -*-
####################################################################################################
# Name: CV Process Testing
# Author: Jorden Allcock
#
# Description: File is responsible for:
#
#       - Mesuring Size of Files prior to running python script
#	- Initiating the CV Process operation to strip characters and thus reduce file size
#	- Calculate difference of file sizes before and after processing
#	- Output file size, positive value shows a reduction in file size
####################################################################################################

###################################################################################
# Required imports
###################################################################################

import os                               # To enable file browsing of local directory
import sys
import datetime				# Required to show start/end datetime of processing
sys.path.append('..')                   # Required to import scripts from parent folder
import collections
import cv_process

###################################################################################
# Getting initial CV File Size
###################################################################################

logfile = open('/home/jallcock/environments/Final-Project/testing/cv_reduction_testing_log.txt', 'a')

logfile.write('Starting processing at ' + str(datetime.datetime.now()) + '\n\n')

cv_directory = '/home/jallcock/environments/Final-Project/stored_cvs'
cv_size_difference = {}

if os.listdir(cv_directory) == []:
    logfile.write('Directory empty - unable to process CVs')
else:
    for file in os.listdir(cv_directory):
        if os.path.getsize(os.path.join(cv_directory, file)) > 0:
            cv_size_difference[file] = os.path.getsize(os.path.join(cv_directory, file))
            logfile.write('File size of [' + file + '] before processing - ' + str(os.path.getsize(os.path.join(cv_directory, file))) + '\n')

    logfile.write('\nInitial CV Size Computed')

    logfile.write('\n\n')

###################################################################################
# Initiating CV Process script
###################################################################################

    logfile.write('Running CV Process script\n')

    cv_process.main(cv_directory)

    logfile.write('Completed processing of CVs\n')

###################################################################################
# Checking contents of CV Directory after CV Download
###################################################################################

#if os.listdir(cv_directory) == []:
    for file in os.listdir(cv_directory):
        if os.path.getsize(os.path.join(cv_directory, file)) > 0:
            cv_size_difference[file] = cv_size_difference[file] - os.path.getsize(os.path.join(cv_directory, file))
            logfile.write('File size of [' + file + '] after processing - ' + str(os.path.getsize(os.path.join(cv_directory, file))) + '\n')
        else:
            logfile.write('************************' + file + ' IS ZERO SIZED************************' + '\n')
#else:
#    logfile.write('Files not written to directory\n')

###################################################################################
# Outputting Difference in File Size
###################################################################################

for key in cv_size_difference:
    logfile.write('Difference in file size for [' + key  + '] is ' + str(cv_size_difference[key]) + '\n')

logfile.write('Finished processing at ' + str(datetime.datetime.now()) + '\n')

logfile.close()
