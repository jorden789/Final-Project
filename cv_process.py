#! /usr/bin/env python

####################################################################################################
# Name: CV Process
# Author: Jorden Allcock
# 
# Description: File is not essential to core processing, however is designed to assist in formatt-
# ing CV's into an easier to read format.
# 
# Parameters: 
# 
# 	p_directory - Location of file to be processed to be passed as an absolute value
####################################################################################################

###################################################################################
# Required imports
###################################################################################

import sys
import os

###################################################################################
# read file and store contents into suitable variable
###################################################################################

def main(p_directory):
    for file in os.listdir(p_directory):
        cv_to_process = open(os.path.join(p_directory, file), 'r')
        cv_information = cv_to_process.read()
        cv_to_process.close()

        print('File ' + file + ' has been read successfully')

###################################################################################
# Formatting operations to occur are:
# 
# 	1. Remove extra blank spaces to condense the CV information
###################################################################################

        for x in range(0, 10):
            #cv_information = cv_information.decode('utf-8', 'ignore').lower().encode('utf-8')
            cv_information = cv_information.replace('  ', ' ')
            cv_information = cv_information.replace(' \r', ' ')
            cv_information = cv_information.replace(' \n', ' ')
            cv_information = cv_information.replace('\u2022', ' ')
            cv_information = cv_information.replace('\uff0d', ' ')



###################################################################################
# Writing formatted contents back to file
###################################################################################

        cv_info_to_send = open((os.path.join(p_directory, file)), 'w')
        cv_info_to_send.write(cv_information)
        cv_info_to_send.close()

if __name__ == "__main__":
     main(sys.argv[1])
