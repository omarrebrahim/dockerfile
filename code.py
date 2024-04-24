import pandas as pd
file = open(r'C:\Users\HP\OneDrive\Desktop\project\random_paragraphs.txt..txt')
paragraph = file.readlines()
print(paragraph[:10]) 
file.close()

str(paragraph)

import nltk
from nltk.corpus import stopwords
 
nltk.download('stopwords')
print(stopwords.words('english'))

text = open(r'C:\Users\HP\Downloads\archive\random_paragraphs.txt..txt') 
  
# Create an empty dictionary 
d = dict() 
  
# Loop through each line of the file 
for line in text: 
    # Remove the leading spaces and newline character 
    line = line.strip() 
  
    # Convert the characters in line to 
    # lowercase to avoid case mismatch 
    line = line.lower() 
  
    # Split the line into words 
    words = line.split(" ") 
                         
  
    # Iterate over each word in line 
    for word in words: 
        # Check if the word is already in dictionary 
        if word in d: 
            # Increment count of word by 1 
            d[word] = d[word] + 1
        else: 
            # Add the word to dictionary with count 1 
            d[word] = 1
print(words[:100])  
# Print the contents of dictionary 
for key in list(d.keys()): 
    print(key, ":", d[key]) 

