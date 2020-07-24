import spacy
from os import listdir
from os.path import isfile, basename, splitext, join
from os.path import splitext
from pdfextr import pdf_extract
from pdfextr import docx_extract
import nltk
import pandas as pd
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
from nameparser.parser import HumanName
from nltk.tag.stanford import StanfordNERTagger
#import docx2txt


pdf_files = []
docx_files = []

for f in listdir('Resumes'):
  full_name = join('Resumes', f)
  if isfile(full_name):
    name = basename(f)
    filename, ext = splitext(name)
    if ext == '.pdf':
      pdf_files.append(name)
    elif ext == ('.docx'):
    #elif ext in ('.doc', '.docx'):
      docx_files.append(name)

'''
for i in range(len(pdf_files)):
  pdf_file = pdf_files[i]
  pdf_extract(pdf_file, i)
'''

for k in range(len(docx_files)):
    docx_file = docx_files[k]
    for n in range(len(pdf_files),len(docx_files)+len(pdf_files)):
         docx_extract(docx_file,n)


#print(pdf_files)
#print(docx_files)
#print(range(len(pdf_files)))
#print(range(len(docx_files)))
#print(docx_files)
#print(range(len(pdf_files)+1,len(docx_files)+len(pdf_files)+1))

'''

nlp = spacy.load('en_core_web_sm')

PATH = '/Users/annanyulund/Documents/Resume_parsing/Resumes/'

names = []
organization = []
location = []
phone = []
date = []


for num in range(0, 1): # going 0 to 9
  file_name = f"result{num}.txt"
  file = open(file_name)
  doc = nlp(file.read())
  print(doc)
  file.close()


  for ent in doc.ents:
      print (ent.text, ent.label_)


for ent in doc.ents:
  if ent.label_ == 'DATE':
      date.append(ent)
  elif ent.label_ == 'ORG':
      organization.append(ent)
  elif ent.label_ == 'PERSON':
      names.append(ent)
  elif ent.label_ == 'GPE':
      location.append(ent)
  elif ent.label_ == 'CARDINAL':
      phone.append(ent)
      break

print('Name:',names)
print('Organizaton:',organization)
print ('Location:', location)
print ('Phone or email:', phone)

names1 = []
organization1 = []
location1 = []
phone1 = []
date1 = []

for ent in doc.ents:
  if ent.label_ == 'DATE':
      date1.append(ent)
  elif ent.label_ == 'ORG':
      organization1.append(ent)
  elif ent.label_ == 'PERSON':
      names1.append(ent)
  elif ent.label_ == 'GPE':
      location1.append(ent)
  elif ent.label_ == 'CARDINAL':
      phone1.append(ent)


all_names = pd.DataFrame(names1)
all_organizations = pd.DataFrame(organization1)
all_locations = pd.DataFrame(location1)
all_phones = pd.DataFrame(phone1)
all_dates = pd.DataFrame(date1)
print ('All Names:', all_names)
print ('All Organizations:', all_organizations)
print ('All Locations:', all_locations)
print ('All Phones and Emails:', all_phones)
print ('All Dates:', all_dates)
'''




'''
text = '/Users/annanyulund/Documents/Resume_parsing/result8.txt'
st = StanfordNERTagger('stanford-ner/all.3class.distsim.crf.ser.gz', 'stanford-ner/stanford-ner.jar')


for sent in nltk.sent_tokenize(text):
    tokens = nltk.tokenize.word_tokenize(sent)
    tags = st.tag(tokens)
    for tag in tags:
        if tag[1]=='PERSON': print (tag)

#print(person_list)
file.close()
'''
