from __future__ import division

def consonant_cluster_templates (consonant_cluster):
	to_return = []
	if len (consonant_cluster) == 1:
		of_interest = consonant_cluster[0]
		to_return += [[["c"], [of_interest]], [["c", "v", "c"], [of_interest, "v", of_interest]]]
	else:
		of_interest = consonant_cluster[0]
		all_variations = consonant_cluster_templates (consonant_cluster[1:])
		for entry in all_variations:
			to_return += [[entry[0], [of_interest] + entry[1]],[["c", "v"]+entry[0], [of_interest, "v"] + entry[1]], [["c", "v"]+entry[0], [of_interest, "v", of_interest] + entry[1]]]
	return to_return

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

def rough_templates (word, vowels, blank_code):
	# word should already be in the form of a consonant cluster
	templates = []
	lengths = []

	for entry in word:
		if entry[0] == "v":
			vowel = entry[1][0]
			new_temps = [	[["v"], [vowel]], 	[[], []],	[["v", "v"], [vowel, vowel]], 	[["v", "c", "v"], [vowel, blank_code, vowel]]	]
			templates.append (new_temps)
			lengths.append (4)
		else:
			consonant_cluster = entry[1]
			returned = consonant_cluster_templates (consonant_cluster)
			templates.append (returned)
			lengths.append (len (returned))
	return templates, lengths

			

