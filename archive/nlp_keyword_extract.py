####################################################################################################
# Name: CV Parse Routine
# Author: Jorden Allcock
# 
# Description: Script is responsible for looping through the extracted CV Information, pre-formatt-
# ing the text such that only basic characters remain, defining the model language base and custom
# attributes ready for text reduction to highlight presence of key words.
####################################################################################################

from __future__ import unicode_literals, print_function

import plac
import random
from pathlib import Path
import spacy
import sys, os

####################################################################################################
# Custom Training Data to highlight key phrases based on Resource Request
####################################################################################################

# new entity label
LABEL = 'SKILL'

TRAIN_DATA = [
   # (" PL/SQL ", {'entities': [(1, 7, 'SKILL')]}), (" No records available", {'entities': []}),
    #("SQL ", {'entities': [(0, 3, 'SKILL')]}), 
    (" No records available", {'entities': []}), 
    ("Originally based upon relational algebra and tuple relational calculus, SQL consists of many types of statements", {'entities': [(72, 75, 'SKILL')]}), 
    ("SQL is a domain-specific language used in programming", {'entities': [(0, 3, 'SKILL')]}), 
    ("SQL", {'entities': [(0, 3, 'SKILL')]})
]


@plac.annotations(
    model=("Model name. Defaults to blank 'en' model.", "option", "m", str),
    new_model_name=("New model name for model meta.", "option", "nm", str),
    output_dir=("Optional output directory", "option", "o", Path),
    n_iter=("Number of training iterations", "option", "n", int),
    cv_input=("File Location of specific CV", "option", "cv", str))


def main(model=None, new_model_name='animal', output_dir=None, n_iter=20, cv_input=''):
    """Set up the pipeline and entity recognizer, and train the new entity."""
    if model is not None:
        nlp = spacy.load(model)  # load existing spaCy model
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank('en')  # create blank Language class
        print("Created blank 'en' model")

    # Add entity recognizer to model if it's not in the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner)
    # otherwise, get it, so we can add labels to it
    else:
        ner = nlp.get_pipe('ner')

    ner.add_label(LABEL)   # add new entity label to entity recognizer

    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        optimizer = nlp.begin_training()
        for itn in range(n_iter):
            random.shuffle(TRAIN_DATA)
            losses = {}
            for text, annotations in TRAIN_DATA:
                nlp.update([text], [annotations], sgd=optimizer, drop=0.35, losses=losses)
#            print(losses)


####################################################################################################
# Pull of CV Text
####################################################################################################

        print('Specified CV: ' + cv_input)
        #cv_to_process = open(os.path.join(cv_input), 'r')
        cv_to_process=open(cv_input, 'r')
        cv_text = cv_to_process.read()
        cv_to_process.close()

####################################################################################################
# Analysis of CV Information using specified filters for keywords
####################################################################################################

        #test_text = 'Do you like PL/SQL'
        doc = nlp(cv_text.decode('utf-8'))
        #print("Entities in '%s'" % test_text)
        for ent in doc.ents:
            #print('Skill Keyword: ' + ent.label_, ent.text)
            print('Skill Keyword: ' + ent.text)

####################################################################################################
# Analysis of CV information selecting Nouns
####################################################################################################

                

####################################################################################################
# Output of CV's with highlighted key words
####################################################################################################


if __name__ == '__main__':
    plac.call(main)
