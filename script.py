from nltk import pos_tag, RegexpParser
from tokenize_words import word_sentence_tokenize
from chunk_counters import np_chunk_counter, vp_chunk_counter
# import text of choice 
text = open("dorian_gray.txt", encoding='utf-8').read().lower()

# sentence and word tokenize text 
word_tokenized_text = word_sentence_tokenize(text)

# store and print any word tokenized sentence 
single_word_tokenized_text = word_tokenized_text[100]


# create a list to hold part-of-speech tagged sentences 
pos_tagged_text = []

# create a for loop through each word tokenized sentence 
for token in word_tokenized_text:
  # part-of-speech tag each sentence and append to list of pos-tagged sentences 
  pos_tagged_text.append(pos_tag(token))

# store and print any part-of-speech tagged sentence 
#single_pos_sentence = pos_tagged_text[20]
#print(single_pos_sentence)

# define noun phrase chunk grammar 
np_chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"


# create noun phrase RegexpParser object 
np_chunk_parser = RegexpParser(np_chunk_grammar)

# define verb phrase chunk grammar 
vp_chunk_grammar = "VP: {<DT>?<JJ>*<NN><VB.*><RB.?>?}"

# create verb phrase RegexpParser object 
vp_chunk_parser = RegexpParser(vp_chunk_grammar)

# create a list to hold noun phrase chunked sentences and a list to hold verb phrase chunked sentences 
np_chunked_text = []
vp_chunked_text = []

# create a for loop through each pos-tagged sentence 
for pos in pos_tagged_text:
  # chunk each sentence and append to lists 
  np_chunked_text.append(np_chunk_parser.parse(pos))
  vp_chunked_text.append(vp_chunk_parser.parse(pos))

# store and print the most common NP-chunks 
most_common_np_chunks = np_chunk_counter(np_chunked_text)

print(most_common_np_chunks)
print('')
# store and print the most common VP-chunks 
most_common_vp_chunks = vp_chunk_counter(vp_chunked_text)
print(most_common_vp_chunks)
