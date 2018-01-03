import spacy
nlp = spacy.load('en')

doc1 = nlp("10,167 this's spacy tokenize test")

print(doc1)

for token in doc1:
	print (token)

for token in doc1:
	print(token, token.lemma, token.lemma_)

print( )

for token in doc1:
	print(token, token.pos, token.pos_)
