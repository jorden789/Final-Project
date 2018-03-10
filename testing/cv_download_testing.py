#! /usr/bin/env python
# -*- coding: utf-8 -*-
####################################################################################################
# Name: CV Download Testing
# Author: Jorden Allcock
#
# Description: File is responsible for:
#
#       - Initiating the CV Download operation to empty directory
#	- Ensuring the CV's are present in required directory
#	- Ensuring CV's are not zero-sized
####################################################################################################

###################################################################################
# Required imports
###################################################################################

import os                               # To enable file browsing of local directory
import sys
import datetime				# Required to show start/end datetime of processing
sys.path.append('..')                   # Required to import scripts from parent folder

import cv_link_pull

###################################################################################
# Checking contents of CV Directory
###################################################################################

logfile = open('/home/jallcock/environments/Final-Project/testing/cv_download_log.txt', 'a')

logfile.write('Starting processing at ' + str(datetime.datetime.now()) + '\n\n')

cv_directory = '/home/jallcock/environments/Final-Project/stored_cvs'

if os.listdir(cv_directory) != []:
    for file in os.listdir(cv_directory):
        if os.path.getsize(os.path.join(cv_directory, file)) > 0:
            logfile.write(file + ' - ' + str(os.path.getsize(os.path.join(cv_directory, file))) + '\n')
    logfile.write('Directory not empty - unable to download CVs')
else:
    logfile.write('Directory [' + cv_directory + '] Empty')

    logfile.write('\n\n')

###################################################################################
# Initiating CV Download process
###################################################################################

    logfile.write('Running CV Link Pull script\n')

    cv_link_pull.main('https://resumes.livecareer.com/search?jt=software%20engineering')

    logfile.write('CV\'s downloaded into CV Repository\n')

###################################################################################
# Checking contents of CV Directory after CV Download
###################################################################################

    if os.listdir(cv_directory) != []:
        for file in os.listdir(cv_directory):
            if os.path.getsize(os.path.join(cv_directory, file)) > 0:
                logfile.write(file + ' - ' + str(os.path.getsize(os.path.join(cv_directory, file))) + '\n')
            else:
                logfile.write('************************' + file + ' IS ZERO SIZED************************' + '\n')
    else:
        logfile.write('Files not written to directory')

logfile.write('Finished processing at ' + str(datetime.datetime.now()))

logfile.close()
