from __future__ import division
import sys
import copy

vowels = ["AA", "AE", "AH", "AO", "AW", "AY", "EH", "ER", "EY", "IH", "IY", "OW", "OY", "UH", "UW"]

consonants_array = [
		["B",	[0,	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1,	-1,	-1, 	0, 	-1, 	-1, 	-1, 	-1, 	-1,	1, 	-1,	-1,	-1,	-1,	-1]],
		["CH",	[-1,	0, 	2, 	2, 	-1, 	-1, 	0, 	-1, 	-1, 	-1,	-1,	-1, 	-1, 	-1, 	-1, 	0, 	2, 	2,	-1, 	-1,	2,	-1,	0,	-1]],
		["D",	[-1,	2, 	0, 	1, 	-1, 	-1, 	2, 	-1, 	-1, 	-1,	-1,	-1, 	-1, 	-1, 	-1, 	-1, 	0, 	1,	-1, 	-1,	-1,	-1,	-1,	-1]],
		["DH",	[-1,	-1, 	1, 	0, 	2, 	-1, 	-1, 	-1, 	-1, 	-1,	-1,	-1, 	-1, 	-1, 	-1, 	-1, 	1, 	0,	2, 	-1,	-1,	-1,	-1,	-1]],
		["F",	[-1,	-1, 	-1, 	-1, 	0, 	-1, 	-1, 	-1, 	-1, 	-1,	-1,	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	2,	0, 	-1,	-1,	-1,	-1,	-1]],
		["G",	[-1,	-1, 	-1, 	-1, 	-1, 	0, 	-1, 	0, 	-1, 	-1,	-1,	2, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1,	-1, 	-1,	-1,	-1,	-1,	-1]],
		["JH",	[-1,	0, 	2, 	2, 	-1, 	-1, 	0, 	-1, 	-1, 	-1,	-1,	-1, 	-1, 	-1, 	-1, 	0, 	2, 	2,	-1, 	-1,	2,	-1,	0,	-1]],
		["K",	[-1,	-1, 	-1, 	-1, 	-1, 	0, 	-1, 	0, 	-1, 	-1,	-1,	2, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1,	-1, 	-1,	-1,	-1,	-1,	-1]],
		["L",	[-1,	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	0, 	-1,	-1,	-1, 	-1, 	1, 	-1, 	-1, 	-1, 	-1,	-1, 	1,	2,	-1,	-1,	2]],
		["M",	[-1,	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	0,	1,	2, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1,	-1, 	-1,	-1,	-1,	-1,	-1]],
		["N",	[-1,	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	1,	0,	1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1,	-1, 	-1,	-1,	-1,	-1,	-1]],
		["NG",	[-1,	-1, 	-1, 	-1, 	-1, 	2, 	-1, 	2, 	-1, 	2,	1,	0, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1,	-1, 	-1,	-1,	-1,	-1,	-1]],
		["P",	[0,	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1,	-1,	-1, 	0, 	-1, 	-1, 	-1, 	-1, 	-1,	-1, 	-1,	-1,	-1,	-1,	-1]],
		["R",	[-1,	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	1, 	-1,	-1,	-1, 	-1, 	0, 	-1, 	-1, 	-1, 	-1,	-1, 	0,	2,	-1,	-1,	2]],
		["S",	[-1,	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1,	-1,	-1, 	-1, 	-1, 	0, 	1, 	-1, 	-1,	-1, 	-1,	-1,	0,	1,	-1]],
		["SH",	[-1,	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1,	-1,	-1, 	-1, 	-1, 	1, 	0, 	-1, 	-1,	-1, 	-1,	-1,	1,	0,	-1]],
		["T",	[-1,	2, 	0, 	1, 	-1, 	-1, 	2, 	-1, 	-1, 	-1,	-1,	-1, 	-1, 	-1, 	-1, 	-1, 	0, 	1,	-1, 	-1,	-1,	-1,	-1,	-1]],
		["TH",	[-1,	-1, 	1, 	0, 	2, 	-1, 	-1, 	-1, 	-1, 	-1,	-1,	-1, 	-1, 	-1, 	-1, 	-1, 	1, 	0,	2, 	-1,	-1,	-1,	-1,	-1]],
		["V",	[1,	-1, 	-1, 	2, 	0, 	-1, 	-1, 	-1, 	-1, 	-1,	-1,	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1,	0, 	1,	-1,	-1,	-1,	-1]],
		["W",	[-1,	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	1, 	-1,	-1,	-1, 	-1, 	0, 	-1, 	-1, 	-1, 	-1,	-1, 	0,	2,	-1,	-1,	1]],
		["Y",	[-1,	2, 	-1, 	-1, 	-1, 	-1, 	2, 	-1, 	2, 	-1,	-1,	-1, 	-1, 	2, 	-1, 	-1, 	-1, 	-1,	-1, 	2,	0,	-1,	-1,	1]],
		["Z",	[-1,	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1,	-1,	-1, 	-1, 	-1, 	0, 	1, 	-1, 	-1,	-1, 	-1,	-1,	0,	1,	-1]],
		["ZH",	[-1,	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1,	-1,	-1, 	-1, 	-1, 	1, 	0, 	-1, 	-1,	-1, 	-1,	-1,	1,	0,	-1]],
		["-",	[-1,	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	-1, 	2, 	-1,	-1,	-1, 	-1, 	2, 	-1, 	-1, 	-1, 	-1,	-1, 	1,	1,	-1,	-1,	0]]
		]

