# -*- coding: utf-8 -*-

####################################################################################################
# Name:   CV Resource Score
# Author: Jorden Allcock
#
# Description: File is responsible for:
#
#       - Extracting link of CV text from the returned results (from search string parameter)
#       - Opening link for CV text, extracting and storing text
#
# Parameters:
#
#       - p_resource_request_tokens
# 	- p_cv_tokens
#
####################################################################################################

###################################################################################
# Required imports
###################################################################################

import collections                      # To enable dictionary addition/updating
import operator                         # To enable sorting of dictionary elements
import spacy

def main(p_resource_request_tokens, p_cv_tokens, p_file):

    nlp = spacy.load("en")
    similarity_bound = 0.6
    cv_scores_matrix = {}

    cv_token_similarities = collections.defaultdict(list)
    cv_token_similarity_score = 0

    for i, token1 in enumerate(p_resource_request_tokens):
        for x, token2 in enumerate(p_cv_tokens):
            try:
                # Removes keywords not of focus, and removes non-similar and identical matches
                if ((token1.pos_ == 'NOUN' or token1.pos_ == 'PROPN')
                and (token1.text != token2.text) and (token2.pos_ == 'NOUN' or token2.pos == 'PROPN')
                and token1.similarity(token2) >= similarity_bound
                and (token1.pos_ == 'NOUN' or token1.pos_ == 'PROPN')):
                    try:
                        #print(token1.text + '|' + token2.text + ' -> ' + str(token1.similarity(token2)))
                        cv_token_similarities[token1.text + '|' + token2.text].append(token1.similarity(token2))
                    except KeyError:
                        cv_token_similarities[token1.text + '|' + token2.text] = token1.similarity(token2)
    
                    cv_token_similarity_score = cv_token_similarity_score + token1.similarity(token2)
            except:
                continue;

    print('Similarity Score [' + str(cv_token_similarity_score)  + ']')
    return cv_token_similarity_score

    #cv_scores_matrix[p_file.encode('utf-8')] = (cv_token_similarity_score)

    #print('\nCV Scores Matrix')
    #sorted_scores_matrix = sorted(cv_scores_matrix.items(), key=operator.itemgetter(1), reverse=True)
    #print(sorted_scores_matrix)

    #return sorted_scores_matrix

if __name__ == "__main__":
     main(sys.argv[1])

