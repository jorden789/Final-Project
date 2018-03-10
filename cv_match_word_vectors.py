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
import sys
import cv_resource_rank			# Custom script written to return the best candidate per job
import cv_resource_score

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


def main(p_resource_request_loc):

######################################################################
# Read Resource Request Contents
######################################################################

    #resource_request = xlrd.open_workbook('/home/jallcock/environments/Final-Project/resource_requests/resource_request_1.xlsx')
    resource_request = xlrd.open_workbook(p_resource_request_loc)
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

    for file in os.listdir('/home/jallcock/environments/Final-Project/stored_cvs/'):
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

            cv_scores_matrix[file.encode('utf-8')] = cv_resource_score.main(resource_request_tokens, cv_tokens, file)

    #print(cv_scores_matrix)

###################################################################################
# Build up the Ranked List of Candidates using Hungarian Algorithm
###################################################################################

    #cv_scores_matrix_pop = sorted(cv_scores_matrix.items(), key=operator.itemgetter(1), reverse=True)
    #cv_scores_matrix_pop = OrderedDict(sorted(cv_scores_matrix.items()))
    #print(cv_scores_matrix_pop)

    best_cvs = []

    for x  in range(0, 5):
        best_cv = cv_resource_rank.main(cv_scores_matrix)
        best_cv_position = best_cv[1]
        best_cv_name = best_cv[0]

        #best_cvs.append(cv_scores_matrix.keys()[best_cv_position]) 
        value_to_remove = list(cv_scores_matrix.keys())[best_cv_position]
        best_cvs.append(value_to_remove)
        del cv_scores_matrix[value_to_remove]

    print(best_cvs)
    return best_cvs

###################################################################################
# Word2Vec Analysis
###################################################################################

if __name__ == "__main__":
     main(sys.argv[1])

