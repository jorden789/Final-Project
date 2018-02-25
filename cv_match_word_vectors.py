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

###################
# Actions left are:
# 
# - Remove Duplicate Tokens
# - Sort out appropriate weighting system
# - Determine boundary settings for similarity
###################

###################################################################################
# Required imports
###################################################################################

from __future__ import unicode_literals
import spacy
import random
import xlrd				# To enable analysis of Resource Request Spreadsheet
import os				# To enable file browsing of local directory
import collections			# To enable dictionary addition/updating
import operator				# To enable sorting of dictionary elements

nlp = spacy.load("en")
similarity_bound = 0.6

#nlp = spacy.load("en_core_web_lg")


######################################################################
# Re-used Functions
######################################################################

def remove_duplicate_tokens(tokens):
    unique_tokens = []
    token_matching = set()
    lower_tokens = [token.text.lower() for token in tokens]
    for token in lower_tokens:
        if token not in token_matching:
            unique_tokens.append(token)
            token_matching.add(token)
    return unique_tokens

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

#print('Removing Resource Request Duplicate Tokens')
#resource_request_tokens = remove_duplicate_tokens(all_items_doc)


for skills_token in all_items_doc:
    if (skills_token.pos_ == 'NOUN' or skills_token.pos_ == 'PROPN'):
        print(skills_token, skills_token.pos_, skills_token.vector_norm)

###################################################################################
# CV Information Input
###################################################################################

cv_scores_matrix = {}

for file in os.listdir('/home/jallcock/environments/python_output'):
    with open('/home/jallcock/environments/python_output/' + file, 'r') as myfile:
        #print('File being processed: ' + file)
        data=myfile.read()
        #doc1 = nlp(data.decode('utf8'))
        doc1 = nlp(data.decode('utf-8'))


###################################################################################
# CV Information Parse
###################################################################################





###################################################################################
# Word2Vec Compute
###################################################################################


        resource_request_tokens = all_items_doc
        cv_tokens = doc1			


        print('File being processed: ' + file)
        #print('Removing Resource Request Duplicate Tokens')
        #resource_request_tokens = remove_duplicate_tokens(resource_request_tokens)
        
        #print('Removing CV Information Duplicate Tokens')
        #cv_tokens = remove_duplicate_tokens(cv_tokens)
        #print(cv_tokens)

        cv_token_similarities = collections.defaultdict(list)
        cv_token_similarity_score = 0

        for i, token1 in enumerate(resource_request_tokens):
            for x, token2 in enumerate(cv_tokens):
	        # Removes keywords not of focus, and removes non-similar and identical matches
                if ((token1.pos_ == 'NOUN' or token1.pos_ == 'PROPN') 
                and (token1.text != token2.text) and (token2.pos_ == 'NOUN' or token2.pos == 'PROPN') 
                and abs(token1.similarity(token2)) > similarity_bound 
                and (token1.pos_ == 'NOUN' or token1.pos_ == 'PROPN')):
                    try:
                        #print(token1.text + '|' + token2.text + ' -> ' + str(token1.similarity(token2)))
                        cv_token_similarities[token1.text + '|' + token2.text].append(token1.similarity(token2))
                    except KeyError:
                         cv_token_similarities[token1.text + '|' + token2.text] = token1.similarity(token2)
                    cv_token_similarity_score = cv_token_similarity_score + token1.similarity(token2)                

        print('Similarity Score [' + str(cv_token_similarity_score)  + ']')
        cv_scores_matrix[file.encode('utf-8')] = (cv_token_similarity_score)

print('\nCV Scores Matrix')
sorted_scores_matrix = sorted(cv_scores_matrix.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_scores_matrix)

###################################################################################
# Word2Vec Analysis
###################################################################################

