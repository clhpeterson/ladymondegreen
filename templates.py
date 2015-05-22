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

def create_templates (word, vowels, vowel_code, blank_code, dictionary, semivowel_list, nothing_special_code, blank_to_vowel_code, blank_to_consonant_code):
	simplified = vowels_and_consonant_clusters (word, vowels)
	to_return = []
	originals = []
	lengths = []
	# if we start out with a consonant cluster, we can optionally add in a vowel at the beginning
	if simplified[0][0] == "c":
		to_return.append ([blank_code, vowel_code])
		originals.append ([nothing_special_code, blank_code])
		lengths.append (2)
	for entry in simplified:
		# if we have a vowel, it can become 0, 1, or 2 vowels
		if entry[0] == "v":
			# you should create a separate code for if it's a blank to vowerl
			to_return += [[vowel_code, blank_code], semivowel_list, [blank_code, vowel_code]]
			originals += [[nothing_special_code, entry[1][0]], [nothing_special_code, blank_code], [blank_to_vowel_code, entry[1][0]]]
			lengths += [2, len(semivowel_list), 2]
		else:
			# otherwise it's a consonant cluster, in which case we can insert a consonant cluster at the beginning
			to_return += [semivowel_list]
			lengths.append (len(semivowel_list))
			originals.append ([nothing_special_code, blank_code])
			of_interest = entry[1]
			# for each consonant, we can have C, CvC, or Cv
			for consonant in of_interest:
				to_return += [dictionary[consonant]]
				lengths.append (len (dictionary[consonant]))
				originals.append ([nothing_special_code, consonant])
				to_return += [[blank_code, vowel_code]]
				lengths.append (2)
				originals.append ([nothing_special_code, blank_code])
				to_return += [[blank_code]+dictionary[consonant]]
				lengths.append (1+len(dictionary[consonant]))
				originals.append ([blank_to_consonant_code, consonant])
			# we can also have a semivowel at the end of the consonant cluster
			to_return += [semivowel_list]
			lengths.append (len (semivowel_list))
			originals.append ([nothing_special_code, blank_code])
	# if we end with a consonant cluster, we can add on optional vowel
	if simplified[-1][0] == "c":
		to_return.append ([blank_code, vowel_code])
		lengths.append (2)
		originals.append ([nothing_special_code, blank_code])
	return to_return, lengths, originals

