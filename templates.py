from __future__ import division

# first we need to separate the word into vowels and consonant cluseters
def vowels_and_consonant_clusters (word, vowels):
	to_return = []
	consonant_cluster = []
	for entry in word:
		if entry in vowels:
			if consonant_cluster != []:
				to_return.append (["c", consonant_cluster])
				consonant_cluster = []
			to_return.append (["v", [entry]])
		else:
			consonant_cluster.append (entry)
	if consonant_cluster != []:
		to_return.append (["c", consonant_cluster])
	return to_return

def create_templates (word, vowels, vowel_code, blank_code, dictionary, semivowel_list):
	simplified = vowels_and_consonant_clusters (word, vowels)

	# semivowel_list needs to be of the form [[["-"], 0, 0], [["R"], 1, 0], ...]

	# we need to keep track of what substitutions we can make, the score associated with that substitution, and, in the case of vowels, what the original vowel was
	
	# each entry in to_return will be of the form [["c"/"v"], [[sub1], [score1]], [[sub2], [score2]],...]
	# the substitutions will be sorted from lowest to highest by score
	# "c"/"v" will either be "c" indicating that that block came from a consonant (cluster), or something like "AA" indicating the vowel that that block came from
	# lengths will keep track of the number of substitutions for each one

	to_return = []
	lengths = []

	# max_score is the maximum score that we are allowing:
	# 1 for inserting vowel at the beginning
	# 1 for inserting semivowel at beginning of consonant cluster
	# 3 for each consonant in consonant cluster
	# 1 for inserting semivowel at end of consonant cluster
	# 2 for each vowel
	# 1 for inserting vowel at the end of the word
	max_score = 0

	# vowel_subs
	# we need semivowel list to be of the form [["", 0], ["R", 1], ...]

	vowel_subs = [[[vowel_code], 0, 1], [[blank_code], 1, 0]]
	for entry in semivowel_list:
		vowel_subs.append ([[vowel_code, entry[0][0], vowel_code], 2+entry[1], 2])
	length_vowel_subs = 1 + 1 + len (semivowel_list)

	# if we start out with a consonant cluster, we can optionally add in a vowel at the beginning
	if simplified[0][0] == "c":
		to_return.append ([["-"], [[[blank_code], 0], [[vowel_code], 2]]])
		lengths.append (2)
		max_score += 1
	for entry in simplified:
		# if we have a vowel, it can become 0, 1, or 2 vowels
		if entry[0] == "v":
			vowel = entry[1][0]
			to_return.append ([vowel], vowel_subs)
			lengths.append (length_vowel_subs)
			max_score += 2
		else:
			# otherwise it's a consonant cluster, in which case we can insert a consonant cluster at the beginning
			of_interest = entry[1]
			if of_interest[0] not in semivowel_set:
				to_return += [["-"], semivowel_list] 
				lengths += len (semivowel_list)
				max_score += 1
			# for each consonant, we can have C, CvC, or Cv
			for consonant in of_interest:
				# you need to create a dictionary of allowable substitutions
				could_sub = dictionary[consonant]
				to_return += [["-"], could_sub]
				lengths += len (could_sub)
				max_score += 3
			# we can also have a semivowel at the end of the consonant cluster
			if of_interest[-1] not in semivowel_set:
				to_return += [["-"], semivowel_list]
				lengths += len (semivowel_list)
				max_score += 1
	# if we end with a consonant cluster, we can add on optional vowel
	if simplified[-1][0] == "c":
		to_return.append ([["-"], [[[blank_code], 0], [[vowel_code], 2]]])
		lengths.append (2)
		max_score += 1
	return to_return, lengths, max_score

