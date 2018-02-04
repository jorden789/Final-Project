#! /usr/bin/env python

####################################################################################################
# Name: CV Match Routin - Word Vectors on Keywords
# Author: Jorden Allcock
#
# Description: File is responsible for:
#
#       - Reading appropriate contents of specified resource request
#       - Selecting appropriate information from CV (keywords)
#       - Identifying similarity/match between CV elements and Resource Request elements
#
# Parameters:
#
#       - p_resource_request_loc        Directory/file location of specified resource request to be
#                                       analysed
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
import os

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

###################################################################################
# Resource Information Analysis
###################################################################################

#tech_skills_doc = nlp(tech_skills_required)
#bus_skills_doc = nlp(bus_skills_required)
#additional_info_doc = nlp(additional_info)
all_items_doc = nlp(tech_skills_required + bus_skills_required + additional_info)

for skills_token in all_items_doc:
    if (skills_token.pos_ == 'NOUN' or skills_token.pos_ == 'PROPN'):
        print(skills_token, skills_token.pos_)

###################################################################################
# CV Information Input
###################################################################################




###################################################################################
# CV Information Parse
###################################################################################





###################################################################################
# Word2Vec Compute
###################################################################################


#tokens = nlp(u'sql plsql java oracle ebusiness')
resource_request_tokens = nlp(all_items_doc.text)
cv_tokens = nlp(all_items_doc.text)



for token1 in resource_request_tokens:
    for token2 in cv_tokens:
	# Removes keywords not of focus, and removes non-similar and identical matches
        if ((token1.pos_ == 'NOUN' or token1.pos_ == 'PROPN') and token1.similarity(token2) > 0.4 and token1.similarity(token2) < 0.98):
            print(token1.text + '|' + token2.text + ' -> ' + str(token1.similarity(token2)))


###################################################################################
# Word2Vec Analysis
###################################################################################

