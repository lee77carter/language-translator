# A Language Translator Script

import csv

# function defining an introduction
def intro(user):
  print('Welcome to the Spanish and French translator app.\nPlease enter an English word and press the "Enter" key.')
  print('\nType "done" at any time to exit')

def exit(user):
  print('\nThanks for using the translator app. Have a great day!')

# GLOBAL variables
translations = {} # translations dictionary

# Open CSV file in read mode
with open("translations.csv", "r") as words:
    reader = csv.DictReader(words, delimiter=",")
    for line in reader:
      english = line["English"].lower()
      spanish = line["Spanish"].lower()
      french = line["French"].lower()
      translations[english] = [spanish,french] #spanish = index 0 & french = index 1
      
done = False

# Actions at runtime
intro('user')
while not done:
  word = input("\nType an English word to translate:  ")
  word = word.lower()
  
  if word == "done":
    exit('user')
    done = True
  elif word in translations:
    print(f'\nSPANISH:{translations[word][0]}') #word = dictionary key & 0 = Spanish set to index 0 above
    print(f'\nFRENCH:{translations[word][1]}') #word = dictionary key & 0 = French set to index 1 above
  else:
    print("\nTranslation is not known")
    