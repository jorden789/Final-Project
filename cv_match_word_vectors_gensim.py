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

#from __future__ import unicode_literals
from gensim import models
#import random
#nlp = spacy.load("en")
#import xlrd
import os

###################################################################################
# Word2Vec Gensim Compute
###################################################################################


sentences = 'sql plsql java ebusiness oracle'
model = models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
words = list(model.wv.vocab)
print(words)

###################################################################################
# Word2Vec Gensim Analysis
###################################################################################

