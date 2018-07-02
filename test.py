import spacy
import en_core_web_sm


nlp = spacy.load('en_core_web_sm')

doc = nlp("cat".decode('utf8'))

print doc.similarity(nlp("can".decode('utf8')))

print doc.similarity(nlp("dog".decode('utf8')))

doc = nlp("hello good evening".decode('utf8'))

print doc.similarity(nlp("good night".decode('utf8')))
