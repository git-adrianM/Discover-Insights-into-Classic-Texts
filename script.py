from nltk import pos_tag, RegexpParser
from tokenize_words import word_sentence_tokenize
from chunk_counters import np_chunk_counter, vp_chunk_counter
# import text of choice here
text = open("dorian_gray.txt", encoding='utf-8').read().lower()

# sentence and word tokenize text here
word_tokenized_text = word_sentence_tokenize(text)

# store and print any word tokenized sentence here
single_word_tokenized_text = word_tokenized_text[100]


# create a list to hold part-of-speech tagged sentences here
pos_tagged_text = []

# create a for loop through each word tokenized sentence here
for token in word_tokenized_text:
  # part-of-speech tag each sentence and append to list of pos-tagged sentences here
  pos_tagged_text.append(pos_tag(token))

# store and print any part-of-speech tagged sentence here
single_pos_sentence = pos_tagged_text[20]
print(single_pos_sentence)

# define noun phrase chunk grammar here


# create noun phrase RegexpParser object here


# define verb phrase chunk grammar here


# create verb phrase RegexpParser object here


# create a list to hold noun phrase chunked sentences and a list to hold verb phrase chunked sentences here



# create a for loop through each pos-tagged sentence here

  # chunk each sentence and append to lists here
  
  

# store and print the most common NP-chunks here



# store and print the most common VP-chunks here

