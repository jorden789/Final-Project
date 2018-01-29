#! /usr/bin/env python

####################################################################################################
# Name: CV Analysis Routine
# Author: Jorden Allcock
#
# Description: File is responsible for:
# 
# 	- Reading appropriate contents of specified resource request
# 	- Selecting appropriate information from CV (keywords)
# 	- Identifying similarity/match between CV elements and Resource Request elements
#
# Parameters:
#
# 	- p_resource_request_loc	Directory/file location of specified resource request to be
# 					analysed
#       
####################################################################################################

###################################################################################
# Required imports
###################################################################################

from __future__ import unicode_literals
import spacy
import random
nlp = spacy.load("en")
import xlrd

###################################################################################
# Common custom functions for processing
###################################################################################

def cleanup(token, lower = True):
    if lower:
       token = token.lower()
    return token.strip()


######################################################################
# Read Resource Request Contents
######################################################################

resource_request = xlrd.open_workbook('/home/jallcock/environments/Final-Project/resource_requests/resource_request_1.xlsx')
request_information = resource_request.sheet_by_index(0)

print('######################################################################')
print(' Resource Information ')
print('######################################################################')

print(' ')

job_title = request_information.cell(39, 3).value
tech_skills_required = request_information.cell(43, 3).value
bus_skills_required = request_information.cell(46, 3).value
additional_info = request_information.cell(49, 3).value

print('Required Role: ' + job_title)
print('Tech Required Skills: ' + tech_skills_required)
print('Bus. Required Skills: ' + bus_skills_required)
print('Additional Information: ' + additional_info)

######################################################################
# NLP Processing of Resource Information
######################################################################



######################################################################
# Rough Keyword Extract from CV
######################################################################

print(' ')

print('######################################################################')
print(' CV Information ')
print('######################################################################')

print(' ')

# Loop through all CV Files for Key Word Processing

# Open CV File ready for analysis
with open('/home/jallcock/environments/python_output/CV-10.txt', 'r') as myfile:
    data=myfile.read()
    doc1 = nlp(data.decode('utf8'))
    
    labels = set([w.label_ for w in doc1.ents])
    for label in labels:
        entities = [cleanup(e.string, lower=False) for e in doc1.ents if label==e.label_] 
        entities = list(set(entities)) 
        if label in ['ORG', 'PERSON', 'PRODUCT']:
            print label, entities

######################################################################
# Keyword Matching of Tokens between Resource Request and CV Info
######################################################################

            for entity in entities:
                entity_now = entity.decode('utf-8').replace('\n ', ' ').strip()
		if tech_skills_required.find(entity_now) > 0:
                    print 'Found [' + entity_now + ']'                

                if bus_skills_required.find(entity_now) > 0:
                    print 'Found [' + entity_now + ']'

                if additional_info.find(entity_now) > 0:
                    print 'Found [' + entity_now  + ']' 



######################################################################
# Near Neighbour Comparisons of Tokens between Resource Request and 
# CV Information
######################################################################