# now we create the individual classes

consonants = [entry[0] for entry in consonants_array]

classes = []
dont_look = set()
for i in range (0, len (consonants_array)):
	if i not in dont_look:
		to_add = []
		of_interest = consonants_array[i][1]
		for j in range (0, len (of_interest)):
			if of_interest[j] != -1:
				if consonants_array[j][1] == of_interest:
					to_add.append (consonants_array[j][0])
					dont_look.add (j)
		classes.append (to_add)

# for example consonant_to_entry["B"] = 0
consonant_to_entry = {}
for i in range (0, len (consonants_array)):
	consonant_to_entry[consonants_array[i][0]] = i

# for example consonant_to_entry["JH"] = 1
consonant_to_code = {}
for i in range (0, len (classes)):
	of_interest = classes[i]
	for entry in of_interest:
		consonant_to_code[entry] = i

# for example substitutions[0] = [*all the things that "B" can become indexed by class index*]
substitutions = {}
for i in range (0, len (classes)):
	example = consonants_array[consonant_to_entry[classes[i][0]]][1]
	subs = set()
	for j in range (0, len (example)):
		if example[j] != -1:
			subs.add (consonant_to_code[consonants_array[j][0]])
	subs = list (subs)
	substitutions[i] = subs

vowel_code = "v"
blank_code = len(classes)-1

# we need a dictionary that gives the scores to be inserted into create_templates.
# needs to be sorted by score

# we need to create a score matrix based on the new classes

class_scores_matrix = []
for i in range (0, len (classes)):
	to_append = []
	index = consonant_to_entry[classes[i][0]]
	for j in range (0, len (classes)):
		new_index = consonant_to_entry[classes[j][0]]
		to_append.append (consonants_array[index][1][new_index])
	class_scores_matrix.append (to_append)

scores_dict = {}
scores_dict_last = {}
for i in range (0, len (classes)):
	possible = substitutions[i]
	with_scores = []
	for entry in possible:
		with_scores.append ([entry, class_scores_matrix[i][entry]])
	all_possible = []
	all_possible_last = []
	for entry1 in with_scores:
		all_possible.append ( ([entry1[0]], entry1[1], 0))
		all_possible_last.append ( ([entry1[0]], entry1[1], 0))
		all_possible.append ( ([entry1[0], vowel_code], entry1[1]+2, 1))
		for entry2 in with_scores:
			if entry1 != entry2:
				all_possible.append ( ([entry1[0], entry2[0]], max(entry1[1], entry2[1]), 0))
				all_possible_last.append ( ([entry1[0], entry2[0]],max(entry1[1], entry2[1]), 0))
			all_possible.append ( ([entry1[0], vowel_code, entry2[0]], max(entry1[1],entry2[1])+2, 1))
	# need to sort them both
	# bozo sort

	all_possible = sorted (all_possible, key=lambda entry:entry[1])
	all_possible_last = sorted (all_possible_last, key=lambda entry:entry[1])

	scores_dict[i] = all_possible
	scores_dict_last[i] = all_possible_last

semivowel_list = []
for entry in substitutions[17]:
	semivowel_list.append (([entry], class_scores_matrix[17][entry], 0))

semivowel_list = sorted (semivowel_list, key=lambda entry:entry[1])




def create_all_templates (my_array, is_last):
	if len (my_array) == 1:
		if is_last == True:
			return [my_array, [my_array[0], "v", my_array[0]]]
		else:
			return [my_array, [my_array[0], "v", my_array[0]], [my_array[0], "v"]]
	start = create_all_templates (my_array[:1], False)
	to_return = []
	smaller = create_all_templates (my_array[1:], len(my_array[1:]) == 1)
	for entry in start:
		for entry2 in smaller:
			to_return.append (entry+entry2)
	return to_return


def get_next_one (where_at, bases):
	to_return = copy.deepcopy(where_at)
	index = 0
	while index < len(to_return):
		to_return[index] += 1
		if to_return[index] == bases[index]:
			to_return[index] = 0
			index += 1
		else:
			return to_return
	return False


def create_reduced_word (word, consonants, blank_code):
	to_return = []
	last_one = None
	for entry in word:
		if entry == blank_code:
			continue
		if entry != last_one or entry not in consonants:
			to_return.append (entry)
		last_one = entry
	return to_return



