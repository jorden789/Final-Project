from __future__ import unicode_literals
import spacy
import random
nlp = spacy.load("en")

def cleanup(token, lower = True):
    if lower:
       token = token.lower()
    return token.strip()

#with open('/home/jallcock/environments/python_output/CV-34.txt', 'r') as myfile:
#    data=myfile.read().replace('\n', '')
#    data=myfile.read()
#    doc1 = nlp(data.decode('utf8'))

#    print(doc1)

#    for token in doc1:
#    	print (token)

#    print(doc1.ents)
    
#    labels = set([w.label_ for w in doc1.ents])
#    for label in labels:
#        entities = [cleanup(e.string, lower=False) for e in doc1.ents if label==e.label_] 
#        entities = list(set(entities)) 
#        print label, entities

    #for token in doc1:
#	print(token, token.lemma, token.lemma_)
#
 #   print(' ')
#
 #   for token in doc1:
#	print(token, token.pos, token.pos_)


######################################################################
# Training Data
######################################################################

LABEL = 'SKILL'

TRAIN_DATA = [
    ('SQL', {'entities': [(0, 3,'SKILL') ]})
]


#####################################################################
# Analyse text
#####################################################################

nlp = spacy.blank('en')
print("Created blank 'en' model")


if 'ner' not in nlp.pipe_names:
    ner = nlp.create_pipe('ner')
    nlp.add_pipe(ner)
# otherwise, get it, so we can add labels to it
else:
    ner = nlp.get_pipe('ner')

ner.add_label(LABEL)   # add new entity label to entity recognizer

other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
with nlp.disable_pipes(*other_pipes):  # only train NER
    optimizer = nlp.begin_training()
    for itn in range(20):
        random.shuffle(TRAIN_DATA)
        losses = {}
        for text, annotations in TRAIN_DATA:
            nlp.update([text], [annotations], sgd=optimizer, drop=0.35,
                       losses=losses)
#        print(losses)

    test_text = 'Do you like PL/SQL'
    doc = nlp(test_text)
    print("Entities in '%s'" % test_text)
    for ent in doc.ents:
        print(ent.label_, ent.text)
