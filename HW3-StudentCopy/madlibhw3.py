# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text

import nltk
import random
from nltk.book import *
from nltk import word_tokenize,sent_tokenize

print("START*******")

debug = False #True


if debug:
	print ("Getting information from file madlib_test.txt...\n")

<<<<<<< HEAD
param =  (text2[:150])
print (' '.join(param))
tokens = nltk.word_tokenize(param)
tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples

if debug:
	print ("First few tagged tokens are:")
	for tup in tagged_tokens[:5]:
		print (tup)

tagmap = {"NN":"a noun","VB":"a verb","IN":"a preposition","JJ":"an adjective", "AT":"an article"}
substitution_probabilities = {"NN":0.15,"VB":0.10,"PRT":0.10,"JJ":0.10, "RB":0.10}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

final_words = []


for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print ("".join(final_words))

print("\n\nEND*******")