file = open('dictionary.txt', 'r')

just_words = []

words = []

for i in range(0, 126):
	file.readline()

for line in file:
	new_word = line[:-1]
	new_word = new_word.split("  ")
	word = new_word[0]
	if word[-1] == ")":
		word = word[:-3]
	pro = new_word[1]
	phonemes = pro.split(' ')
	for i in range(0, len(phonemes)):
		if phonemes[i][-1] in set(["0", "1", "2"]):
			phonemes[i] = phonemes[i][:-1]
	just_words.append(word)
	words.append([word, phonemes])

# remove HH
for entry in words:
	of_interest = entry[1]
	of_interest[:] = [x for x in of_interest if x != "HH"]

words = words[:-5]

# substitute words for their codes

for word in words:
	of_interest = word[1]
	code_word = []
	for phoneme in of_interest:
		if phoneme in consonants:
			code_word.append (consonant_to_code[phoneme])
		else:
			code_word.append (phoneme)
	code_word = create_reduced_word (code_word, consonants, blank_code)
	word.append(code_word)

def create_word_dictionary (words):
	to_return = dict()
	keys = [""]
	for entry in words:
		word = entry[0]
		if word != keys[-1]:
			to_return[word] = [{"arpa":entry[1], "code":entry[2]}]
			keys.append(word)
		else:
			to_return[word].append ([{"arpa":entry[1], "code":entry[2]}])
	return to_return

word_dictionary = create_word_dictionary (words)

def phrase_to_phonemes (phrase, word_dict):
	words = phrase.split(" ")
	words = [entry.upper() for entry in words]
	to_return = []
	for entry in words:
		try:
			to_return += word_dict[entry][0]["arpa"]
		except:
			print "Invalid word:", entry
			return
	return to_return

def single_word (subs, indices):
	to_return = []
	for i in range (0, len(indices)):
		to_return.append (subs[i][indices[i]])
	return to_return

def create_all_variations (word, substitutes, vowel_code, blank_code):
	subs = []
	base = []
	for entry in word:
		new_sub = substitutes[entry]
		subs.append (new_sub)
		base.append (len (new_sub))
	to_return = []
	where = [0 for i in range(0, len (base))]
	while where != False:
		new_word = single_word (subs, where)
		new_word = create_reduced_word (new_word, vowel_code, blank_code)
		to_return.append (new_word)
		where = get_next_one (where, base)
	return to_return

def create_all_variations2 (subs, base, vowel_code, blank_code):
	to_return = []
	where = [0 for i in range (0, len (base))]
	while where != False:
		new_word = single_word (subs, where)
		new_word = create_reduced_word (new_word, vowel_code, blank_code)
		to_return.append (new_word)
		where = get_next_one (where, base)
	return to_return




def create_trie (words, substitutes, vowel_code, blank_code):
	# words should not be words, but codes
	root = dict()
	for i in range(0, len(words)):
		word = words[i][2]
		new_words = create_all_variations (word, substitutes, vowel_code, blank_code)
		for entry in new_words:
			child = root
			for code in entry:
				if code in child.keys():
					child = child[code]
				else:
					child[code] = dict()
					child = child[code]
			if "words" in child.keys():
				child["words"].append(i)
			else:
				child["words"] = [i]
	return root

# you_tried = create_trie (words, substitutes, 14, -1)

# just_words = set(just_words)

# you need to have a thing which combines two interchangeable consecutive letters
# into one



'''
file = open('mad_gab.txt', 'r')

i = 1
for line in file:
	line = line[:-1]
	words = line.split(" ")
	words = [entry.upper() for entry in words]
	for entry in words:
		if entry not in just_words:
			print i, entry
	i += 1
'''

# genius! you preprocess the data to contain all variations of the word
'''
unique = set()
for entry in words:
	real = tuple (entry[2])
	if real not in unique:
		unique.add (real)


consonants = set([0,1,2,3,4,5,6,7,8,9,10,11,12,13])

firsts = []
middles = []
ends = []

for entry in words:
	of_interest = entry[2]
	# first find the consonant clusters at the beginning
	to_append = []
	for letter in of_interest:
		if letter in consonants:
			to_append.append (letter)
		else:
			break
	if to_append != []:
		firsts.append ([to_append, entry])
	to_append = []
	i = -1
	while i > -1*len(of_interest):
		if of_interest[i] in consonants:
			to_append.insert (0, of_interest[i])
		else:
			break
		i -= 1
	if to_append != []:
		ends.append ([to_append, entry])
	to_append = []
	for i in range (0, len(of_interest)):
		if len(to_append) >= 6:
			print entry
		if of_interest[i] in consonants:
			to_append.append (of_interest[i])
		else:
			if to_append != []:
				middles.append ([to_append, entry])
			to_append = []

'''
	


