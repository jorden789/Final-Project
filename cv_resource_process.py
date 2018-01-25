from __future__ import unicode_literals
import spacy
import random
nlp = spacy.load("en")
import xlrd

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

job_title = request_information.cell(39, 3)
tech_skills_required = request_information.cell(43, 3)
bus_skills_required = request_information.cell(46, 3)
additional_info = request_information.cell(49, 3)

print('Required Role: ' + job_title.value)
print('Tech Required Skills: ' + tech_skills_required.value)
print('Bus. Required Skills: ' + bus_skills_required.value)
print('Additional Information: ' + additional_info.value)

######################################################################
# Rough Keyword Extract from CV
######################################################################

print(' ')

print('######################################################################')
print(' CV Information ')
print('######################################################################')

print(' ')

with open('/home/jallcock/environments/python_output/CV-34.txt', 'r') as myfile:
    #data=myfile.read().replace('\n', '')
    data=myfile.read()
    doc1 = nlp(data.decode('utf8'))
    
    labels = set([w.label_ for w in doc1.ents])
    for label in labels:
        entities = [cleanup(e.string, lower=False) for e in doc1.ents if label==e.label_] 
        entities = list(set(entities)) 
        if label in ['ORG', 'PERSON', 'PRODUCT']:
            print label, entities



######################################################################
#  
######################################################################

