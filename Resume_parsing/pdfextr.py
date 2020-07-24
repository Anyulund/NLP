#!/usr/bin/env python3

import pdf2image
import os
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import docxpy

PATH = '/Users/annanyulund/Documents/Resume_parsing/Resumes/'

'''-------------------------------------PDF Parser---------------------------------------------------'''
def delete_ppms():
  for file in os.listdir('Resumes'):
    if '.ppm' in file or '.DS_Store' in file:
      try:
          os.remove(PATH + file)
      except FileNotFoundError:
          pass

def pdf_extract(file, i):
  #print("extracting from file:", file)
  delete_ppms()
  images = pdf2image.convert_from_path(PATH + file, output_folder=PATH)
  j = 0
  for file in sorted (os.listdir('Resumes')):
    if '.ppm' in file and 'image' not in file:
      os.rename(PATH + file, PATH + 'image' + str(i) + '-' + str(j) + '.ppm')
      j += 1
  j = 0
  f = open(f'result{i}.txt', 'w')
  files = [f for f in os.listdir('Resumes') if '.ppm' in f]
  for file in sorted(files, key=lambda x: int(x[x.index('-') + 1: x.index('.')])):
      #print("extracting from:", file)
      temp = pytesseract.image_to_string(Image.open(PATH + file))
      f.write(temp)
  f.close()



'''----------------------------------------Word Parser---------------------------------------------------'''



def docx_extract(file, i):
    delete_ppms()
    j = 0
    for file in sorted (os.listdir('Resumes')):
        if '.docx' in file and 'file' not in file:
          os.rename(PATH + file, PATH + 'file' + str(i) + '_' + str(j) + '.docx')
          j += 1
    j = 0
    f = open(f'result{i}.txt', 'w')
    files = [f for f in os.listdir('Resumes') if '.docx' in f]
    for file in sorted(files, key=lambda x: int(x[x.index('-') + 1: x.index('.')])):
      #print("extracting from:", file)
      temp = docxpy.process(PATH + file)
      f.write(temp)
    f.close()

'''----------------------------------------Total Parser------------------------------------------------'''
'''
def pdf_extract(file, i):
  #print("extracting from file:", file)
  delete_ppms()
  images = pdf2image.convert_from_path(PATH + file, output_folder=PATH)
  j = 0
  for file in sorted (os.listdir('Resumes')):
    if '.ppm' in file and 'image' not in file:
      os.rename(PATH + file, PATH + 'image' + str(i) + '-' + str(j) + '.ppm')
    elif '.docx'
      j += 1
  j = 0
  f = open(f'result{i}.txt', 'w')
  files = [f for f in os.listdir('Resumes') if '.ppm' in f]
  for file in sorted(files, key=lambda x: int(x[x.index('-') + 1: x.index('.')])):
      #print("extracting from:", file)
      temp = pytesseract.image_to_string(Image.open(PATH + file))
      f.write(temp)
  f.close()
'''
